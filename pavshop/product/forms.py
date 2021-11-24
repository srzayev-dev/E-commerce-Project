from django import forms


class ProductReviewsForm(forms.Form):
    review = forms.CharField(widget=forms.Textarea(attrs={'rows': '4'}))
    