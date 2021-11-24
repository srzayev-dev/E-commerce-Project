from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from product.models import *
from django.db.models import Q
from product.forms import ProductReviewsForm
from django.views.generic import ListView, DetailView
from blog.models import Tag
from django.db.models import Count
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import EmptyPage, Paginator
from django.views.generic import ListView
from django.http import HttpResponseRedirect

class SafePaginator(Paginator):
    def validate_number(self, number):
        try:
            return super(SafePaginator, self).validate_number(number)
        except EmptyPage:
            if number > 1:
                return self.num_pages
            else:
                raise


# def product_detail_view(request, pk):
#     product_detail = Product.objects.get(pk=pk)

#     qs = Product.objects.order_by('-created_at','price')
#     qs2 = Product.objects.all()
#     q_r = Review.objects.all()
#     # all_rws = Product.objects.filter(title='hjhjhjh')[0].review.all()
#     #for i in all_rws:
#         # print(i)
#     # qs3 = qs.filter(Q(title__icontains='h') | Q(title__icontains='5'))
#     # versions = qs2[1].version.all()
#     # for i in versions:
#     #     print(i.size)

#     # *********BRAND-LARI EYNI OLAN MEHSULLAR ******
#     # product1 = qs2[1]
#     # for prod in qs2:
#     #     if prod.brand == product1.brand:
#     #         print(prod)

#     # # ********* SON 3 product ******
#     # Product.objects.order_by("-id")[:3]

#     if request.method == "POST" and 'product_review' in request.POST:
#         form = ProductReviewsForm(request.POST)
#         if form.is_valid():
#             review = Review(
#                 product = Product.objects.get(pk=pk),
#                 name = request.POST.get('name'),
#                 email = request.POST.get('email'),
#                 review = request.POST.get('review')
#             )

#             review.save()
#     else:
#         form = ProductReviewsForm()

#     context = {

#         'products' : qs,
#         'form' : ProductReviewsForm(),
#         'product_detail' : product_detail,
#         'products' : qs2,
#         'title' : 'PAVSHOP - Multipurpose eCommerce HTML5 Template',
#         'review' : q_r
#     }

#     return render(request, 'product_detail.html', context=context)

# '''
# def product_list_view(request):
#     qs2 = Product.objects.all()

#     context = {
#         'title' : 'PAVSHOP - Multipurpose eCommerce HTML5 Template',
#         'products' : qs2
#     }

#     return render(request, 'product_list.html', context=context)
# '''

class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    paginator_class = SafePaginator
    paginate_by = 2
    def get_queryset(self):
        queryset = Product.objects.all()
        if self.request.GET.get('category_name'):
            queryset =  queryset.filter(
            product_category__title = self.request.GET.get('category_name'))
            
        if self.request.GET.get('color_name'):
            queryset =  queryset.filter(Q(versions__color = self.request.GET.get('color_name')) & Q(versions__is_main = True))
            

        if self.request.GET.get('priceranger'):
            if self.request.GET.get('priceranger') == '1':
                queryset = queryset.filter(price__lte = 100)
            elif self.request.GET.get('priceranger') == '2':
                queryset =  queryset.filter(Q(price__gte = 101) & Q(price__lte = 300)) 
            elif self.request.GET.get('priceranger') == '3':
                queryset =  queryset.filter(Q(price__gte = 301) & Q(price__lte = 600))
            elif self.request.GET.get('priceranger') == '4':
                queryset =  queryset.filter(Q(price__gte = 601) & Q(price__lte = 800))
            elif self.request.GET.get('priceranger') == '5':
                queryset =  queryset.filter(Q(price__gte = 801) & Q(price__lte = 1000))
            elif self.request.GET.get('priceranger') == '6':
                queryset = queryset.filter(price__gte = 1001)     
            
        return queryset
    
    def get_popular_tags(self):
        return Tag.objects.annotate(num_tags=Count('blog_tags')).order_by('-num_tags')[:7]
        
    def get_all_categories(self):
        return Product_Category.objects.all()
    
    def get_all_brands(self):
        return Brand.objects.all()
    
    def get_title(self):
        return "PAVSHOP - Multipurpose eCommerce HTML5 Template"
    
    def get_last_10_categories(self):
        # return Product_Category.objects.order_by('-id')[10]
        return Product_Category.objects.annotate(num_categ=Count('Category')).order_by('-num_categ')[:10]
        # return Product_Category.objects.values('id').annotate(title=Count('id')).order_by('-id')[:5]
    
    def get_brands(self):
        brands = Brand.objects.all()
        if len(brands) < 5:
            return brands
        else:
            brands = Brand.objects.order_by('-id')[:4]
            return brands


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['products'] = self.get_products()
        context['title'] = self.get_title()
        context['popular_tag'] = self.get_popular_tags()
        context['categories'] = self.get_last_10_categories()
        context['brands'] = self.get_brands()
        

        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"

    def get_product_detail(self):
        return Product.objects.get(pk=self.kwargs.get('pk'))

    def get_product_price(self):
        return Product.objects.all()
    
    def get_review(self):
        return Review.objects.filter(product=self.kwargs.get('pk'))
    
    def get_price_with_discount(self):
        return Product.objects.get(pk=self.kwargs.get('pk')).price*(100-Product.objects.get(pk=self.kwargs.get('pk')).discount)/100


    def post(self, request, *args, **kwargs):
        form = ProductReviewsForm(request.POST)
        if form.is_valid():
            review = Review(
                product = Product.objects.get(pk=self.kwargs['pk']),
                name = request.POST.get('name'),
                email = request.POST.get('email'),
                review = request.POST.get('review'),
                user = request.user,
            )
            review.save()
            self.object = self.get_object()
            context = super().get_context_data(**kwargs)
            context['form'] = review
            return HttpResponseRedirect(self.request.path_info)
            return self.render_to_response(context=context)
        else:
            form = ProductReviewsForm()
            self.object = self.get_object()
            context = super().get_context_data(**kwargs)
            return self.render_to_response(context=context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_detail'] = self.get_product_detail()
        context['products'] = self.get_product_price()
        context['review'] = self.get_review()
        context['form'] = ProductReviewsForm
        context['price'] = self.get_price_with_discount()
        return context
