from core.forms import SubscribeForm
from core.models import Subscribe
from product.models import Product
from django.db.models import Count
from django.shortcuts import render
from blog.models import Blog
from django.db.models.query_utils import Q


def get_subscribe_form(request):
    if request.method == "POST" and "subscribe" in request.POST:
            form = SubscribeForm(request.POST)
            if form.is_valid():
                # subscribe = Subscribe(
                #     mail=request.POST.get('mail')
                # )
                form.save()
    else:
        form= SubscribeForm()
    return {'sub_form':form}

def get_top_product(request):
    top_product = Product.objects.annotate(num_rev =Count('review')).order_by('-num_rev')[:3]
    return {'top_products':top_product}

def search_method(request):
    query = request.GET.get('q', None)
    blogs = Blog.objects.all()
    if query is not None:
        blog = blogs.filter(Q(title__icontains=query) | Q(content__icontains=query))
        return render(request, 'search.html', context = {'blogs':blogs, 'blog':blog})