
const SubscribeLogic = {
    url: `${location.origin}/api/subscribe/`,

    addSubscriber(mail) {
        console.log(localStorage.getItem('token'));
        fetch(`${this.url}`, {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`,
            },
            body: JSON.stringify({
                'mail': mail,
            }),
        }).then(response => response.json()).then(data => {
            console.log(data);
        });
    }
}


subscribesend = document.getElementById('subscribesend');
subscribesend.addEventListener('click', () => {
    console.log('salam');
    mail = document.getElementById('id_mail').value
    SubscribeLogic.addSubscriber(mail);
})

