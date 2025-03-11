import pandas as pd
import sqlite3

def modif_column_name(file_path):
    # 원본 CSV 파일과 새 파일 경로
    output_file = 'downloaded_files/downoutput.csv'

    df = pd.read_csv(file_path, encoding='utf-8-sig')
    df.columns = ['받는사람 이름',	'받는사람 전화번호',	'받는사람 전화번호2',	'받는사람 주소',	'받는사람 상세주소',	
                        '상품 이름',	'옵션 이름',	'상품 수량',	'배송메시지',	'주문일시',	'주문번호']
    if len(df) == 0:
        return False
    
    df.to_excel('downloaded_files/togle.xlsx', index=False) 

    order_list = []
    for i, row in df.iterrows():
        order_no = row['주문번호']
        order_date = row['주문일시']
        name = row['받는사람 이름']
        tel = row['받는사람 전화번호']
        address = row['받는사람 주소'] + str(row['받는사람 상세주소'])
        prd = row['상품 이름']
        opt = row['옵션 이름']
        orderq = int(row['상품 수량'])
        msg = row['배송메시지']
        prd_key = order_no + opt
        order_list.append((order_no, order_date, name, tel, address, prd, opt, orderq, msg, prd_key))
        
    from db import conn_db
    if len(order_list) > 0:
        conn = conn_db()
        cursor = conn.cursor()
        cursor.executemany("""
                                INSERT OR IGNORE 
                                INTO cafe23_order 
                                (order_no, order_date, name, tel, address, prd, opt, orderq, msg, prd_key) 
                                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """, order_list)
        conn.commit()
    return True
    



