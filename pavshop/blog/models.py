from django.db import models
from pavshop.utils.base import BaseModel

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Blog(BaseModel):
    title = models.CharField(max_length=255, verbose_name='title')
    description = models.CharField(max_length=500, verbose_name='description')
    full_description = RichTextUploadingField(blank=True, null= True)
    tag_id = models.ManyToManyField('blog.Tag', related_name="blog_tags")
    category = models.ForeignKey('blog.Blog_Category', on_delete=models.CASCADE, related_name="blogs")
    image = models.ImageField(upload_to='blog/images/', null=True, blank=True, verbose_name='blog_image')

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
    
    def __str__(self):
        return self.title

    




class Comment(BaseModel):
    name = models.CharField(max_length=255, verbose_name='name',null=True, blank=True)
    email = models.EmailField(verbose_name='email',null=True, blank=True)
    subject = models.CharField(max_length=255, verbose_name='subject')
    message = models.TextField(verbose_name='message', default='')
    replied = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Replied',default=None, null=True, blank=True, related_name="replies")
    blog_id = models.ForeignKey(Blog, related_name="blogComment", on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey('users.User', related_name="userComments", on_delete=models.CASCADE, null=True, blank=True) #null silinecek

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
    
    def __str__(self):
        return self.name
    
class Tag(BaseModel):
    title = models.CharField(max_length=255, verbose_name='title')

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        
    def __str__(self):
        return self.title

class Blog_Category(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Category_name")
    product_tag = models.ManyToManyField(Tag, related_name="product_tags")

    class Meta:
        verbose_name = "Blog_category"
        verbose_name_plural = "Blog_categories"

    def __str__(self):
        return self.title

