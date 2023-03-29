# 1-1. /projects/<post_id> GET - html파일 렌더링
# 1-2. /projects/show/<post_id> GET - 렌더링 된 페이지에 특정 게시글 내용 보여주기
# 2. /projects/remove DELETE

from flask import Blueprint, render_template, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

# 팀 mongodb : mongodb+srv://sparta:test@cluster0.oduyak2.mongodb.net/?retryWrites=true&w=majority
# my mongodb : mongodb+srv://sparta:test@cluster0.qr5m03o.mongodb.net/?retryWrites=true&w=majority
# 재형 mongodb : mongodb://sparta:test@ac-xuujf6q-shard-00-00.coyzpl6.mongodb.net:27017,ac-xuujf6q-shard-00-01.coyzpl6.mongodb.net:27017,ac-xuujf6q-shard-00-02.coyzpl6.mongodb.net:27017/?ssl=true&replicaSet=atlas-lrxmt3-shard-0&authSource=admin&retryWrites=true&w=majority
client = MongoClient('mongodb+srv://sparta:test@cluster0.qr5m03o.mongodb.net/?retryWrites=true&w=majority')
db = client.dbtoyproject

bp = Blueprint('detali', __name__, url_prefix='/projects')

@bp.route('/main')
def main_home():
    return '임시 메인 페이지입니다'

# 1-1
@bp.route('/<post_id>')
def detail_home(post_id):
    return render_template('detail.html')

# 1-2
@bp.route('/show/<post_id>')
def get_project(post_id):
    try:
        project = db.project.find_one({'_id':ObjectId(post_id)})
        member_email = project['member_email']
        title = project['title']
        content = project['content']

        return jsonify({'success':True, 'member_email':member_email, 'title':title, 'content':content})
    except:
        return jsonify({'success':False, 'msg':'없는 게시글 입니다.'})
    
# 2
@bp.route('/remove', methods=["DELETE"])
def delete_project():
    json_data = request.get_json()
    post_id = json_data['post_id'] 
    db.project.delete_one({'_id':ObjectId(post_id)})

    return jsonify({'msg':'삭제 완료'})