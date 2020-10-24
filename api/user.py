from flask import Flask,jsonify,request
app=Flask(__name__)
app.config["JSON_AS_ASCII"] = False

# data=[
# {"id":1,"uesrname":"小明","password":"123456","role":0,"sex":0,"telephone":"10086","adress":"北京市海淀区"},
# {"id": 2, "username": "李华", "password": "abc", "role": 1, "sex": 0, "telephone": "10010", "address": "广州市天河区"},
# {"id": 3, "username": "大白", "password": "666666", "role": 0, "sex": 1, "telephone": "10000", "address": "深圳市南山区"}
# ]
#
# @app.route("/")
# def hello_world():
#     return 'hello_world'
#
# @app.route("/users",methods=['GET'])
# def get_all_users():
#     "获取所有用户信息"
#     return jsonify({"code":"0","msg":"操作成功","data":data})
#
# @app.route("/users/<int:user_id>",methods=['GET'])
# def get_user(user_id):
#     "获取某个用户信息"
#     if user_id > 0 and user_id <= len(data):
#         return jsonify({"code":"0","msg":"操作成功","data":data[user_id -1]})
#     return jsonify({"code":"1","msg":"用户不存在"})

@app.route("/register",methods=['POST'])
def user_register():
    username = request.json.get('username').strip()
    password = request.json.get('password').strip()
    sex = request.json.get('sex','0').strip()
    telephone = request.json.get('telephone','').strip()
    address = request.json.get('telephone','').strip()
    if username and password and telephone:
        import re
        if username=='wintest':
            return jsonify({'code':"2002","msg":"用户已存在"})
        elif not (sex=='0'or sex=='1'):
            return jsonify({'code':2003,'msg':'输入的性别只能是0（男）或1（女）'})
        elif not(len(telephone)==11 and re.match('^1[3,5,7,8]\d{9}$',telephone)):
            return jsonify({'code':2004,'msg':"手机号格式不正确"})
        else:
            return jsonify({'code':0,'msg':'恭喜，注册成功'})
    else:
        return jsonify({'code':2001,'msg':"用户名/密码/手机号不能为空，请查收！"})

@app.route('/login',methods=['POST'])
def user_login():
    username = request.values.get('username')
    password = request.values.get('password')
    if username and password:
        if username=='wintest' and password=='123456':
            return jsonify({"code":0,"msg":"恭喜，登录成功"})
        return jsonify({"code":1002,"msg":"用户名或密码错误"})
    else:
        return jsonify({'code':1001,'msg':"用户名或密码不能为空"})

if __name__ == '__main__':
    app.run()

