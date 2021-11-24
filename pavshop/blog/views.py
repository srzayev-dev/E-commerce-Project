from django.core.checks import messages
from django.db.models.query_utils import Q
from django.forms.models import model_to_dict
from django.http import request
from django.shortcuts import render
# from django.views.generic import View, DetailView
# from django.views.generic.list import ListView
from django.views.generic import View, DetailView, ListView
from blog.models import Blog, Tag, Blog_Category
from django.db.models import Count, query
from blog.models import Blog,Comment
from blog.forms import blog_comment_form
from django.utils import timezone
from django.core.paginator import EmptyPage, Paginator
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


def blog_detail(request, pk):
    blog_detail = Blog.objects.get(pk=pk)
    qs = Blog.objects.order_by('-created_at')

    
    # you make like it
    blogs = Blog.objects.all()
    # blog1 = blogs[0]
    # for blog in blogs.all():
    #     if blog1.category == blog.category:
    #         print(blog)
        
    #q1=Blog.objects.values('title', 'description') 

    comments = Comment.objects.filter(blog_id=pk)

    q2=Blog.objects.all()
    q_m_t=Tag.objects.annotate(num_tags=Count('blog_tags')).order_by('-num_tags')[:5]
    q_m=list(q_m_t)
    q5 = Blog.objects.order_by('-id')[:3]
    q6=list(q2)

    if request.method == "POST" and 'comment_blog' in request.POST:
        form = blog_comment_form(request.POST)
        if form.is_valid():
            comment = Comment(
                blog_id = Blog.objects.get(pk=pk),
                message = request.POST.get('message'),
                email = request.POST.get('email'),
                name = request.POST.get('name'),
                subject = request.POST.get('subject'),
                user = request.user,
            )
            comment.save()
    else:
        form = blog_comment_form()
    context = {
        'blogs' : q5,
        'blog' : q6,
        'popular_tag' : q_m,
        'blog_detail' : blog_detail,
        'blogss' : qs,

        # 'recent' : q6,
        'form' : form,
        'like_it' : blogs,

        'form' : form,
        'comments' : comments

    }

    return render(request, 'blog_detail.html', context=context)

def blog_list(request):
    q5 = Blog.objects.order_by('-id')[:3]
    q_m_t=Tag.objects.annotate(num_tags=Count('blog_tags')).order_by('-num_tags')[:7]
    q_m=list(q_m_t)
    q2=Blog.objects.all()
    q6=list(q2)
    all_blogs = Blog.objects.all()
    all_blogs_categories = Blog_Category.objects.all()
    context = {
        'blogs' : q5,
        'popular_tag' : q_m,
        'blog' : q2,
        'all_blogs_categories' : all_blogs_categories,
    }
    return render(request, 'blog_list.html', context = context)


class blogList(ListView):
    model = Blog
    template_name = "blog_list.html"
    paginator_class = SafePaginator
    paginate_by = 1
    # context_object_name = 'blgs'

    def get_last3(self):
        return Blog.objects.order_by('-id')[:3]
        
    def get_popular_tags(self):
        q_m_t=Tag.objects.annotate(num_tags=Count('blog_tags')).order_by('-num_tags')[:7]
        return list(q_m_t)

    def get_queryset(self):
        queryset = Blog.objects.all()
        if self.request.GET.get('category_name'):
            queryset =  Blog.objects.filter(
                category__title = self.request.GET.get('category_name'))
        return queryset

    def get_all_categories(self):
        return Blog_Category.objects.all()

    # def get(self, request, *args, **kwargs):
    #     context = {
    #         'blogs' : self.get_last3(),
    #         'popular_tag' : self.get_popular_tags(),
    #         # 'blog' : self.get_all_blogs(),
    #         'all_blogs_categories' : self.get_all_categories(),
    #     }
    #     return render(request, 'blog_list.html', context = context)
    
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['products'] = self.get_products()
        context['blogs'] = self.get_last3()
        context['popular_tag'] = self.get_popular_tags()
        context['all_blogs_categories'] = self.get_all_categories()

        return context

