from django import forms

from .models import Blog


class createBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['blogtitle', 'content']
        widgets = {
            'blogtitle': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter the title of your blog'
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Write your blog content here',
                    'rows': 5
                }
            ),
        }
