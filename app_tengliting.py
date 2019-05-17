from flask import Flask,jsonify,request
from flask_jwt_extended import JWTManager,create_access_token
#from flask_cors import *#导入模块


class User(object):
    def __init__(self,username,password):
        self.username = username
        self.password = password
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

#CORS(app,suports_credentials=True)  #设置跨域
if __name__ == '__main__':
    app.run(debug=True,port=5000)


users = {}
@app.route('/signup13',methods=['POST'])
def signup13():
    if not request.is_json:
        return jsonify({"msg","错误请求不是json!"}),400
    username = request.json.get('username',None)
    password = request.json.get('password',None)
    if not username:
        return jsonify({"msg","不是用户！"}),400
    if not password:
        return jsonify({"msg","密码错误  ✌耶"}),400
    if username in users:
        return jsonify({"msg","用户已注册  ✌耶"}),400
    users[username] = User(username,password)
    return jsonify({"msg","注册成功  ✌耶"}),200

@app.route('/login13',methods=['POST'])
def login13():
    if not request.is_json:
        return jsonify({"msg", "错误请求不是json!"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if (not username) or (not password):
        return jsonify({"msg","不是用户 或 密码错误"}),400
    if username in users:
        return jsonify({"msg","用户已注册  haha"}),200
    loginuser = users.get(username,None)
    if not loginuser:
        return jsonify({"msg","用户不存在"}),401
    elif loginuser.password == password:
        return jsonify(access_token=create_access_token(identity=username)),200
    else:
        return jsonify({"msg","Password is incorrect!"}),401
    if loginuser and loginuser.password==password:
        return jsonify(access_token=create_access_token(identity=username)), 200
    else:
        return jsonify({"msg":"Username or password is not correct!"}), 401



import teng13.ting13 as ting13
app.register_blueprint(ting13.apk)



if __name__ == "__main__":
    app.run()