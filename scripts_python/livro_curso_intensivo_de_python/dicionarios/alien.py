#coding: utf-8
alien_0 = { 'color': 'green', 'points': 5 }

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points.")

# Adicionando novos pares chave-valor
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# Modificando valores em um dicionario
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'

print("The alien is now " + alien_0['color'] + ".")

# Removendo pares chave-valor
del alien_0['points']
print(alien_0)
