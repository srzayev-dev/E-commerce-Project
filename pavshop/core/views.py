from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls.conf import path
from django.views.generic import TemplateView, FormView
from django.views.generic.edit import CreateView
from core.forms import ContactForm, SubscribeForm
from core.models import Contact_us, Subscribe
from django.views.generic import ListView
from product.models import Shopping_card
from product.models import Product
from django.db.models import Count
from blog.models import Blog
# from django.core.paginator import EmptyPage, Paginator
# from core.forms import SearchForm
# from core.models import Search

# class SafePaginator(Paginator):
#     def validate_number(self, number):
#         try:
#             return super(SafePaginator, self).validate_number(number)
#         except EmptyPage:
#             if number > 1:
#                 return self.num_pages
#             else:
#                 raise


# class searchView(ListView):
#     model = Product
#     template_name = "search_product.html"
#     paginator_class = SafePaginator
#     paginate_by = 2
#     def post(self, request, *args, **kwargs):
#         form = SearchForm(request.POST)
#         if form.is_valid():
#             search = Search(
#                 search = request.POST.get('searched'),
#                 user = request.user,
#             )
#             search.save()
#             # self.object = self.get_object()
#             context = super().get_context_data(**kwargs)
#             context['form'] = search
#             return self.render_to_response(context=context)
#         else:
#             form = SearchForm()
#             # self.object = self.get_object()
#             context = super().get_context_data(**kwargs)
#             return self.render_to_response(context=context)

#     def get_queryset(self):
#         queryset = Product.objects.all()
#         if self.request.GET.get('searched'):
#             queryset =  queryset.filter(
#             title__contains = self.request.GET.get('searched'))    
#         return queryset
   
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = SearchForm
#         return context

def search_view(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        products = Product.objects.filter(title__contains=searched)
        return render(request, 'search_product.html',
        {'searched' : searched,
        'products' : products,
        })
    else:
        return render(request, 'search_product.html', {})

def home_view(request):
    
    pop_product = Product.objects.annotate(num_rev =Count('review')).order_by('-num_rev')[:4]
    son_product = Product.objects.all()


    context = {
        'title' : 'PAVSHOP - Multipurpose eCommerce HTML5 Template',
        'pop_products': pop_product,
        'son_products': son_product,
       
    }

    return render(request, 'index.html', context=context)


# def contact_view(request):
#     if request.method == "POST" and "contact" in request.POST:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             contact = Contact_us(
#                 fullname = request.POST.get('fullname'),
#                 email = request.POST.get('email'),
#                 phone = request.POST.get('phone'),
#                 subject = request.POST.get('subject'),
#                 message = request.POST.get('message'),
#             )
#             contact.save()
#     else:
#         form=ContactForm(request.POST)   
#     context = {
#         'title' : 'PAVSHOP - Multipurpose eCommerce HTML5 Template',
#         'form' : ContactForm(request.POST or None),   
#     }
#     return render(request, 'contact.html', context=context)

class ContactFormView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        print(form)
        form.save()
        return super().form_valid(form)
    
# def about_us_view(request):
    
#     context = {
#         'title' : 'PAVSHOP - Multipurpose eCommerce HTML5 Template'
#     }

#     return render(request, 'about_us.html', context=context)

class AboutUs(TemplateView):
    template_name = 'about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About Us'
        return context


def profile_view(request):
    context = {
        'title' : 'PAVSHOP - Multipurpose eCommerce HTML5 Template'
    }
    return render(request, 'profile.html', context=context)





# class ProductListView(ListView):
#     model = Shopping_card
#     template_name = "navbar.html"
        
#     def get_all_prdtcs_in_shopping_card(self):
#         return Shopping_card.objects.all()

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['products'] = self.get_all_prdtcs_in_shopping_card()
#         return context

def change_lang(request):
    if request.GET.get('lang') == 'en' or request.GET.get('lang') == 'az':
        path_list =request.META.get('HTTP_REFERER').split('/')
        path_list[3] = request.GET.get('lang')
        path = '/'.join(path_list)
        response = HttpResponseRedirect(path)
        response.set_cookie('django_language', request.GET.get('lang'))
        return response