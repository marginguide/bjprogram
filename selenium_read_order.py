
from seleniumbase import SB
import time, os, glob
from config import ID, PASSWORD, togle_ID, togle_PASS
from bs4 import BeautifulSoup
import pyautogui
import random
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

def pyautogui_image_click(btn_name):
    
    
    cnt = 0
    while True:
        try:
            
            if btn_name == "confirm":
                try:
                    btn_path = 'static/pyauto_img/confirm_button_1.png'
                    btn_img = pyautogui.locateCenterOnScreen(btn_path)
                except:
                    btn_path = 'static/pyauto_img/confirm_button_2.png'
                    btn_img = pyautogui.locateCenterOnScreen(btn_path)
            else:
                btn_path = 'static/pyauto_img/' + btn_name + '.png'
                btn_img = pyautogui.locateCenterOnScreen(btn_path)
            pyautogui.click(btn_img)
            return True
        except:
            cnt += 1
            time.sleep(0.5)
        if cnt > 60: return False


def order_process():

    
    # return 105
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
        time.sleep(1)
        if self.is_element_visible(xpath):
            self.slow_click(xpath)
            time.sleep(1)

        
        
        
        url = "https://muscleguards.cafe24.com/admin/php/shop1/s_new/shipped_begin_list.php"
        self.open(url)
        
        xpath = "//a[@id='eExcelDownloadBtn']"
        self.slow_click(xpath)
        
        self.switch_to_window(1)
        xpath = "//select[@id='aManagesList']"
        self.select_option_by_text(xpath, '자동화용데이터')
        # 엑셀 파일요청 클릭

        if not pyautogui_image_click('generate_btn'):return False
        if not pyautogui_image_click('confirm'):return False

        
        # 
        xpath = "//tbody[@class='center']/tr[1]//a"
        for i in range(30):
            if self.is_element_clickable(xpath):
                break
            time.sleep(1)
        self.slow_click(xpath)
        
        target_file = "muscleguards"
        excel = wait_for_csv(target_file, 30)
        pass
        from data_manage import modif_column_name
        if modif_column_name(excel):
            excel = wait_for_csv(keyword="togle", timeout= 30)
        else:
            return "주문이 없습니다."
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
        self.slow_click(xpath)
        time.sleep(3)

        url = "https://togle.io/app/orders/process/notPrinted"
        self.open(url)
        
        xpath = "//span[text()= '신규주문 엑셀 업로드']//ancestor::button"
        self.assert_element(xpath, timeout=10)
        self.slow_click(xpath)
        time.sleep(1)
        xpath = "//div[@class='q-card']//div[text()= '쇼핑몰 선택']//ancestor::label"
        self.assert_element(xpath, timeout=10)
        time.sleep(1)
        self.slow_click(xpath)
        
        
        xpath = "//div[@class='ellipsis' and contains(text(), '머슬가드')]/parent::div/parent::div"
        self.assert_element(xpath, timeout=10)
        self.slow_click(xpath)
        
        xpath = "//input[contains(@class, 'q-uploader__input')]//ancestor::a"
        self.assert_element(xpath, timeout=10)
        self.slow_click(xpath)
        time.sleep(2)
        pyautogui.typewrite(excel)  # 파일 경로 입력
        pyautogui.press("enter")

        xpath = "//span[text()='확인']//ancestor::button"
        self.assert_element(xpath, timeout=10)
        self.slow_click(xpath)
        
        
        
        
        def assert_tracking():
            xpath = "//span[text()='일괄 송장출력']//ancestor::button"
            self.assert_element(xpath, timeout=10)
            time.sleep(10)
            self.slow_click(xpath)
            
            xpath = "//span[text()='확인']//ancestor::button"
            self.slow_click(xpath)
            pass
           
            
            if not pyautogui_image_click('blank_screen_click'):return False
            pyautogui.hotkey('ctrl', 'p')
            if not pyautogui_image_click('select_printer'):return False
            if not pyautogui_image_click('more_view'):return False
            if not pyautogui_image_click('x_printer'):return False
            if not pyautogui_image_click('do_print'):return False
            
            self.open_new_tab()
            url = "https://www.togle.io/app/orders/process/notPrinted"
            self.open(url)
            try:
                xpath = "//input[@placeholder ='아이디(Email)']"
                self.assert_element(xpath, timeout=10)
                self.type(xpath, togle_ID)
                xpath = "//input[@placeholder ='비밀번호']"
                self.type(xpath, togle_PASS)
                xpath = "//span[text()= '로그인']//ancestor::button"
                self.slow_click(xpath)
            except:
                pass
            time.sleep(3)
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
                
                order_no =item.find("div", attrs={"aria-colindex": "6"}).get_text(strip=True) 
                if prev_order_no == order_no:continue
                prev_order_no = order_no
                
                if "파일업로드" in item.get_text():
                    try:
                        tracking_no = item.find("div", attrs={"aria-colindex": "9"}).select_one("span > div > div").get_text(strip=True)
                        Num = {}
                        Num['order_no'] = order_no
                        Num['tracking_no'] = tracking_no
                    # 송장번호가 없을 경우
                    except:
                        return False
                    tracking_list.append(Num)
            return tracking_list
            
        tracking_list = assert_tracking()
        if tracking_list == False:
            tracking_list = assert_tracking()
            if tracking_list == False:
                return "오류발생했어요. 니가 알아서 해봐요."
        
        print(tracking_list)
        # url = "https://muscleguards.cafe24.com/admin/php/shop1/s_new/shipped_begin_list.php"
        # self.open(url)
        # time.sleep(1)
        self.switch_to_window(-1)
        
        for i in range(30):
            self.switch_to_tab(i)
            url = self.get_current_url()
            if url == "https://muscleguards.cafe24.com/admin/php/shop1/s_new/shipped_begin_list.php":break
            
        for order in tracking_list:
            order_no = order['order_no']
            tracking_no = order['tracking_no']
            xpath = f"//tbody[@order_id='{order_no}']//div[@class='gSingle']/input"
            if not self.is_element_present(xpath): continue
            self.type(xpath, tracking_no)
            xpath = f"//input[@data-row-key='{order_no}']"
            self.slow_click(xpath)
        self.scroll_to_top()
        if not pyautogui_image_click('onshipment_generate_btn'):return False
        if not pyautogui_image_click('confirm'):return False
        time.sleep(10)

        
        # time.sleep(1)
        # pyautogui.click(450,744)
        # time.sleep(1)
        # pyautogui.click(763, 245)
        pass
    
        return len(tracking_list)
    
order_process()