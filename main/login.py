from flask import Blueprint, render_template, jsonify, request, session, redirect, url_for
from pymongo import MongoClient
import jwt
import datetime
import hashlib

client = MongoClient('mongodb+srv://sparta:test@cluster0.qr5m03o.mongodb.net/?retryWrites=true&w=majority')
db = client.dbtoyproject

bp = Blueprint('login', __name__, url_prefix='/')
SECRET_KEY = '20T'



@bp.route('/') 
def before_login():
    return render_template('before_login.html')

@bp.route('/main')
def after_login():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"email": payload['email']})
        return render_template('after_login.html', nickname=user_info["nickname"])
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))

@bp.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)

@bp.route('/signup')
def signup():
    return render_template('signup.html')

@bp.route('/project/open')
def open_project():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"email": payload['email']})
        return render_template('open_project.html', email=user_info["email"])
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))

#######
# API #
#######
@bp.route('/api/signup', methods=['POST'])
def api_signup():
    json_data = request.get_json()
    email_receive = json_data['email_give']
    nickname_receive = json_data['nickname_give']
    password_receive = json_data['password_give']
    bloglink_receive = json_data['bloglink_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()

    doc = {
        'email': email_receive,
        'nickname': nickname_receive,
        'password': pw_hash,
        'bloglink': bloglink_receive
    }

    db.users.insert_one(doc)

    return jsonify({'result': True})

@bp.route('/api/login', methods=['POST'])
def api_login():
    email_receive = request.form['email_give']
    password_receive = request.form['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()

    result = db.users.find_one({'email': email_receive, 'password': pw_hash})

    if result is not None:
        payload = {
            'email': email_receive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=300)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jsonify({'result': 'success', 'token': token})
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})

# @app.route('/projects/host')
# def myopen():
#     token_receive = request.cookies.get('mytoken')

#     try:
#         payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
#         open_projects = list(db.project.find({"email": payload['email']},{'_id':False}))
#         ids = db.project.find({}).distinct('_id')
#         for i, open_project in enumerate(open_projects):
#             open_project['id'] = str(ids[i])
#         return jsonify({'result': 'success', 'open_projects': open_projects})
#     except jwt.ExpiredSignatureError:
#         return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
#     except jwt.exceptions.DecodeError:
#         return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})