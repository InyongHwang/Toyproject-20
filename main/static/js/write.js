let domain = window.location.protocol + '//' + window.location.host

function save_content() {
    let token = $.cookie('mytoken')
    function parseJwt (token) {
        var base64Url = token.split('.')[1];
        var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
        var jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function(c) {
            return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
        }).join(''));

        return JSON.parse(jsonPayload);
    }

    let member_email = parseJwt(token)['email'].trim()
    let title = $('#title').val()
    let content = $('#content').val()

    let json_data = JSON.stringify({
        'member_email':member_email,
        'title':title,
        'content':content
    })

    fetch('/projects/write', { 
                method: "POST",
                headers: {'Content-Type':'application/json'},
                body: json_data
    }).then((res) => res.json()).then((data) => {
        alert(data["msg"]);
        let url = domain + '/projects/main'
        window.location.href = url
    });
}