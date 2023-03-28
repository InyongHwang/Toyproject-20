import hashlib
from datetime import datetime, timedelta
import jwt
from flask import Flask, render_template, request, jsonify, redirect, url_for
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.oduyak2.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

SECRET_KEY = '20T'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/members/signup', methods=["GET"])
def signup_get():
    return render_template('signup.html')

@app.route('/members/signup', methods=["POST"])
def signup_post():
    json_data = request.get_json()
    email_receive = json_data['email_give']
    nickname_receive = json_data['nickname_give']
    password_receive = json_data['password_give']
    bloglink_receive = json_data['bloglink_give']

    duplicate = db.users.find_one({'email':email_receive})
    if duplicate is not None:
        return jsonify({'result':False, 'msg':'중복된 이메일입니다.'})

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    
    doc = {
        'email': email_receive,
        'nickname': nickname_receive,
        'password': pw_hash,
        'bloglink': bloglink_receive
    }
    
    db.users.insert_one(doc)

    return jsonify({'result':True})

@app.route('/members/login', methods=["GET"])
def login_get():
    return render_template('login.html')

@app.route('/members/login', methods=["POST"])
def login_post():
    json_data = request.get_json()
    email_receive = json_data['email_give']
    password_receive = json_data['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()

    user_info = db.users.find_one({'email':email_receive, 'password': pw_hash})

    if user_info is not None:
        payload = {
            'email': email_receive
            # 'exp': datetime.utcnow() + timedelta(seconds=5)
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return jsonify({'result':True, 'token':token})
    else:
        return jsonify({'result':False, 'msg':'아이디/비밀번호가 일치하지 않습니다.'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)