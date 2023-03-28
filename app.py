from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId

# 팀 mongodb : mongodb+srv://sparta:test@cluster0.oduyak2.mongodb.net/?retryWrites=true&w=majority
client = MongoClient('mongodb+srv://sparta:test@cluster0.qr5m03o.mongodb.net/?retryWrites=true&w=majority')
db = client.dbtoyproject

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# 구현 해야 하는 API list
# 1-1. /projects/<post_id> GET - html파일 렌더링
# 1-2. /projects/show/<post_id> GET - 렌더링 된 페이지에 특정 게시글 내용 보여주기
# 2. /projects/remove DELETE
# 3-1. /projects/edit/<post_id> GET - html파일 렌더링
# 3-2. /projects/edit/show/<post_id> GET - 렌더링 된 페이지에 특정 게시글 내용 보여주기
# 4. /projects/edit PUT
# 5. /projects/join/in - 특정 프로젝트 참여 신청
# 6-1. /projects/join - 신청한 프로젝트 페이지 렌더링
# 6-2. /projects/join/view - 내(로그인 한 사람)가 신청한 프로젝트 데이터 가져오기
# 6-3. /projects/join/out - 프로젝트 신청 취소하기


# 0 - 임시 메인 페이지
@app.route('/projects/main')
def main_home():
    return '임시 메인 페이지입니다'

# 1-1
@app.route('/projects/<post_id>') 
def detail_home(post_id):
   return render_template('detail.html')

# 1-2
@app.route('/projects/show/<post_id>')
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
@app.route('/projects/remove', methods=["DELETE"])
def delete_project():
   json_data = request.get_json()
   post_id = json_data['post_id'] 
   db.project.delete_one({'_id':ObjectId(post_id)})

   return jsonify({'msg':'삭제 완료'})

# 3-1
@app.route('/projects/edit/<post_id>')
def edit_home(post_id):
    return render_template('edit.html')

# 3-2
@app.route('/projects/edit/show/<post_id>')
def get_edit(post_id):
    project = db.project.find_one({'_id':ObjectId(post_id)})
    title = project['title']
    content = project['content']

    return jsonify({'title':title, 'content':content})

# 4
@app.route('/projects/edit', methods=['PUT'])
def edit_project():
    json_data = request.get_json()
    post_id = json_data['post_id']
    title = json_data['title']
    content = json_data['content']
    updated_at = datetime.today()
    db.project.update_one({'_id':ObjectId(post_id)}, {'$set':{'title':title, 'content':content, 'updated_at':updated_at}})
    return jsonify({'msg':'수정 완료'})

# 5
@app.route('/projects/join/in', methods=['POST'])
    # 이미 존재하는 데이터에 대해서 예외처리 필요
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

# 6-1
@app.route('/projects/join')
def join_home():
    return render_template('join.html')

# 6-2
@app.route('/projects/join/view', methods=["POST"])
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

# 6-3
@app.route('/projects/join/out', methods=["DELETE"])
def cancle_applying():
    json_data = request.get_json()
    join_id = json_data['join_id']
    db.join.delete_one({'_id':ObjectId(join_id)})

    return jsonify({'msg':'취소 완료'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)