category_name = document.getElementsByName('category_name')
category_name.forEach(element => {
    element.addEventListener('click', function () {
        if (window.location.href.includes('category_name') == false) {
            if (window.location.href.includes('?')) {
                window.location.href += `&category_name=${element.value}`;
            } else {
                window.location.href += `?category_name=${element.value}`;
            }
        } else {
            window.location.href = window.location.href.replace(/category_name=.*?(&|$)/, `category_name=${element.value}$1`);
        }
    })
});
color = document.getElementsByName('color_name')
color.forEach(element => {
    element.addEventListener('click', function () {
        if (window.location.href.includes('color_name') == false) {
            if (window.location.href.includes('?')) {
                window.location.href += `&color_name=${element.value}`;
            } else {
                window.location.href += `?color_name=${element.value}`;
            }
        } else {
            window.location.href = window.location.href.replace(/color_name=.*?(&|$)/, `color_name=${element.value}$1`);
        }
    })
});
brand = document.getElementsByName('brand')
brand.forEach(element => {
    element.addEventListener('click', function () {
        if (window.location.href.includes('brand') == false) {
            if (window.location.href.includes('?')) {
                window.location.href += `&brand=${element.value}`;
            } else {
                window.location.href += `?brand=${element.value}`;
            }
        } else {
            window.location.href = window.location.href.replace(/brand=.*?(&|$)/, `brand=${element.value}$1`);
        }
    })
});
priceSubmit = document.getElementsByName('priceSubmit')
priceSubmit.forEach(element => {
    element.addEventListener('click', function () {
        if (window.location.href.includes('priceSubmit') == false) {
            if (window.location.href.includes('?')) {
                window.location.href += `&priceSubmit=${element.value}`;
            } else {
                window.location.href += `?priceSubmit=${element.value}`;
            }
        } else {
            window.location.href = window.location.href.replace(/priceSubmit=.*?(&|$)/, `priceSubmit=${element.value}$1`);
        }
    })
});
// for (let i = 0; i < first_last.length; i++) {
//     first_last[i].addEventListener('click', function () {
//         if (window.location.href.includes('page') == false) {
//             if (window.location.href.includes('?')) {
//                 window.location.href += `&page=${first_last[i].getAttribute('page')}`;
//             } else {
//                 window.location.href += `?page=${first_last[i].getAttribute('page')}`;
//             }
//         } else {
//             window.location.href = window.location.href.replace(/page=.*?(&|$)/, `page=${first_last[i].getAttribute('page')}$1`);
//         }
//     })
// }
page_num = document.getElementsByClassName('page_num')
for (let i = 0; i < page_num.length; i++) {
    page_num[i].addEventListener('click', function () {
        if (window.location.href.includes('page') == false) {
            if (window.location.href.includes('?')) {
                window.location.href += `&page=${page_num[i].innerText}`;
            } else {
                window.location.href += `?page=${page_num[i].innerText}`;
            }
        } else {
            window.location.href = window.location.href.replace(/page=.*?(&|$)/, `page=${page_num[i].innerText}$1`);
        }
    })
}
previous = document.getElementById('previous')
if (previous) {
    previous.addEventListener('click', function () {
        if (window.location.href.includes('page') == false) {
            if (window.location.href.includes('?')) {
                window.location.href += `&page=${previous.getAttribute('page')}`;
            } else {
                window.location.href += `?page=${previous.getAttribute('page')}`;
            }
        } else {
            window.location.href = window.location.href.replace(/page=.*?(&|$)/, `page=${previous.getAttribute('page')}$1`);
        }
    })
}
next = document.getElementById('next')
if (next) {
    next.addEventListener('click', function () {
        if (window.location.href.includes('page') == false) {
            if (window.location.href.includes('?')) {
                window.location.href += `&page=${next.getAttribute('page')}`;
            } else {
                window.location.href += `?page=${next.getAttribute('page')}`;
            }
        } else {
            window.location.href = window.location.href.replace(/page=.*?(&|$)/, `page=${next.getAttribute('page')}$1`);
        }
    })
}