import sys
import json
from random import randint
import numpy as np


# takes seed from command ling
arguments = sys.argv[1:]
arguments = ' '.join(arguments)

sentence = '[START] '
sentence += arguments
print("seeding with: " + arguments + " ...")

dictionary = {}

# imports the dictionary
with open('data/dict.txt', 'r') as fp:
    file = fp.read()
    dictonary = json.loads(file)

next_seed_word = sys.argv[len(sys.argv)-1]

# find probability
while next_seed_word != '[END]' and next_seed_word != None:
    possible_words = dictonary[next_seed_word]
    key_list = []
    value_list = []
    for key, value in possible_words.items():
        key_list.append(key)
        value_list.append(value)

    new_word_place = randint(0, np.sum(value_list))
    i = 0
    for num in value_list:
        if new_word_place - num < 0:
            next_seed_word = key_list[i]
            break
        else:
            new_word_place -= num
            i += 1
    
    sentence += " "
    sentence += next_seed_word
    


print(sentence)
