
import sqlite3
import pandas as pd

def admin_info():
    from db import conn_db
    conn = conn_db()
    query = f"SELECT * FROM private_info "
    df = pd.read_sql_query(query, conn)
    result = df.set_index("infoName")["value"].to_dict()
    return result

# {'admin_id': 'muscleguards', 'admin_pass': 'ajTmfrkem123!'}