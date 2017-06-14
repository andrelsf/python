#
# Usando argumentos nomeados arbitrários
#
#coding: utf-8

def build_profile(first, last, **user_info):
    """ Constroi um dicionário contendo tudo que sabemos sobre um usuário."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('andre', 'ferreira',
        location='goiânia', field='TI', country='BR',)
print(user_profile)

