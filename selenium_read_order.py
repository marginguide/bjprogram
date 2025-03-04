
from seleniumbase import SB
import time, requests, os, glob
from pravate_info  import admin_info
from urllib.parse import urlparse, parse_qs
from config import ID, PASSWORD, togle_ID, togle_PASS
from bs4 import BeautifulSoup

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



def wait_for_csv(keyword="muscleguards", timeout= 30):
    basedir = os.path.abspath(os.path.dirname(__file__))
    folder = os.path.join(basedir, "downloaded_files")
    start_time = time.time()  # 시작 시간 기록

    while time.time() - start_time < timeout:
        # 🔹 특정 키워드가 포함된 CSV 파일 찾기
        matching_files = glob.glob(os.path.join(folder, f"*{keyword}*.*"))

        if matching_files:
            return matching_files[0]  # 첫 번째 발견된 파일 반환

        time.sleep(1)  # 🔹 1초 대기 후 다시 검색

    print("⏳ 30초 동안 파일을 찾지 못했습니다.")
    return None  # 시간 초과 시 None 반환


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
    

    def excel_down_click():
        with SB(headless2=False, uc=True, uc_cdp=False ,block_images=False, undetectable=True, ) as self:
            url = "https://eclogin.cafe24.com/Shop/"
            self.open(url)
            xpath = "//input[@id='mall_id']"
            self.assert_element(xpath, timeout=10)
            self.type(xpath, ID)
            
            xpath = "//input[@id='userpasswd']"
            self.type(xpath, PASSWORD)
            xpath = "//button[text()='로그인']"
            self.slow_click(xpath)
            
            xpath = "//a[@id='iptBtnEm']"
            self.slow_click(xpath)
            time.sleep(1)
            
           
            
            url = "https://muscleguards.cafe24.com/admin/php/shop1/s_new/shipped_begin_list.php"
            self.open(url)
            
            xpath = "//a[@id='eExcelDownloadBtn']"
            self.click(xpath)



            self.switch_to_window(1)

                    

            xpath = "//select[@id='aManagesList']"
            self.select_option_by_text(xpath, '자동화용데이터')
            # 엑셀 파일요청 클릭
            
            xpath = "//span[text() = '엑셀파일요청']/parent::a"
            self.click(xpath)
            
        
    def excel_download():



        with SB(headless2=False, uc=True, uc_cdp=False ,block_images=False, undetectable=True, ) as self:
            url = "https://eclogin.cafe24.com/Shop/"
            self.open(url)
            xpath = "//input[@id='mall_id']"
            self.assert_element(xpath, timeout=10)
            self.type(xpath, ID)
            
            xpath = "//input[@id='userpasswd']"
            self.type(xpath, PASSWORD)
            xpath = "//button[text()='로그인']"
            self.slow_click(xpath)
            
            xpath = "//a[@id='iptBtnEm']"
            self.slow_click(xpath)
            time.sleep(1)
            
            url = "https://muscleguards.cafe24.com/admin/php/Excel/ExcelCreateDownloadPopup.php?menu_no=72"
            self.open(url)
            time.sleep(1)
                    

            xpath = "//tbody[@class='center']/tr[1]//a"
            self.click(xpath)
            # 엑셀 파일요청 클릭
            time.sleep(2)
            target_file = "muscleguards"
            excel = wait_for_csv(target_file, 30)
            pass
            from data_manage import modif_column_name
            if modif_column_name(excel):
                excel = wait_for_csv(keyword="togle", timeout= 30)
             # 토글이동
            url = "https://togle.io/app/login"
            self.open(url)
            
            xpath = "//input[@placeholder ='아이디(Email)']"
            self.assert_element(xpath, timeout=10)
            self.type(xpath, togle_ID)
            xpath = "//input[@placeholder ='비밀번호']"
            self.type(xpath, togle_PASS)
            xpath = "//span[text()= '로그인']//ancestor::button"
            self.click(xpath)
            time.sleep(3)
            url = "https://togle.io/app/orders/process/notPrinted"
            self.open(url)
            
            xpath = "//span[text()= '신규주문 엑셀 업로드']//ancestor::button"
            self.assert_element(xpath, timeout=10)
            self.click(xpath)
            time.sleep(1)
            xpath = "//div[@class='q-card']//div[text()= '쇼핑몰 선택']//ancestor::label"
            self.assert_element(xpath, timeout=10)
            time.sleep(1)
            self.click(xpath)
            
            
            xpath = "//div[@class='ellipsis' and contains(text(), '머슬가드')]/parent::div/parent::div"
            self.assert_element(xpath, timeout=10)
            self.click(xpath)
            
            xpath = "//input[contains(@class, 'q-uploader__input')]//ancestor::a"
            self.assert_element(xpath, timeout=10)
            self.click(xpath)
            time.sleep(3)
            import pyautogui
            pyautogui.typewrite(excel)  # 파일 경로 입력
            pyautogui.press("enter")

            xpath = "//span[text()='확인']//ancestor::button"
            self.assert_element(xpath, timeout=10)
            self.click(xpath)
            
            xpath = "//span[text()='일괄 송장출력']//ancestor::button"
            self.assert_element(xpath, timeout=10)
            self.click(xpath)
            
            xpath = "//span[text()='확인']//ancestor::button"
            self.click(xpath)
            pass
            
            # 프린트 아이콘 버튼
            xpath = "//button[@id='print-confirm']"
            
            self.click(xpath)
            
            
            # 송장번호 엑셀 받기
            
            xpath = "//div[contains(text(),'엑셀 다운로드')]//ancestor::button"
            self.click(xpath)
            
            xpath = "//span[text()='발송정보 다운로드']//ancestor::button"
            self.click(xpath)
            
            xpath = "//div[@class='q-card']//div[contains(text(),'샐릿34 (ncp_1oegid_01)')]//ancestor::div[contains(@class,'row ')]//div[@role='checkbox']//input"
            self.click(xpath)
            xpath = "//span[text()='확인']//ancestor::button"
            self.click(xpath)
            pyautogui.click(x=500, y=600)
            
            # 결과 테이블 DIV
            xpath = "//div[@class='ag-center-cols-container']/div"
            return 'auth_code'
    

    # try:excel_down_click()
    # except:pass
    try:excel_download()
    except:pass
    # self.

    tab_list = self.driver.window_handles()
    self.execute_script("window.alert = function() {}; window.confirm = function() { return true; };")
    self.open_new_tab()

    self.refresh_page()
    # self.switch_to_alert()

    # self.accept_alert()
    pass
    # self.click(xpath)
    

    # # 다운로드 버튼 클릭
    # xpath = "//a[@id='eShipBeginExcelDownload']"
    # self.click(xpath)
    # self.switch_to_alert()
    # self.accept_alert()
    
    
    # # 파일 패스 찾기
    # response = requests.get("https://api64.ipify.org?format=json")
    # external_ip = response.json()["ip"]
    # target_file = f"{external_ip}_orders.csv"
    # excel_file = get_file_path(target_file, 20)
    # print(excel_file)
    
    # 주문을 읽어서 DB로
    
    
    

    
read_order()

#data-testid