# Create your views here.
from re import X
from xxlimited import Xxo
from django.contrib import messages
from django import forms
from django.shortcuts import render
from django.forms import ModelForm
from .models import Droit, Personne


'''
# Sans ModelForm
class ContactForm2(forms.Form):
    name = forms.CharField(max_length=200)
    firstname = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    message = forms.CharField(max_length=1000)

def contact(request):
    # on instancie un formulaire
    form = ContactForm()
    # on teste si on est bien en validation de formulaire (POST)
    if request.method == "POST":
        # Si oui on récupère les données postées
        form = ContactForm(request.POST)
        # on vérifie la validité du formulaire
        if form.is_valid():
            new_contact = form.save()
            # on prépare un nouveau message
            messages.success(request,'Nouveau contact '+new_contact.name+' '+new_contact.email)
            #return redirect(reverse('detail', args=[new_contact.pk] ))
            context = {'pers': new_contact}
            return render(request,'detail.html', context)
    # Si méthode GET, on présente le formulaire
    context = {'form': form}
    return render(request,'contact.html', context)

class CommentForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)
'''

class PersonneForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonneForm, self).__init__(*args, **kwargs)
        self.fields['nom'].label = "nom"
        self.fields['prenom'].label = "prenom"

    class Meta:
        model = Personne
        fields = ('nom', 'prenom')
        widgets = {'message': forms.Textarea(attrs={'cols': 60, 'rows': 2}), }


def CreatePersonne(request):
    # on instancie un formulaire
    form = PersonneForm()
    # on teste si on est bien en validation de formulaire (POST)
    if request.method == "POST":
        # Si oui on récupère les données postées
        form = PersonneForm(request.POST)
        # on vérifie la validité du formulaire
        if form.is_valid():
            new_personne = form.save()
            # on prépare un nouveau message
            messages.success(request,new_personne.nom)
            # return redirect(reverse('detail', args=[new_contact.pk] ))
            context = {'personne': new_personne}
            return render(request, 'thanks.html', context)
    # Si méthode GET, on présente le formulaire
    context = {'form': form}
    return render(request, 'nouvellepersonne.html', context)

class DroitForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DroitForm, self).__init__(*args, **kwargs)
        self.fields['aide'].label = "aide"
        self.fields['personne'].label = "personne"

    class Meta:
        model = Droit
        fields = ('aide', 'personne')
        widgets = {'message': forms.Textarea(attrs={'cols': 60, 'rows': 2}), }


def CreateDroit(request):
    # on instancie un formulaire
    form = DroitForm()
    # on teste si on est bien en validation de formulaire (POST)
    if request.method == "POST":
        # Si oui on récupère les données postées
        form = DroitForm(request.POST)
        # on vérifie la validité du formulaire
        if form.is_valid():
            new_droit = form.save()
            # on prépare un nouveau message
            messages.success(request,new_droit.nom)
            # return redirect(reverse('detail', args=[new_contact.pk] ))
            context = {'droit': new_droit}
            return render(request, 'thanks.html', context)
    # Si méthode GET, on présente le formulaire
    context = {'form': form}
    return render(request, 'nouvellepersonne.html', context)
