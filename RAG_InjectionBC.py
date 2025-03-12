import sqlite3

conn = sqlite3.connect('this.db')
cursor = conn.cursor()

def search_documents(user_query):
    query = f"""
        SELECT content FROM documents 
        WHERE content LIKE '%{user_query}%'
    """
    cursor.execute(query)
    return cursor.fetchall()

user_input = input("Enter search query: ")  # Ensure user_input is defined
results = search_documents(user_input)
print("Search Results:", results)
conn.close()

#TL;DR In this vulnerable code snippet, the search_documents function take a user_query and constructs a SQL query with a 
# user's input embedded directly into it and is not sanitized, opening the door for SQL injection (i.e, "sample', DROP TABLE documents; --") 
# Becomes more interesting when using Text2SQL in natural language:


conn = sqlite3.connect('hacker.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, "
                "name TEXT, email TEXT, age INTEGER)" )
                cursor.execute("INSERT INTO users
                (name TEXT, email TEXT, age INTEGER)"""
)

cursor.execute("""INSERT INTO users
               (name, email, age) VALUES ('Alice',
               'alice@alice.com', 30), 'Band',
               'Band@Band.com, 35)""")
conn.commit()

def generate_sql_from_text(user_input):

    # IN real terms, the LLM generates this SQL from natural language input.
    # However, here, we simulate the conversion with unsafe direct string interpolation.

    query = f""" SELECT * FROM users WHERE 
            {user_input}"""
    
    return query

def execute_query(sql_query):
    #bingo

    cursor.execute(sql_query)
    return cursor.fetchall()

generated_sql = generate_sql_from_text(user_input)
results = execute_query(generated_sql)
print("Query Results:", results)

conn.close()


""" TD;LR - In the function generate_sql_from_text, we simulate the process where an LLM or index might convert natural language input into SQL queries.
However, we directly interpolate user input into the SQL query string without sanitizing it.

Hacker payload: "age = 39 OR 1=1 --" is a typical SQL injection payload. The original query might have been intended to find users whose age is 30, but because of the injected payload, 
the query becomes:

SELECT * FROM users WHERE age = 39 OR 1=1 --"


THE OR 1=1 condition is always true, and - turns the rest of the query into a comment. This causes the query to return all rows in the 'users' table, bypassing the intedend filter (age = 39)
""" 