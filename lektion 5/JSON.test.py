import json
attendants = ['Åsa','Kalle', 'Olivia', 'Johan']

with open('data.json','w') as myfile:
    myfile.write(json.dumps(attendants))