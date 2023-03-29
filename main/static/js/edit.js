$(document).ready(function () {
    show_project();
    let token = $.cookie('mytoken')
    if (token == undefined) {
        $('#profile_area').text('로그인')
    } else {
        $('#profile_area').text('로그아웃')
    }
});

function show_project() {
    let url = window.location.href
    let post_id = url.split('/').pop()
       
    fetch('/projects/edit/show/' + post_id).then((res) => res.json()).then((data) => {
        let title = data['title']
        let content = data['content']
        
        $('#title').val(title)
        $('#content').text(content)

        $('#edit_button').empty()
        let temp_html = `<a href="#" class="on" onclick="edit_project('${post_id}')">수정하기</a>`
        $('#edit_button').append(temp_html)
    })
}

function edit_project(post_id) {
    let title = $('#title').val()
    let content = $('#content').val()

    let json_data = JSON.stringify({
        'post_id':post_id,
        'title':title,
        'content':content
    })

    fetch('/projects/edit', {
                method:'PUT',
                headers:{'Content-Type':'application/json'},
                body:json_data
    }).then(res => res.json()).then(data => {
        alert(data['msg'])
        let url = '/projects/' + post_id
        window.location.href = url
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