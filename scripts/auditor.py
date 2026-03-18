import os
from github import Github, Auth
from groq import Groq

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
REPO_NAME = os.getenv("REPO_NAME" )
PR_NUMBER = int(os.getenv("PR_NUMBER"))

def run_ai_audit():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("Error: GITHUB_TOKEN not found in environment!")
        return
    auth = Auth.Token(GITHUB_TOKEN)
    g = Github(auth=auth)
    client = Groq(api_key=GROQ_API_KEY)
    
    repo = g.get_repo(REPO_NAME)
    pr = repo.get_pull(PR_NUMBER)
    
    diff_text = ""
    for file in pr.get_files(): #gets only the files modified
        diff_text += f"--- File: {file.filename} ---\n{file.patch}\n\n"

    system_prompt = (
        "You are a Senior Product Engineer. Review the following code diff. "
        "Highlight security risks (SQL injection, hardcoded keys) and logic bugs. "
        "Keep your response concise and use a Markdown table for specific line suggestions."
    )
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Review this diff:\n{diff_text}"}
        ]
    )
    
    review_feedback = response.choices[0].message.content

    pr.create_issue_comment(f"### 🤖 AI Code Review\n\n{review_feedback}")
    print("Audit complete! Check your Pull Request for the comment.")

if __name__ == "__main__":
    run_ai_audit()