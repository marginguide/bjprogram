from flask import Flask, render_template, request
import threading
import webview
app = Flask(__name__, static_folder='./static', template_folder='./templates')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def home():
    return render_template('index.html')
    
    
    
def start_server():
    app.run(host='0.0.0.0', port=5000)   

if __name__ == '__main__':
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()
    webview.create_window('BJ- ORDER', url="http://localhost:5000/", min_size=(1600, 1000), text_select=True, )
    webview.start()
