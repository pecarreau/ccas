from django.contrib import admin

# Register your models here.


from .models import Question, Choice #rend modifiable la class question depuis l'interface admin

admin.site.register(Question) 
admin.site.register(Choice)