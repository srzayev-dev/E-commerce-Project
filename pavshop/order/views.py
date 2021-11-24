from django.shortcuts import redirect, render
from order.forms import billing_form, shipping_form, place_order_form
from order.models import Shipping_Info
from product.models import Shopping_card, ItemInShoppingCart, Product

def checkout(request):

    # if request.method == "POST" and 'billing' in request.POST:
    #     form = billing_form(request.POST)
    #     if form.is_valid():
    #         form.save()
    # else:
    #     form = billing_form()

    # if request.method == "POST" and 'shipping' in request.POST:
       
    # else:
    #     form2 = shipping_form()
    
    if request.method == "POST":
        form2 = shipping_form(request.POST)
        if form2.is_valid():
            form2 = Shipping_Info(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            user=request.user,
            company_name=request.POST.get('company_name'),
            country=request.POST.get('country'),
            town=request.POST.get('town'),
            address=request.POST.get('address'),
            payment=request.POST.get('payment'),
            )
            form2.save()
            Shopping_card.objects.filter(user=request.user).filter(is_ordered=False).update(
            is_ordered=True, shipping_address=form2)
            user_cart = Shopping_card.objects.filter(user=request.user).filter(
            is_ordered=True).filter(shipping_address=form2).first()
            for i in range(len(ItemInShoppingCart.objects.filter(userOfShoppingCard=user_cart))):
                quantity = ItemInShoppingCart.objects.filter(userOfShoppingCard=user_cart)[
                    i].product.main_version.quantity - ItemInShoppingCart.objects.filter(userOfShoppingCard=user_cart)[i].quantity
                version = Product.objects.get(id=ItemInShoppingCart.objects.filter(
                userOfShoppingCard=user_cart)[i].product.id)
                mv = version.main_version
                mv.quantity = quantity
                mv.save()
            Shopping_card.objects.get_or_create(user=request.user, is_ordered=False)
        return redirect('checkout')    
    else:
        form2 = shipping_form()



    context = {
        'form2' : form2,

    }
    return render(request, 'checkout.html', context=context)




def shopping_cart(request):
    return render(request, 'shopping_cart.html')
