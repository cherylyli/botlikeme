from dictogram import Dictogram
import json

test_dict = Dictogram()

with open('data/input.txt', 'r') as fp:
	file = fp.read()
	test_sentence = test_dict.add_many_tokens(file)
	with open('data/dict.txt', 'w') as output:
		json.dump(test_sentence, output)