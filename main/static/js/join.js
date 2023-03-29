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

    fetch('/projects/join/view', {
                method:'POST',
                headers:{'Content-Type':'application/json'},
                body:json_data
    }).then(res => res.json()).then(data => {
        let projects = data['result']
        
        let num = 0
        projects.forEach((project) => {
            num = num + 1
            let title = project['title']
            let join_id = project['join_id']

            let temp_html = `<div>
                                <div class="num">${num}</div>
                                <div class="title">${title}</div>
                                <div class="date">
                                    <button type="button" class="btn btn-dark cancle-btn" onclick="cancle('${join_id}')">신청 취소</button>
                                </div>
                            </div>`
            $('#projects').append(temp_html)
        })
    })
}

function cancle(join_id) {
    let json_data = JSON.stringify({
        'join_id':join_id
    })

    fetch('/projects/join/out', {
                method:'DELETE',
                headers:{'Content-Type':'application/json'},
                body:json_data            
    }).then(res => res.json()).then(data => {
        alert(data['msg'])
        window.location.reload()
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