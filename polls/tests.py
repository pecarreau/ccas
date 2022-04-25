from django.test import TestCase

# Create your tests here.

import requests

"""
url = "https://mes-aides.1jeune1solution.beta.gouv.fr/api/simulation/via/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYyNWU2ZWQyMWQ0ZWJmODAxMWI5YzhmMiIsInNjb3BlIjoiY2Nhc19zYWludF9sb3Vpc19wcmVwcm9kIiwiZXhwIjoxNjUwMzU5ODMxLCJpYXQiOjE2NTAzNTYyMzF9.Qvios975lPLrZ3hXrqN13ppMZoCgUK-38wANPY3X7-I"
response = requests.get(url, params= "id=openfisca" )
#print(response.json())

content=response.json()

list_key= []
for key in content:
    list_key.append(key)

#for key in list_key :
#   for cle in content[key]:
#        print(cle)

list_infos = []
for key in content['individus']['demandeur']:
    list_infos.append(key)
"""
'''
url = "https://mes-aides.1jeune1solution.beta.gouv.fr/api/simulation/via/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYyNWVhZDAwMTQyYWVkNDc4ZmMzNTllOSIsInNjb3BlIjoiY2Nhc19zYWludF9sb3Vpc19wcmVwcm9kIiwiZXhwIjoxNjUwMzc1NDUyLCJpYXQiOjE2NTAzNzE4NTJ9.EFYCLQHru3PVOK-1Kpkc1X3sNu0UEvIDrJ41PbvwBnY"
response = requests.get(url, params= "id=openfisca" )
content=response.json()
key_aides = []
content_individus_demandeur= content['individus']['demandeur']
for key in content_individus_demandeur : 
    if 'aide' in key or 'gratuite' in key or 'eligibilite' in key or 'bourse' in key or 'carte' in key:
        key_aides.append(key)
aides_eligible = []
for key in key_aides : 
    if content_individus_demandeur[key]['2022-04'] == 1 or content_individus_demandeur[key]['2022-04'] == True : 
        aides_eligible.append(key)
print(aides_eligible)
'''

url = "https://mes-aides.1jeune1solution.beta.gouv.fr/api/simulation/via/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYyNjAzZjlmN2YyM2JhNzgwMGQwOTU5YyIsInNjb3BlIjoiY2Nhc19zYWludF9sb3Vpc19wcmVwcm9kIiwiZXhwIjoxNjUwNDc4NTM1LCJpYXQiOjE2NTA0NzQ5MzV9.oMBjLjrcTLvdhNWYxQjb33jVOkE5oMdFhfX0Wkx6C-w"
response = requests.get(url, params= "id=openfisca" )
content=response.json()
print(content)

