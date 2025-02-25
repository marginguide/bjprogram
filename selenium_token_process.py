
from seleniumbase import SB
import time
from pravate_info  import admin_info
from urllib.parse import urlparse, parse_qs

def token_auto(url):
    try:
        admin_inform_ = admin_info()
        id = admin_inform_.get('admin_id')
        pw = admin_inform_.get('admin_pass')
        # 셀레니움
        with SB(headless2=True, uc=False, uc_cdp=False , uc_subprocess=True, log_cdp=True, remote_debug=True, block_images=False) as self:
            self.open(url)
            xpath = "//input[@id='mall_id']"
            self.type(xpath, id)
            xpath = "//input[@id='userpasswd']"
            self.type(xpath, pw)
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
        
        
