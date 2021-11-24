function myFunction() {
    console.log('salam');
	addToBasket.forEach(item => {
        var prd = item.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement;
        prd.classList.remove("col-md-4");
        prd.classList.add("col-md-7");
    })
}