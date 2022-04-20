import requests

url = 'https://mes-aides.org/api/benefits'
content = requests.get(url).json() #content est une liste de dictionnaire (chacun correspond à une aide)

liste_aide=[]
for aide in content :
    if aide['source']=='openfisca':
        liste_aide.append(aide['id'])

print(liste_aide)