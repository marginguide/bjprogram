from flask import Flask, render_template, request, url_for
import threading
import webview
app = Flask(__name__, static_folder='./static', template_folder='./templates')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/get_auth', methods=["GET", "POST"])
def get_auth():
    if request.method == "GET":
        return render_template('get_auth.html')
    else:
        from auth import create_url
        url = create_url()
        return url
    
def start_server():
    app.run(host='0.0.0.0', port=8000)   

if __name__ == '__main__':
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()
    webview.create_window('BJ- ORDER', url="http://localhost:8000/", min_size=(1600, 1000), text_select=True, )
    webview.start()
