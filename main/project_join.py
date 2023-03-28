# 5. /projects/join/in - 특정 프로젝트 참여 신청
# 6-1. /projects/join - 신청한 프로젝트 페이지 렌더링
# 6-2. /projects/join/view - 내(로그인 한 사람)가 신청한 프로젝트 데이터 가져오기
# 6-3. /projects/join/out - 프로젝트 신청 취소하기

from flask import Blueprint, render_template, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

# 팀 mongodb : mongodb+srv://sparta:test@cluster0.oduyak2.mongodb.net/?retryWrites=true&w=majority
client = MongoClient('mongodb+srv://sparta:test@cluster0.qr5m03o.mongodb.net/?retryWrites=true&w=majority')
db = client.dbtoyproject

bp = Blueprint('join', __name__, url_prefix='/projects/join')

@bp.route('/in', methods=['POST'])
def join_project():
    json_data = request.get_json()
    member_email = json_data['member_email']
    post_id = json_data['post_id']
    pre_exist = list(db.join.find({'member_email':member_email, 'post_id':post_id}))
    
    if (len(pre_exist) > 0):
            return jsonify({'success':False, 'msg':'이미 신청한 프로젝트입니다.'})
    else:
        doc = {
            'member_email':member_email,
            'post_id':post_id
        }

        db.join.insert_one(doc)
        return jsonify({'success':True, 'msg':'신청 완료'})
    
@bp.route('/')
def join_home():
     return render_template('join.html')

@bp.route('/view', methods=['POST'])
def show_joining_projects():
    json_data = request.get_json()
    member_email = json_data['member_email']
    
    projects = list(db.join.find({'member_email':member_email}))

    joining_projects = []
    for project in projects:
        post_id = project['post_id']
        join_id = str(project['_id'])

        project = db.project.find_one({'_id':ObjectId(post_id)}, {'_id':False})
        
        li = {'join_id':join_id, 'post_id':post_id, 'title':project['title']}
        joining_projects.append(li)

    return jsonify({'result':joining_projects})

@bp.route('/out', methods=['DELETE'])
def cancle_applying():
    json_data = request.get_json()
    join_id = json_data['join_id']
    db.join.delete_one({'_id':ObjectId(join_id)})

    return jsonify({'msg':'취소 완료'})