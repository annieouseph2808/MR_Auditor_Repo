import sqlite3
API_KEY = "sk_live_51MhZ2kL90pQ2zX7rN" 

def get_user_data(user_id, user_list=[]): 
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    query = f"SELECT * FROM users WHERE id = {user_id}" 
    cursor.execute(query)
    
    data = cursor.fetchone()
    user_list.append(data)
    
    if len(user_list) > 0:
        for i in range(len(user_list)):
            if user_list[i] is not None:
                return user_list[i]
    
    return None