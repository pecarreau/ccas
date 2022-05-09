from django.contrib import admin

# Register your models here.
from .models import Aide, Droit, Personne #rend modifiable la class question depuis l'interface admin

admin.site.register(Aide) 
admin.site.register(Personne)
admin.site.register(Droit)