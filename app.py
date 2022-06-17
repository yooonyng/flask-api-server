# 기본적인 api 서버 구조
from flask import Flask

app = Flask(__name__)

# API가 있어야한다. 아래 코드가 API
@app.route('/',methods=['GET'])
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run()

