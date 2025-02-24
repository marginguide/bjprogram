import requests, base64
import flask
import sqlite3
from datetime import datetime
import pandas as pd
mallid = "muscleguards"



def token_generate_process(AUTH_CODE):
    # 카페24 스토어 정보
    STORE_ID = "muscleguards"  # 예: "myshop"
    CLIENT_ID = "RpSFomfvaaBVrA18fVDLMA"
    CLIENT_SECRET = "kwEwgm66GRKjADaqrbDpgA"
    REDIRECT_URI = "https://muscleguards.cafe24api.com/artfinger/magazine.html"

    # Base64 인코딩 (client_id:client_secret)
    auth_header = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()

    # API 엔드포인트
    url = f"https://{STORE_ID}.cafe24api.com/api/v2/oauth/token"

    # 요청 헤더
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # 요청 데이터 (POST Body)
    data = {
        "grant_type": "authorization_code",
        "code": AUTH_CODE,
        "redirect_uri": REDIRECT_URI
    }

    # API 요청
    response = requests.post(url, headers=headers, data=data)
    token_data = response.json()

    # 토큰 정보 저장
    access_token = token_data.get("access_token")
    access_token_expireAt = token_data.get("expires_at")
    access_token_expireAt = access_token_expireAt.replace('T', ' ')
    access_token_expireAt = access_token_expireAt[:19]
    input_access = save_token('access', access_token, access_token_expireAt)
    if input_access == False:
        pass
    refresh_token = token_data.get("refresh_token")
    refresh_token_expireAt = token_data.get("refresh_token_expires_at")
    refresh_token_expireAt = refresh_token_expireAt.replace('T', ' ')
    refresh_token_expireAt = refresh_token_expireAt[:19]
    input_refresh= save_token('refresh', refresh_token, refresh_token_expireAt)
    


def save_token(tokenType,  tokenValue, expiresAt):
    # try:
        conn = sqlite3.connect('data/db.db')
        cursor = conn.cursor()
        query = f"""
                    INSERT INTO  token 
                            (tokenType, tokenValue, expiresAt) 
                    VALUES ('{tokenType}', '{tokenValue}', '{expiresAt}') 
                    ON CONFLICT DO UPDATE SET 
                    tokenValue = '{tokenValue}', expiresAt = '{expiresAt}'
                """
        cursor.execute(query)
        conn.commit()
        return True
    # except:
    #     return False


def get_access():
    now = datetime.now()
    str_now = datetime.strftime(now, "%Y-%m-%d %H:%M:%S")
    
    # 액세스 토큰 만료시간 가져오기
    conn = sqlite3.connect('data/db.db')
    query = "SELECT expiresAt,  tokenValue FROM token WHERE tokenType = 'access'"
    df = pd.read_sql_query(query, conn)
    access_token_expire = df['expiresAt'][0]
    
    # 지금 시간과 비교
    if str_now >= access_token_expire:
        pass
        # 리프레시 토큰을 이용하여 새로운 액세스 토큰을 받아서 저장하는 프로시져]
    else:
        access_token = df['tokenValue'][0]
        
        
# get_access()

str = 'abcd'
print(str[0])