function myFunction() {
	addToBasket.forEach(item => {
        var prd = item.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement;
        prd.classList.remove("col-md-4");
        prd.classList.add("col-md-7");
    })
}

function myFunction2() {
	addToBasket.forEach(item => {
        var prd = item.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement;
        prd.classList.remove("col-md-7");
        prd.classList.add("col-md-4");
    })
}