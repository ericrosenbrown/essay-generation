import os
import random
from numpy.random import choice

def read_csv(path):
	all_lines = ""
	with open(path,"r") as fp:
		line = fp.readline()
		cnt = 1
		while line:
			full_line = line.strip()
			split_line = full_line.split(",")
			split_line = split_line[1:]
			total_line = ""
			for entry in split_line:
				total_line += entry
			if cnt != 1:
				all_lines += total_line
			line = fp.readline()
			cnt += 1
	return(all_lines)

def prepare_markov(data):
	markov_dict = {} 
	split_spaces = data.split(" ")
	
	for word1 in range(len(split_spaces)-1):
		if split_spaces[word1] not in markov_dict.keys():
			markov_dict[split_spaces[word1]] = {split_spaces[word1+1]:1}
		else:
			if split_spaces[word1+1] not in markov_dict[split_spaces[word1]].keys():
				markov_dict[split_spaces[word1]][split_spaces[word1+1]] = 1
			else:
				markov_dict[split_spaces[word1]][split_spaces[word1+1]] += 1
	#print string_phrase
	return(markov_dict)

def next_essay_word(wword,markov_dict):
	word2_dict = markov_dict[wword]
	word2_keys = list(word2_dict.keys())
	word2_amounts =word2_dict.values()
	word2_probs = [amount / sum(word2_amounts) for amount in word2_amounts]

	draw = choice(word2_keys, 1,
              p=word2_probs)
	return(draw[0])
	#nword = random.choice(markov_dict[wword].keys())
	#return nword

def produce_sentences(markov,starting_word):
	cur_word = starting_word
	full_string = cur_word
	for _ in range(10):
		try:
			cur_word = next_essay_word(cur_word,markov_dict)
			full_string += " " + cur_word
		except:
			pass
	return(full_string)

path = "./form.csv"
data = read_csv(path)
markov_dict = prepare_markov(data)
essay = produce_sentences(markov_dict,"have")
print(essay)