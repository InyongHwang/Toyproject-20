let token = $.cookie('mytoken')
$(document).ready(function () {
    show_comment();

    if (token == undefined) {
        $('#profile_area').text('로그인')
    } else {
        $('#profile_area').text('로그아웃')
    }
});

function show_comment() {

    fetch('/projects/main/show').then((res) => res.json()).then((data) => {
        let rows = data['result']
        // $('#content-list').empty()
        
        rows.forEach((a) => {
            let id =a['_id']
            let title = a['title']
            let content = a['content']
            content = content.substr(0, 10)
            let url = '/projects/'+id

            let temp_html = `<div>
                                <div class="title"><a href="#" onclick="go_detail('${url}')">${title}</a></div>
                                <div class="writer">${content}</div>
                            </div>`

            $('#content-list').append(temp_html)
        })
    })
}

function go_detail(url) {
    if (token == undefined) {
        alert('로그인이 필요합니다.')
        window.location.href = '/login'
    } else {
        window.location.href = url
    }
}
function go_write_page() {
    if (token == undefined) {
        alert('로그인이 필요합니다.')
        window.location.href = '/login'
    } else {
        window.location.href = '/projects/write'
    }
    
}

function join_list() {
    if (token == undefined) {
        alert('로그인이 필요합니다.')
        window.location.href = '/login'
    } else {
        window.location.href = '/projects/join'
    }
    
}

function host_list() {
    if (token == undefined) {
        alert('로그인이 필요합니다.')
        window.location.href = '/login'
    } else {
        window.location.href = '/projects/host'
    }
   
}

function main() {
    window.location.href = '/projects/main'
}

function log() {
    if (token == undefined) {
        window.location.href = '/login'
    } else {
        $.removeCookie('mytoken', {path:'/'})
        alert('로그아웃!')
        window.location.href = '/'
    }
}