
def get_first_token():
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
get_first_token()