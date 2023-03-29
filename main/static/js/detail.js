let domain = window.location.protocol + '//' + window.location.host

$(document).ready(function () {
    show_project();
});

function show_project() {
    let url = window.location.href
    let post_id = url.split('/').pop()
       
    fetch('/projects/show/' + post_id).then((res) => res.json()).then((data) => {
        if (data['success'] == true) {
            let title = data['title']
            let content = data['content']
            
            // let writer_email = data['member_email'].trim()
            // let member_email = $.cookie('email').trim()
            
            let writer_email = data['member_email'].trim()
            let member_email = 'tjsalszla123@gmail.com'.trim()
            
            $('#title').text(title)
            $('#content').text(content)

            $('#buttons').empty()
            let edit_url = domain + '/projects/edit/' + post_id
            temp_html = `<a href="#" onclick="join_project('${post_id}')" class="on" id="join_button">신청</a>
                         <a href="${edit_url}" id="edit_button">수정</a>
                         <a href="#" onclick="delete_project('${post_id}')" id="delete_button">삭제</a>`
            $('#buttons').append(temp_html)

            if (writer_email == member_email) {
                $('#join_button').hide()
            } else {
                $('#edit_button').hide()
                $('#delete_button').hide()
            }
        } else {
            alert(data['msg'])
        }
    })
}

function delete_project(post_id) {
    let json_data = JSON.stringify({
        'post_id':post_id
    })
    
    fetch('/projects/remove', {
        method:'DELETE',
        headers:{'Content-Type':'application/json'},
        body:json_data
    }).then(res => res.json()).then(data => {
        alert(data['msg'])
        window.location.href = domain + '/projects/main'
    })
}

function join_project(post_id) {
    // let member_email = $.cookie('email')
    let member_email = 'tjsalszla123@gmail.com'

    let json_data = JSON.stringify({
        'member_email':member_email,
        'post_id':post_id
    })

    fetch('/projects/join/in', {
                method:'POST',
                headers:{'Content-Type':'application/json'},
                body:json_data
    }).then(res => res.json()).then(data => {
        alert(data['msg'])
        if (data['success'] == false) {
            window.location.href = domain + '/projects/main'
        } else {
            window.location.href = domain + '/projects/join'
        }
    })
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

function show_nickname() {
    
}