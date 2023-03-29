let domain = window.location.protocol + '//' + window.location.host
        
$(document).ready(function () {
    show_joining_project();
});

function show_joining_project() {
    // let member_email = $.cookie('email')
    let member_email = 'w.hand715@gmail.com'

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
                                    <button type="button" class="btn btn-dark" onclick="cancle('${join_id}')">신청 취소</button>
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