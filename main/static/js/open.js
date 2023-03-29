$(document).ready(function () {
    show_joining_project();

    let token = $.cookie('mytoken')
    if (token == undefined) {
        $('#profile_area').text('로그인')
    } else {
        $('#profile_area').text('로그아웃')
    }
});

function show_joining_project() {
    // 토큰 복호화
    let token = $.cookie('mytoken')

    function parseJwt (token) {
        var base64Url = token.split('.')[1];
        var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
        var jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function(c) {
            return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
        }).join(''));
    
        return JSON.parse(jsonPayload);
    }
    let member_email = parseJwt(token)['email']

    let json_data = JSON.stringify({
        'member_email':member_email
    })
    
    fetch('/projects/open/view', {
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body:json_data
    }).then(res => res.json()).then(data => {
        let projects = data['result']

        let num = 0
        projects.forEach(project => {
            num = num + 1
            let open_project_id = project['open_project_id']
            let title = project['title']

            let temp_html = `<div>
                                <div class="num">${num}</div>
                                <div class="title">${title}</div>
                                <div class="date">
                                    <button type="button" class="btn btn-dark" onclick="check_volunteer('${open_project_id}')">신청자 확인</button>
                                </div>
                            </div>`
            $('#open_projects').append(temp_html)
        })
    })
}

function check_volunteer(open_project_id) {
    let json_data = JSON.stringify({
        'open_project_id':open_project_id
    })

    fetch('/projects/open/volunteer', {
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body:json_data
    }).then(res => res.json()).then(data => {
        let projects = data['result']
        let title = data['title']

        $('#description').empty()
        let description = `<strong>내가 모집한 프로젝트 지원자</strong>
                            <p>"${title}" 프로젝트 지원자 리스트입니다</p>`
        $('#description').append(description)

        $('#open_projects').empty()
        let category = `<div class="top">
                            <div class="num">번호</div>
                            <div class="email">지원자 이메일</div>
                            <div class="email"> </div>
                            <div class="num">승인</div>
                            <div class="num">거절</div>
                        </div>`
        $('#open_projects').append(category)

        let num = 0
        projects.forEach(project => {
            num = num + 1
            
            let vol_id = project['volunteer_id']
            
            let member_email = project['member_email']

            let temp_html = `<div class="top">
                                <div class="num">${num}</div>
                                <div class="email">${member_email}</div>
                                <div class="email"> </div>
                                <div class="num" onclick="accept('${vol_id}')" style="cursor:pointer">승인</div>
                                <div class="num" onclick="reject('${vol_id}')" style="cursor:pointer">거절</div>
                            </div>`
            $('#open_projects').append(temp_html)
        })
    })
}

function accept(volunteer_id) {
    let json_data = JSON.stringify({
        'volunteer_id':volunteer_id
    })

    fetch('/projects/open/volunteer/accept', {
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body:json_data
    }).then(res => res.json()).then(data => {
        alert(data['msg'])
        window.location.reload()
    })
}

function reject(vol_id) {
    let json_data = JSON.stringify({
        'volunteer_id':vol_id
    })

    fetch('/projects/open/volunteer/reject', {
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body:json_data
    }).then(res => res.json()).then(data => {
        alert(data['msg'])
    })
}

function join_list() {
    let token = $.cookie('mytoken')

    if (token == undefined) {
        alert('로그인이 필요합니다.')
        window.location.href = '/login'
    } else {
        window.location.href = '/projects/join'
    }
}

function host_list() {
    let token = $.cookie('mytoken')

    if (token == undefined) {
        alert('로그인이 필요합니다.')
        window.location.href = '/login'
    } else {
        window.location.href = '/projects/open'
    }
   
}

function main() {
    window.location.href = '/projects/main'
}

function log() {
    let token = $.cookie('mytoken')
    
    if (token == undefined) {
        window.location.href = '/login'
    } else {
        $.removeCookie('mytoken', {path:'/'})
        alert('로그아웃!')
        window.location.href = '/'
    }
}