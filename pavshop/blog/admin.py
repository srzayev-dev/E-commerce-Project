from django.contrib import admin

from blog.models import Blog, Comment, Tag, Blog_Category

from django.utils.html import format_html

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'get_blog_image')
    list_filter = ('title',)

    def get_blog_image(self, obj):
        if obj.image:
            img = '<img src="{}" width="100px" height="100px"/>'.format(obj.image.url)
            return format_html(img)
        return format_html('<strong> No Image </strong>')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Blog_Category)

