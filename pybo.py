from flask import Flask

app=Flask(__name__)

@app.route('/')      # 주소뒤에 아무것도 없는('/') 녀석이 들어오는 통로
def hello_pybo():
    return 'Hello, Pybo!'