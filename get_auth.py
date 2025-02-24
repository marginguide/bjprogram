import requests, base64
import flask
mallid = "muscleguards"

# 카페24 개발자 센터에서 발급받은 Client ID & Secret
client_id = "RpSFomfvaaBVrA18fVDLMA"
redirect_uri = "https://muscleguards.co.kr/board/free/list.html"
state = "muscle"
scope = "mall.write_order, mall.read_order,mall.read_shipping, mall.write_shipping"
# OAuth 2.0 토큰 발급 URL
url = f"https://{mallid}.cafe24api.com/api/v2/oauth/authorize?response_type=code&client_id={client_id}&state={state}&redirect_uri={redirect_uri}&scope={scope}"
print(url)

def get_acceess():
    # 카페24 스토어 정보
    STORE_ID = "muscleguards"  # 예: "myshop"
    CLIENT_ID = "RpSFomfvaaBVrA18fVDLMA"
    CLIENT_SECRET = "kwEwgm66GRKjADaqrbDpgA"
    AUTH_CODE = "dt9BX5UvJpfNP4Kn6ND9BF"
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
    ACCESS_TOKEN = token_data.get("access_token")
    REFRESH_TOKEN = token_data.get("refresh_token")

    print("Access Token:", ACCESS_TOKEN)
    print("Refresh Token:", REFRESH_TOKEN)
    
get_acceess()