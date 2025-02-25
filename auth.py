import requests, base64
import flask
import sqlite3
from datetime import datetime
import pandas as pd
from seleniumbase import SB
mall_id = "muscleguards"
store_ID = "muscleguards"  # 예: "myshop"
client_id = "RpSFomfvaaBVrA18fVDLMA"
client_secret = "kwEwgm66GRKjADaqrbDpgA"


def create_url():
    mallid = "muscleguards"
    # 카페24 개발자 센터에서 발급받은 Client ID & Secret
    client_id = "RpSFomfvaaBVrA18fVDLMA"
    redirect_uri = "https://muscleguards.co.kr/board/free/list.html"
    state = "muscle"
    scope = "mall.write_order, mall.read_order,mall.read_shipping, mall.write_shipping"
    # OAuth 2.0 토큰 발급 URL
    url = f"https://{mallid}.cafe24api.com/api/v2/oauth/authorize?response_type=code&client_id={client_id}&state={state}&redirect_uri={redirect_uri}&scope={scope}"
    print(url)
    return url

def save_token(tokenType,  tokenValue, expiresAt):
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


def generate_token(type, code):
    redirect_uri = "https://muscleguards.cafe24api.com/artfinger/magazine.html"
    # 요청 헤더
    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    # 엔드포인트 URL
    url = f"https://{store_ID}.cafe24api.com/api/v2/oauth/token"
    
    if type == "auth_code":
        payload = {
                "grant_type" : "authorization_code",
                "code" : code,
                "redirect_uri" : redirect_uri
            }
    else:
        payload = {
                "grant_type":"refresh_token",
                "refresh_token":code
            }
    # API 요청
    response = requests.request("POST", url, data=payload, headers=headers)
    token_data = response.json()

    # 토큰 정보 저장
    access_token = token_data.get("access_token")
    access_token_expireAt = token_data.get("expires_at")
    access_token_expireAt = access_token_expireAt.replace('T', ' ')
    access_token_expireAt = access_token_expireAt[:19]
    input_access = save_token('access', access_token, access_token_expireAt)
    refresh_token = token_data.get("refresh_token")
    refresh_token_expireAt = token_data.get("refresh_token_expires_at")
    refresh_token_expireAt = refresh_token_expireAt.replace('T', ' ')
    refresh_token_expireAt = refresh_token_expireAt[:19]
    input_refresh= save_token('refresh', refresh_token, refresh_token_expireAt)
    return access_token





def get_access():
    now = datetime.now()
    str_now = datetime.strftime(now, "%Y-%m-%d %H:%M:%S")
    
    # 액세스 토큰 만료시간 가져오기
    conn = sqlite3.connect('data/db.db')
    query = "SELECT tokenType, expiresAt,  tokenValue FROM token"
    df = pd.read_sql_query(query, conn)
    dict_expires = df.set_index("tokenType")["expiresAt"].to_dict()
    dict_token_value = df.set_index("tokenType")["tokenValue"].to_dict()
    conn.close()
    access_token_expire = dict_expires.get('access')
    access_token = dict_token_value.get('access')
    
    
    # 지금 시간과 비교
    if str_now > access_token_expire:
        refresh_token = dict_token_value.get('refresh')
        refresh_token_expire  = dict_expires.get('refresh')
        if str_now >= refresh_token_expire:
            url = create_url()
            from selenium_token_process import token_auto
            auth_code = token_auto(url)
            if auth_code:
                access_token = generate_token('auth_code', auth_code)
        access_token = generate_token('refresh_token', refresh_token)

    else:
        pass
        
        


get_access()