# Make a dictionary to store all the tokens from the sentences 
# Each key is associated with an array of dictionaries
# Key: a word
# Value: all the words that came after that word, with weights assigned to it

# TODO:
# 	count how many words in a sentence, use this to influence length of sentence

import re

class Dictogram:
	def __init__(self, dictionary=None):
		"""
		initiate the current dictionary with a pre-existing dictionary
		"""
		if dictionary:
			self.dictionary = dictionary
		else:
			self.dictionary = {}

			
	def add_tokens(self, string):
    	"""
		Given a string of words, insert start and end tokens,
		parse into tokens, and put into the dictionary.
		"""
		# tokenize string, partitions '...', '!', and '?'
		token_list = re.split(r'([().!? ]+)', string)
		token_list.insert(0, "[START]")
		token_list.insert(len(token_list), "[END]")

		# clean up tokens, if token is an empty string, then remove
		i = 0
		while i<len(token_list):
			if token_list[i].strip() == "":
				token_list.pop(i)
			else:
				i += 1
		
		# store tokens and weights into dict
		for i in range(len(token_list)-1):
			if token_list[i] in self.dictionary.keys():
				word_dict = self.dictionary[token_list[i]]
				if token_list[i+1] in word_dict.keys():
					word_dict[token_list[i+1]] += 1
				else:
					word_dict[token_list[i+1]] = 1
				self.dictionary[token_list[i]] = word_dict

			else: 
				self.dictionary[token_list[i]] = {token_list[i+1]: 1}

		return self.dictionary

	def add_many_tokens(self, long_string):
		"""
		parse a long string into smaller strings, and for each small string
		call the previous function
		"""
		long_string_parsed = re.split(r'\\n', long_string)
		i = 0
		for string in long_string_parsed:
			self.add_tokens(string)
		return self.dictionary

		
