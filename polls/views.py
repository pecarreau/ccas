from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Choice, Question
from django.template import loader
from django.http import Http404
import requests

def index(request):
    url = "https://mes-aides.1jeune1solution.beta.gouv.fr/api/simulation/via/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYyNjAxOWJlN2YyM2JhNzgwMGQwNDAwNCIsInNjb3BlIjoiY2Nhc19zYWludF9sb3Vpc19wcmVwcm9kIiwiZXhwIjoxNjUwNDY4ODI1LCJpYXQiOjE2NTA0NjUyMjV9._naULQ2aeQD5QfdXXiaNPOAPIKU4qQNIG4SJKFWTrk4"
    response = requests.get(url, params= "id=openfisca" )
    content=response.json()
    aides_eligible = []
    for cle in content :    
        content_key= content[cle]
        for item in content_key :
            key_aides = []
            content_key_item = content_key[item]
            for key in content_key_item : 
                if 'aide' in key or 'gratuite' in key or 'eligibilite' in key or 'bourse' in key or 'carte' in key:
                    key_aides.append(key)  
            for key in key_aides : 
                if content_key_item[key]['2022-04'] == 1 or content_key_item[key]['2022-04'] == True : 
                    aides_eligible.append(key)
    return render(request,'polls/index.html',{'content' : content, 'content_individus_demandeur' : content_key, 'aides_eligible' : aides_eligible })

def index1(request):
    url = "https://mes-aides.1jeune1solution.beta.gouv.fr/api/simulation/via/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYyNjAzZjlmN2YyM2JhNzgwMGQwOTU5YyIsInNjb3BlIjoiY2Nhc19zYWludF9sb3Vpc19wcmVwcm9kIiwiZXhwIjoxNjUwNDc4NTM1LCJpYXQiOjE2NTA0NzQ5MzV9.oMBjLjrcTLvdhNWYxQjb33jVOkE5oMdFhfX0Wkx6C-w"
    response = requests.get(url, params= "id=openfisca" )
    content=response.json()
    url2 = 'https://mes-aides.org/api/benefits'
    content2 = requests.get(url2).json() #content est une liste de dictionnaire (chacun correspond à une aide)
    liste_aide=[]
    liste_eligibilite = []
    for aide in content2 :
        if aide['source']=='openfisca':
            liste_aide.append(aide['id'])

    for cle in content:
        for key in content[cle]:
            for item in content[cle][key]:
                x=content[cle][key][item]
                
                liste_cle  = []
                for val in x : 
                    liste_cle.append(val)
                if '2022-04' in liste_cle : 
                        if (x['2022-04'] == True or x['2022-04'] == 1) and item in liste_aide:
                            liste_eligibilite.append(item)
    return render(request,'polls/index1.html',{ 'liste_eligibilite' : liste_eligibilite })
'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
#context est un argument qui référence les variables pouvant être appelée dans le fichier html

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
'''

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
