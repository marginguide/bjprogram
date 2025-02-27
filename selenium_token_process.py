
from seleniumbase import SB
import time
from pravate_info  import admin_info
from urllib.parse import urlparse, parse_qs
from config import ID, PASSWORD
def token_auto(url):
    try:
        # 셀레니움
        with SB(headless2=False, uc=True, uc_cdp=False ,block_images=False, undetectable=True) as self:
            self.open(url)
            xpath = "//input[@id='MALL_ID']"
            self.type(xpath, ID)
            xpath = "//input[@id='userpasswd']"
            self.type(xpath, PASSWORD)
            xpath = "//button[text()='로그인']"
            self.slow_click(xpath)
            
            xpath = "//a[@id='iptBtnEm']"
            self.slow_click(xpath)
            time.sleep(1)
            # URL 에서 코드 분리하기
            url = self.get_current_url()
            parsed_url = urlparse(url)
            query_params = parse_qs(parsed_url.query)
            auth_code = query_params['code'][0]
            
            return auth_code
    except:
        return False
        