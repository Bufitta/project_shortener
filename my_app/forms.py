from django import forms

class ShortenerForm(forms.Form):
    original_url = forms.URLField(label='Url', max_length=1000)