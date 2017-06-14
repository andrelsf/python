#
# Percorrendo uma lista inteira com um laço
#
#coding: utf-8


magicians = ['alice', 'david', 'carolina']
# Usando laço for
print("Usando FOR: ")
for magician in magicians:
    print(magician.title())

# Usando laço while
print("\nUsando WHILE:")
x = 0
while x < len(magicians):
    print(magicians[x].title())
    x += 1

for magician in magicians:
    print("\t" + magician.title() + " that was a great trick! ")
    print("\tI can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")
