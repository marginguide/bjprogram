
from seleniumbase import SB
import time, requests, os, glob
from pravate_info  import admin_info
from urllib.parse import urlparse, parse_qs
from config import ID, PASSWORD, togle_ID, togle_PASS
from bs4 import BeautifulSoup
import pyautogui
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
        
        time.sleep(1)
        # 오코 클릭
        pyautogui.click(665, 387)
        time.sleep(1)
        pyautogui.click(840, 224)
        time.sleep(1)
        
        xpath = "//tbody[@class='center']/tr[1]//a"
        self.click(xpath)
        
        target_file = "muscleguards"
        excel = wait_for_csv(target_file, 30)
        pass
        from data_manage import modif_column_name
        if modif_column_name(excel):
            excel = wait_for_csv(keyword="togle", timeout= 30)
            
        self.switch_to_window(0)
        self.open_new_tab()
        
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
        pyautogui.typewrite(excel)  # 파일 경로 입력
        pyautogui.press("enter")

        xpath = "//span[text()='확인']//ancestor::button"
        self.assert_element(xpath, timeout=10)
        self.click(xpath)
        
        
        
        
        
        xpath = "//span[text()='일괄 송장출력']//ancestor::button"
        self.assert_element(xpath, timeout=10)
        time.sleep(5)
        self.click(xpath)
        
        xpath = "//span[text()='확인']//ancestor::button"
        self.click(xpath)
        pass
        time.sleep(10)
        url = "https://togle.io/app/orders/process/notPrinted"
        self.open(url)
        pass
        
        # 결과 테이블의 rows
        for i in range(10):
            time.sleep(1)
            xpath = "//div[@class='ag-center-cols-container']/div"
            line_cnt = len(self.find_elements(xpath))
            if line_cnt > 0: break
        
        
        
        soup = BeautifulSoup(self.get_page_source(), "html.parser")
        items = soup.select("div.ag-center-cols-container > div")
        
        print(items)
        tracking_list = []
        prev_order_no = ''
        for index, item in enumerate(items, start=0):
            
            order_no =item.find("div", attrs={"col-id": "col6"}).get_text(strip=True) 
            if prev_order_no == order_no:continue
            prev_order_no = order_no
            tracking_no = item.find("div", attrs={"col-id": "col9"}).select_one("span > div > div").get_text(strip=True)
            
            Num = {}
            Num['order_no'] = order_no
            Num['tracking_no'] = tracking_no
            tracking_list.append(Num)
            
        
        
        print(tracking_list)
        url = "https://muscleguards.cafe24.com/admin/php/shop1/s_new/shipped_begin_list.php"
        self.open(url)
        time.sleep(1)
                
        for order in tracking_list:
            order_no = order['order_no']
            tracking_no = order['tracking_no']
            xpath = f"//tbody[@order_id='{order_no}']//div[@class='gSingle']/input"
            if not self.is_element_present(xpath): continue
            self.type(xpath, tracking_no)
            xpath = f"//input[@data-row-key='{order_no}']"
            self.slow_click(xpath)
        self.scroll_to_top()
        time.sleep(1)
        pyautogui.click(450,744)
        time.sleep(1)
        pyautogui.click(763, 245)
        pass
    

    
read_order()

#data-testid