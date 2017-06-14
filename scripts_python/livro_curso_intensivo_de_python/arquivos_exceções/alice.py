#coding: utf-8
filename = 'alice_wonderland.txt'

"""
try:
    with open(filename) as alice:
        contents = alice.read()
except FileNotFoundError:
    msg = "sorry, the file " + filename + " does not exist."
    print(msg)
"""

try:
    with open(filename) as alice:
        contents = alice.read()
except FileNotFoundError:
    #msg = "Sorry, the file "+ filename + " does not exist."
    #print(msg)
    pass
else:
    # Conta o número aproximado de palavras no arquivo
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
