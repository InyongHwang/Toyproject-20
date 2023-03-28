import hashlib
from flask import Flask, render_template, request, jsonify, redirect, url_for
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.oduyak2.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/members/signup', methods=["GET"])
def signup_get():
    return render_template('signup.html')

@app.route('/members/signup', methods=["POST"])
def signup_post():
    email_receive = request.form['email_give']
    nickname_receive = request.form['nickname_give']
    password_receive = request.form['password_give']
    bloglink_receive = request.form['bloglink_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    
    doc = {
        'email': email_receive,
        'nickname': nickname_receive,
        'password': pw_hash,
        'bloglink': bloglink_receive
    }
    
    db.users.insert_one(doc)

    return jsonify({'result':True})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)