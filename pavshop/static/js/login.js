var LoginLogic = {
    'url': `${location.origin}/api/token/`,

    fetchToken(email, password) {
        console.log(email, password);
        fetch(this.url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                'email': email,
                'password': password
            })
        }).then(response => response.json()).then(data => {
            localStorage.setItem('data', data);
            if (data.access) {
                localStorage.setItem('token', data.access);
            } else {
                alert(data.message);
            }
        })
    }
}


var submit = document.getElementById('sbmt');

submit.onclick = function () {
    const email = document.querySelector('#id_email').value;
    const password = document.querySelector('#id_password').value;
    LoginLogic.fetchToken(email, password);
    setInterval(form.submit(), 1000);
}