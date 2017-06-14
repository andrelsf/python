# Um dicionario em um dicionario
#coding: utf-8
users = {
        'aferreira':{
            'first': 'andre',
            'last': 'ferreira',
            'location': 'goiânia'
            },
        
        'chris': {
            'first': 'christane',
            'last': 'rezende',
            'location': 'goiania'
            }
        }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation.: " + location.title())
