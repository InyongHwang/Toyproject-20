let domain = window.location.protocol + '//' + window.location.host
$(document).ready(function () {
    show_comment();
    let token = $.cookie('mytoken')

    if (token == undefined) { // nickname이 아니라 로그인하기 버튼
        $('#profile_area').text('로그인')
    } else {

    }
});

function show_comment() {

    fetch('/projects/main/show').then((res) => res.json()).then((data) => {
        let rows = data['result']
        
        $('#content-list').empty()

        rows.forEach((a) => {
            let id =a['_id']
            let title = a['title']
            let content = a['content']
            content = content.substr(0, 10)
            let url = domain + '/projects/'+id

            let temp_html = `<div>
                                <div class="title"><a href="${url}">${title}</a></div>
                                <div class="writer">${content}</div>
                            </div>`

            $('#content-list').append(temp_html)
        })
    })
}

function is_member() {
    let token = $.cookie('mytoken')
    
    if (token == undefined) {
        alert('로그인이 필요합니다')
        window.location.href = domain + '/login'
    }
}

function go_write_page() {
    let url = domain + '/projects/write'
    window.location.href = url
}

function go_login_page() {
    let url = domain + '/login'
    window.location.href = url
}

function join_list() {
    window.location.href = domain + '/projects/join'
}

function host_list() {
    window.location.href = domain + '/projects/host'
}

function main() {
    window.location.href = domain+ '/projects/main'
}