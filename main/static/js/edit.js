let domain = window.location.protocol + '//' + window.location.host

$(document).ready(function () {
    show_project();
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
        let url = domain + '/projects/' + post_id
        window.location.href = url
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