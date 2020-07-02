from django import forms
from .models import Message

class SearchForm(forms.Form):
    q = forms.CharField( max_length=50)

class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('from_email', 'phone', 'subject', 'message',)

