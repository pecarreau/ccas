# Create your views here.
from django.shortcuts import render
from django.forms import ModelForm
from .models import Contact

# Avec ModelForm
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'firstname', 'email', 'message')

from django import forms

# Sans ModelForm
class ContactForm2(forms.Form):
    name = forms.CharField(max_length=200)
    firstname = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    message = forms.CharField(max_length=1000)

def contact(request):
    contact_form = ContactForm()
    contact_form2 = ContactForm2()
    return render(request,'contact.html', {'myform/contact_form' : contact_form, 'contact_form2' : contact_form2})

class CommentForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)
