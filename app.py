# 기본 구조
# from flask import Flask
# from flask_jwt_extended import JWTManager
# from flask_restful import Api

# app = Flask(__name__)

# if __name__ == '__main__':
#     app.run()

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

app = Flask(__name__)

if __name__ == '__main__':
    app.run()

