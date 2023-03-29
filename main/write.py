from flask import Blueprint, render_template, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('mongodb+srv://sparta:test@cluster0.qr5m03o.mongodb.net/?retryWrites=true&w=majority')
db = client.dbtoyproject

bp = Blueprint('write', __name__, url_prefix='/projects')

@bp.route('/main')
def home():
   return render_template('main.html')

@bp.route('/write')
def team_write():
    return render_template('write.html')



@bp.route("/write", methods=["POST"])
def write_post():
    json_data = request.get_json()
    member_email = json_data['member_email']
    title = json_data['title']
    content = json_data['content']

    doc = {
        'title':title,
        'content':content,
        'member_email':member_email
    }
    db.project.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})

@bp.route("/main/show", methods=["GET"])
def mwrite_get():
    all_projects = list(db.project.find({}))
    for project in all_projects:
        project['_id'] = str(project['_id'])

    return jsonify({'result': all_projects})