from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.widgets import TextInput
from blog.models import Comment


class blog_comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name' : forms.TextInput(attrs={
                'type' : "text",
                'class' : "form-control",
                'name' : "name",
            }),
            'email' : forms.TextInput(attrs={
                'type' : "text",
                'class' : "form-control",
                'name' : "email",
            }),
            'subject' : forms.TextInput(attrs={
                'type' : "text",
                'class' : "form-control",
                'name' : "subject",
            }),
            'message' : forms.Textarea(attrs={
                'class' : "form-control",
                'name' : "message",
            }),
        }
        # <textarea class="form-control" placeholder="" name="message"></textarea>
        # 'nickname' : forms.TextInput(attrs={
        #                                 'type' :"text", 
        #                                 'id' : "nickname_field", 
        #                                 'name' : "nickname",
        #                                 'class' : "input-text"}),



