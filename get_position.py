import pyautogui
import sqlite3
import pandas as pd
def update_position(position = 0):
    from db import conn_db
    conn = conn_db()
    cursor = conn.cursor()
    
    if not position == 0:
        x = position.x
        y= position.y

        

        sql = f"""
                INSERT INTO pyautogui_position (posion_name, position_x, position_y )
                VALUES ('close_print_panel', {x}, {y})
                ON CONFLICT DO UPDATE SET 
                position_x = {x}, position_y = {y}
                """
        cursor.execute(sql)
        conn.commit()
        
    sql = "SELECT position_x, position_y FROM pyautogui_position WHERE posion_name = 'close_print_panel'"
    df = pd.read_sql_query(sql, conn)
    
    cursor.close()
    conn.close()
    return df

