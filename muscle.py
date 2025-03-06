# pyinstaller -w --uac-admin --add-data "templates;templates" --add-data "static;static" --contents-directory "." --noconfirm muscle.py

from flask import Flask, render_template, request, url_for, redirect
import threading
import webview
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__, static_folder='./static', template_folder='./templates')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def home():
    pass
    return render_template('index.html')
    
@app.route('/ordering')
def ordering():
    from selenium_read_order import order_process
    order_cnt = order_process()
    complete_at = datetime.strftime(datetime.now(), "%H:%M:%S")
    return render_template('result.html', 
                           complete_at = complete_at,
                           order_cnt = order_cnt)



# scheduler = BackgroundScheduler()

# # 매일 오후 3시 30분에 실행 (24시간 형식)
# scheduler.add_job(ordering, 'cron', hour=19, minute=42)



# scheduler.start()



def start_server():
    app.run(host='0.0.0.0', port=5000)   

if __name__ == '__main__':
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()
    webview.create_window('BJ- ORDER', url="http://localhost:5000/", min_size=(1600, 1000), text_select=True, )
    webview.start()
