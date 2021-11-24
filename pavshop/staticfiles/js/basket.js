const addToBasket = document.querySelectorAll('.icon-basket');
let basket = document.getElementById("basket-main")
let bslist = document.getElementById("shoppinglist")
let update_btn = document.getElementById("updatebtn");
let order_detail = document.getElementsByClassName("order-detail")
let total = 0
let subtotal = 0
let subtotal2 = 0
let user_id = 0
window.addEventListener("load", async function(){
	let response = await fetch(
		`${location.origin}/api/itemCard/`,{
			method: 'GET',
			headers:{
				'Content-Type': 'application/json',
				'Authorization': `Bearer ${localStorage.getItem('token')}`
			},
		}
	)
	let responseData = await response.json();
	let basket = document.getElementById("basket-main")
	total = 0
	if (responseData){
		for (i of responseData){
			var eded = 0
			basket.innerHTML += `<li>
			<div class="media-left">
			<div class="cart-img"> <a href="#"> <img class="media-object img-responsive" src="${i['product']['main_version']['image']}" alt="..."> </a> </div>
			</div>
			<div class="media-body">
			<h6 class="media-heading">${i.product.title}</h6>
			<span class="price">Price: ${i.product.price}</span> <span class="qty">QTY: ${i['quantity']}</span> </div>
			</li>`
			eded += parseInt(i.product.price)
			eded = eded * i['quantity']
			total += eded
			subtotal2 = total
			if (order_detail[0]){
				order_detail[0].innerHTML += `
				<p data3="${i.product.id}" class="lsprd">${i.product.title}<span>$${i.product.price} </span></p>
				`
				}
		}
		if (order_detail[0]){
			order_detail[0].innerHTML += `
			<p class="all-total">TOTAL COST <span> ${subtotal2}</span></p>
			`
		}
		if (bslist != null){
			bslist.innerHTML += `
			<div class="cart-head">
            <ul class="row">
              <!-- PRODUCTS -->
              <li class="col-sm-2 text-left">
                <h6>PRODUCTS</h6>
              </li>
              <!-- NAME -->
              <li class="col-sm-4 text-left">
                <h6>NAME</h6>
              </li>
              <!-- PRICE -->
              <li class="col-sm-2">
                <h6>PRICE</h6>
              </li>
              <!-- QTY -->
              <li class="col-sm-1">
                <h6>QTY</h6>
              </li>
              
              <!-- TOTAL PRICE -->
              <li class="col-sm-2">
                <h6>TOTAL</h6>
              </li>
              <li class="col-sm-1"> </li>
            </ul>
          </div>`
		  quantityArr =[]
		  productIdArr = []
		  var total = 0
			for (i of responseData){
				if (i.quantity != 0){
				quantityArr.push(i.quantity)
				productIdArr.push(i.product.id)
				var eded = 0
				eded += parseInt(i.product.price)
				eded = eded * i['quantity']
				total += eded
				
				bslist.innerHTML += `
				<ul class="row cart-details">
				<li class="col-sm-6">
				  <div class="media"> 
					<!-- Media Image -->
					<div class="media-left media-middle"> <a href="#." class="item-img"> <img class="media-object" src="${i['product']['main_version']['image']}" alt=""> </a> </div>
					
					<!-- Item Name -->
					<div class="media-body">
					  <div class="position-center-center">
						<h5>${i.product.title}</h5>
						<p>${i.product.mini_description}</p>
					  </div>
					</div>
				  </div>
				</li>
				
				<!-- PRICE -->
				<li class="col-sm-2">
				  <div class="position-center-center"> <span class="price"><small>$</small>${i.product.price}</span> </div>
				</li>
				
				<!-- QTY -->
				<li class="col-sm-1">
				  <div class="position-center-center">
					<div class="quinty"> 
					  <!-- QTY -->
					  <select data2="${i.product.id}" onmouseover="changeQuantity()" class="selectpicker" style="display: initial !important; ">
						<option>1</option>
						<option>2</option>
						<option>3</option>
						<option>4</option>
						<option>5</option>
						<option>6</option>
						<option>7</option>
						<option>8</option>
						<option>9</option>
						<option>10</option>
						<option selected>${i.quantity}</option>
					  </select>
					</div>
				  </div>
				</li>
				
				<!-- TOTAL PRICE -->
				<li class="col-sm-2">
				  <div class="position-center-center"> <span class="price"><small>$</small>${total}</span> </div>
				</li>
				
				<!-- REMOVE -->
				<li class="col-sm-1">
				  <div class="position-center-center"> <a href="#."><i data2="${i.product.id}" class="icon-close" onmouseover="rmv()"></i></a> </div>
				</li>
			  </ul>
				`
			}
			subtotal += total
			total = 0
		}

		}
		
	}
	
	if (basket){
		basket.innerHTML+=`<li>
		<h5 class="text-center">SUBTOTAL: ${subtotal2} USD</h5>
		</li>
		<li class="margin-0">
		<div class="row">
		<div class="col-xs-6"> <a href="${location.origin}/order/shoppingcart/" class="btn">VIEW CART</a></div>
		<div class="col-xs-6 "> <a href="${location.origin}/order/checkout/" class="btn">CHECK OUT</a></div>
		</div>
		</li>`

	}
	total = 0
})




