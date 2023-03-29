# 5. /projects/join/in - 특정 프로젝트 참여 신청
# 6-1. /projects/join - 신청한 프로젝트 페이지 렌더링
# 6-2. /projects/join/view - 내(로그인 한 사람)가 신청한 프로젝트 데이터 가져오기
# 6-3. /projects/join/out - 프로젝트 신청 취소하기
# /projects/open - 내가 모집한 프로젝트 목록 조회
# /projects/open/<게시글id> - 내가 모집한 프로젝트에 신청한 사람 조회
# /projects/open/<게시글id>/accept - 프로젝트 참여 승인
# /projects/open/<게시글id>/reject - 프로젝트 참여 거절

from flask import Blueprint, render_template, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

# 팀 mongodb : mongodb+srv://sparta:test@cluster0.oduyak2.mongodb.net/?retryWrites=true&w=majority
client = MongoClient('mongodb+srv://sparta:test@cluster0.qr5m03o.mongodb.net/?retryWrites=true&w=majority')
db = client.dbtoyproject

bp = Blueprint('open', __name__, url_prefix='/projects/open')
    
@bp.route('/')
def open_home():
     return render_template('open.html')

@bp.route('/view', methods=['POST'])
def show_opening_projects():
    json_data = request.get_json()
    member_email = json_data['member_email']
    projects = list(db.project.find({'member_email':member_email}))

    opening_projects = []
    for project in projects:
        title = project['title']
        open_project_id = str(project['_id'])
        
        doc = {'open_project_id':open_project_id, 'title':title}
        opening_projects.append(doc)
    return jsonify({'result':opening_projects})

@bp.route('/volunteer', methods=['POST'])
def show_volunteer():
    json_data = request.get_json()
    open_project_id = json_data['open_project_id']
    volunteers = list(db.join.find({'post_id':open_project_id}))

    title = db.project.find_one({'_id':ObjectId(open_project_id)}, {"title"})['title']
    
    vlts = []
    for volunteer in volunteers:
        member_email = volunteer['member_email']
        vol_id = str(volunteer['_id'])

        doc = {'volunteer_id':vol_id, 'member_email':member_email}
        vlts.append(doc)
    return jsonify({'result':vlts, 'title':title})

@bp.route('/volunteer/accept', methods=['POST'])
def vol_accept():
    json_data = request.get_json()
    volunteer_id = json_data['volunteer_id']
    # db.join.delete_one({'_id':ObjectId(volunteer_id)})
    return jsonify({'msg':"승인되었습니다."})

@bp.route('/volunteer/reject', methods=['POST'])
def vol_reject():
    json_data = request.get_json()
    volunteer_id = json_data['volunteer_id']
    # db.join.delete_one({'_id':ObjectId(volunteer_id)})
    return jsonify({'msg':"거절되었습니다."})