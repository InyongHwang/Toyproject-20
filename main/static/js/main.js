let domain = window.location.protocol + '//' + window.location.host
$(document).ready(function () {
    show_comment();
});

function show_comment() {

    fetch('/projects/main/show').then((res) => res.json()).then((data) => {
        let rows = data['result']
        
        $('#content-list').empty()

        rows.forEach((a) => {
            let id =a['_id']
            let title = a['title']
            let content = a['content']

            let url = domain + '/projects/'+id


            let temp_html = `
            
            <div>
                
                <div class="title"><a href="${url}">${title}</a></div>
                <div class="writer">${content}</div>
               

            </div>   `

            $('#content-list').append(temp_html)


        })
    })
}

function go_write_page() {
    let url = domain + '/projects/write'
    window.location.href = url
}

function go_login_page() {
    let url = domain + '/login'
    window.location.href = url
}