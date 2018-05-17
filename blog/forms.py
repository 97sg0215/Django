from django import forms

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')

#이거 html <form>태그랑 역할이 같음