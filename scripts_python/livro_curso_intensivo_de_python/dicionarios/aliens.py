# Informações aninhadas
#coding: utf-8
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

#aliens = [alien_0, alien_1, alien_2]

#for alien in aliens:
#    print(alien)
aliens = []

# Cria 30 alienígenas verdes
for alien_number in range(30):
    new_alien = {
            'color': 'green', 
            'points': 5,
            'speed': 'slow'
            }
    aliens.append(new_alien)

# Muda os três primeiros alienígenas
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Mostra quantos alienígenas foram criados
for alien in aliens[:5]:
    print(alien)
print("...")

# Mostra quantos alienígenas foram criados
print("Total number of aliens: " + str(len(aliens)))