const BasketLogic = {
	url: `${location.origin}/api/card/`,

	addProduct(productId, product_qty, action ) {
		console.log(localStorage.getItem('token'));
		fetch(`${this.url}`, {
			method: 'POST',
			credentials: 'include',
			headers: {
				'Content-Type': 'application/json',
				'Authorization': `Bearer ${localStorage.getItem('token')}`
			},
			body: JSON.stringify({
				'product_id': productId,
				'product_qty': product_qty,
				'action' : action,
			})
		}).then(response => response.json()).then(data => {
			basket.innerHTML = ''
			total = 0
			for (let i of data){
				if (i.quantity != 0){
				var eded = 0
				basket.innerHTML += `<li>
				<div class="media-left">
				  <div class="cart-img"> <a href="#"> <img class="media-object img-responsive" src="${i['product']['main_version']['image']}" alt="..."> </a> </div>
				</div>
				<div class="media-body">
				  <h6 class="media-heading">${i.product.title}</h6>
				  <span class="price">${i.product.price} USD</span> <span class="qty">QTY: ${i.quantity} </span> </div>
				</li>`
				eded += parseInt(i.product.price)
				eded = eded * i.quantity
				total += eded
				}
			}	
				basket.innerHTML +=`<li>
					<h5 class="text-center">SUBTOTAL: <span class="basket_subtotal_price"> ${total}</span>  USD</h5>
					  </li>
					  <li class="margin-0">
						<div class="row">
							  <div class="col-xs-6"> <a href="${location.origin}/order/shoppingcart/" class="btn">VIEW CART</a></div>
							  <div class="col-xs-6 "> <a href="${location.origin}/order/checkout/" class="btn">CHECK OUT</a></div>
						</div>
					  </li>
			`
			if (order_detail[0]){
			order_detail[0].removeChild(order_detail[0].lastElementChild);
			order_detail[0].innerHTML += `
			<p class="all-total">TOTAL COST <span> ${total}</span></p>
			`
			}
		});
		total=0;
	}
}


addToBasket.forEach(item => {
    item.onclick = function () {
        const productId = this.getAttribute('data');
		let product_qty = document.getElementById("product_qty");
		try{
			BasketLogic.addProduct(productId, product_qty.value, 'add');
		}catch{
			BasketLogic.addProduct(productId, 1, 'add');
		}
    }
})

if (update_btn){
update_btn.onclick = function (){
	for (let i = 0; i < productIdArr.length; i++) {
			BasketLogic.addProduct(productIdArr[i], quantityArr[i], 'update');
		}
	// }
}
}
	function changeQuantity(){
		let pckr = document.getElementsByClassName("selectpicker")
		for (let i = 0; i < pckr.length; i++) {
		pckr[i].onchange = function(){
		productQuantityId = pckr[i].getAttribute('data2');
		console.log(productQuantityId, "sasas");
		quantityArr[i] = parseInt(pckr[i].value)
		}
	}
}
// 	// pckr.forEach(item => {
// 	// 	item.onchange = function () {
// 	// 		quantityOnChange = this.value;
// 	// 		console.log(quantityOnChange);
// 	// 	}
// 	// })
// }

function rmv(){
	let removeBasket = document.querySelectorAll('.icon-close');
	removeBasket.forEach(item => {
    item.onclick = function () {
		var li = item.parentElement.parentElement.parentElement.parentElement;
		console.log("product silindi");
        const productId = this.getAttribute('data2');
		li.remove();
		BasketLogic.addProduct(productId, 0, 'remove');
		let lsprd = document.querySelectorAll('.lsprd');
		lsprd.forEach(item => {
			let prdid = item.getAttribute('data3');
			if (prdid == productId){
				item.remove()
			}
		})
    }
})
}
