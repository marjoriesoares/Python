import json
firstname=input('What is your firstname? ')
lastname=input('What is your lastname? ')
age=input('How old are you? ')
amount=input('How much do you earn in a month? ')

data={}
data['clients']=[]
data['clients'].append({
    'firstname': firstname,
    'lastname':lastname,
    'age':age,
    'amount':amount})
with open(ruta + '/myfirstJson.json', 'w') as file:
  json.dump(data, file, indent=4)