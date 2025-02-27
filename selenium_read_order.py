
from seleniumbase import SB
import time, requests, os
from pravate_info  import admin_info
from urllib.parse import urlparse, parse_qs
from config import ID, PASSWORD
def get_file_path(target_file, timeout):
    start_time = time.time()  # 시작 시간 기록
    basedir = os.path.abspath(os.path.dirname(__file__))
    folder_path = os.path.join(basedir, "downloaded_files")
    while time.time() - start_time < timeout:  # 30초 동안 반복
        for root, dirs, files in os.walk(folder_path):
            if target_file in files:
                return os.path.join(root, target_file)  # 파일 경로 반환
        
        time.sleep(1)  # CPU 과부하 방지를 위해 1초 대기

    return False  # 
def excel_to_togle(excel_file):
    pass
    
def read_order():

    basedir = os.path.abspath(os.path.dirname(__file__))
    folder_path = os.path.join(basedir, "downloaded_files")
    
    # 다운로드 폴더 생성
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # 다운로드 폴더 비우기
    try :
        for root, _, files in os.walk(folder_path):
            for file in files:
                try:
                    os.remove(os.path.join(root, file))
                except OSError as e:
                    raise OSError(f"파일 삭제 실패: {e}") from e
    except Exception:
        pass
    url = "https://eclogin.cafe24.com/Shop/"
    try:
        # 셀레니움
        with SB(headless2=False, uc=True, uc_cdp=False ,block_images=False, undetectable=True) as self:
            self.open(url)
            xpath = "//input[@id='mall_id']"
            self.type(xpath, ID)
            xpath = "//input[@id='userpasswd']"
            self.type(xpath, PASSWORD)
            xpath = "//button[text()='로그인']"
            self.slow_click(xpath)
            
            xpath = "//a[@id='iptBtnEm']"
            self.slow_click(xpath)
            time.sleep(1)
            
            xpath = "//span[text()='배송준비중']/parent::div/following-sibling::div/a"
            # if self.get_text(xpath) == '0':
            #     return 'No Orders'
            
            self.click(xpath)
            

            # 다운로드 버튼 클릭
            xpath = "//a[@id='eShipBeginExcelDownload']"
            self.click(xpath)
            self.switch_to_alert()
            self.accept_alert()
            
            
            # 파일 패스 찾기
            response = requests.get("https://api64.ipify.org?format=json")
            external_ip = response.json()["ip"]
            target_file = f"{external_ip}_orders.csv"
            excel_file = get_file_path(target_file, 20)
            print(excel_file)
            
            
            # URL 에서 코드 분리하기
            # url = self.get_current_url()
            # parsed_url = urlparse(url)
            # query_params = parse_qs(parsed_url.query)
            # auth_code = query_params['code'][0]
            
            return 'auth_code'
    except:
        return False
        
read_order()

#data-testid