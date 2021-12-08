from django import forms
from django.forms import fields, widgets
from django.forms.forms import Form
from books.models import Review


class ReviewForm(forms.ModelForm):
    body    = forms.CharField(widget=forms.Textarea(attrs={'class':'border rounded p-2 w-full',
                                                     'placeholder': 'Write you review here'}))
    image   = forms.ImageField(required=False)

    class Meta:
        model = Review
        fields = ['body', 'image']