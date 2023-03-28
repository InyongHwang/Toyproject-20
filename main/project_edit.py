# 3-1. /projects/edit/<post_id> GET - html파일 렌더링
# 3-2. /projects/edit/show/<post_id> GET - 렌더링 된 페이지에 특정 게시글 내용 보여주기
# 4. /projects/edit PUT

from flask import Blueprint, render_template, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

# 팀 mongodb : mongodb+srv://sparta:test@cluster0.oduyak2.mongodb.net/?retryWrites=true&w=majority
client = MongoClient('mongodb+srv://sparta:test@cluster0.qr5m03o.mongodb.net/?retryWrites=true&w=majority')
db = client.dbtoyproject

bp = Blueprint('edit', __name__, url_prefix='/projects/edit')

@bp.route('/<post_id>')
def edit_home(post_id):
    return render_template('edit.html')

@bp.route('/show/<post_id>')
def get_edit(post_id):
    project = db.project.find_one({'_id':ObjectId(post_id)})
    title = project['title']
    content = project['content']

    return jsonify({'title':title, 'content':content})

@bp.route('/', methods=['PUT'])
def edit_project():
    json_data = request.get_json()
    post_id = json_data['post_id']
    title = json_data['title']
    content = json_data['content']
    # updated_at = datetime.today()
    db.project.update_one({'_id':ObjectId(post_id)}, {'$set':{'title':title, 'content':content}})
    return jsonify({'msg':'수정 완료'})