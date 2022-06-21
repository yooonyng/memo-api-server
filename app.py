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
from config import Config
from resource.user import UserRegisterResource

app = Flask(__name__)

app.config.from_object(Config)
jwt = JWTManager(app)
api = Api(app)

# 경로와 리소스를 연결한다.
api.add_resource(UserRegisterResource, '/users/register')


if __name__ == '__main__':
    app.run()