class BlogGenericDetail(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    def get_all_categories(self):
        return Blog_Category.objects.all()
    def get_blog_detail(self):
        return Blog.objects.get(pk=self.kwargs['pk'])
    def get_blogs_by_create(self):
        return Blog.objects.order_by('-created_at')
    def get_comments(self):
        return Comment.objects.filter(blog_id=self.kwargs['pk'])
    def get_all_blogs(self):
        return Blog.objects.all()
    def get_popular_tags(self):
        return list(Tag.objects.annotate(num_tags=Count('blog_tags')).order_by('-num_tags')[:5])
    def get_last3(self):
        return Blog.objects.order_by('-id')[:3]
    
    
    def post(self, request, *args, **kwargs):
        form = blog_comment_form(request.POST)
        if form.is_valid():
            comment = Comment(
                blog_id = Blog.objects.get(pk=self.kwargs['pk']),
                message = request.POST.get('message'),
                email = request.POST.get('email'),
                name = request.POST.get('name'),
                subject = request.POST.get('subject'),
                user = request.user,
            )
            comment.save()

            self.object = self.get_object()
            context = super().get_context_data(**kwargs)
            context['form'] = form
            return HttpResponseRedirect(self.request.path_info)
            return self.render_to_response(context=context)
        else:
            form = blog_comment_form()
            self.object = self.get_object()
            context = super().get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context=context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'blogs' : self.get_last3(),
            'blog' : self.get_all_blogs(),
            'popular_tag' : self.get_popular_tags(),
            'blog_detail' : self.get_blog_detail(),
            'blogss' : self.get_blogs_by_create(),
            'comments' : self.get_comments(),
            'form' : blog_comment_form,
            'all_blogs_categories' : self.get_all_categories(),
          
        }
        return context

def januar_blogs(request):
    jan = Blog.objects.filter(created_at__month=1)
    context = {'yanvar':jan}
    return render(request, 'january.html', context=context)
def februar_blogs(self):
    feb = Blog.objects.filter(created_at__month=2)
    context = {'fevral':feb}
    return render(request, 'february.html', context=context)

def martch_blogs(request):
    martch = Blog.objects.filter(created_at__month=3)
    context = {'mart':martch}
    return render(request, 'march.html', context=context)
def april_blogs(request):
    april = Blog.objects.filter(created_at__month=4)
    context = {'aprel':april}
    return render(request, 'april.html', context=context)
def may_blogs(request):
    may= Blog.objects.filter(created_at__month=5)
    context = {'may':may}
    return render(request, 'may.html', context=context)
def june_blogs(request):
    juny = Blog.objects.filter(created_at__month=6)
    context = {'iyun':juny}
    return render(request, 'june.html', context=context)
def july_blogs(request):
    july = Blog.objects.filter(created_at__month=7)
    context = {'iyul':july}
    return render(request, 'july.html', context=context)
def august_blogs(request):
    august = Blog.objects.filter(created_at__month=8)
    context = {'avgust':august}
    return render(request, 'august.html', context=context)
def september_blogs(request):
    semp = Blog.objects.filter(created_at__month=9)
    context = {'sentyabr':semp}
    return render(request, 'september.html', context=context)
def october_blogs(request):
    oct = Blog.objects.filter(created_at__month=10)
    context = {'oktyabr':oct}
    return render(request, 'october.html', context=context)
def november_blogs(request):
    nov = Blog.objects.filter(created_at__month=11)
    context = {'noyabr':nov}
    return render(request, 'november.html', context=context)
def december_blogs(request):
    dec = Blog.objects.filter(created_at__month=12)
    context = {'dekabr':dec}
    return render(request, 'december.html', context=context)

# class BlogSearchView(ListView):
#     model = Blog
#     template_name = 'blog_list.html'
#     queryset = Blog.objects.all()
#     context_object_name = 'blog'

#     def get_queryset(self):
#         query= self.request.GET.get('q')
#         return Blog.objects.filter(title__icontains=query).order_by('-created_at')

def search_method(request):
    if request.method == 'POST':
        search_b = request.POST['search_b']
        blogs = Blog.objects.filter(title__icontains=search_b)
        return render(request, 'search.html',
        {'search_b' : search_b,
        'blogs' : blogs,
        })
    else:
        return render(request, 'search.html', {})