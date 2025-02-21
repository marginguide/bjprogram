import sqlite3, os

# 현재 프로그램의 경로
basedir = os.path.abspath(os.path.dirname(__file__))

db_dir = os.path.join(basedir, "data")
if not os.path.exists(db_dir):
    os.makedirs(db_dir)
db_path = os.path.join(db_dir, "db.db")    
conn = sqlite3.connect(db_path)
cursor= conn.cursor()
# DB용 폴더 생성


def create_table():
    query = f"CREATE TABLE IF NOT EXISTS 'token' ( tokenType TEXT  PRIMARY KEY, tokenValue TEXT, createAt TEXT, validTime TEXT )"
    cursor.execute(query)
    conn.commit()


query = "INSERT INTO token (tokenType, tokenValue) VALUES ('access', 'zF5ykHUiChbkLTegSUGcJH')"
cursor.execute(query)
conn.commit()

query = "INSERT INTO token (tokenType, tokenValue) VALUES ('refresh', 'paS0ej7wWiDTj2PuDbFOiA')"
cursor.execute(query)
conn.commit()