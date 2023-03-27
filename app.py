from flask import Flask, render_template, request, jsonify, redirect, url_for
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.oduyak2.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/members/signup_page', methods=["GET"])
def signup_page():
    return render_template('signup.html')

@app.route('/members/signup', methods=["POST"])
def signup():
    email_receive = request.form['email_give']
    ninkname_receive = request.form['ninkname_give']
    password_receive = request.form['password_give']
    bloglink_receive = request.form['bloglink_give']
    print(email_receive, ninkname_receive, password_receive, bloglink_receive)
    return redirect("http://localhost:5000/")

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)