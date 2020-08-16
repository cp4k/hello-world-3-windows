# TIO_CH22_1.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

# Answer to Try It Out, Question 1, Chapter 22

# Program to create silly sentences

import random

noun_file = open("nouns.txt", 'r')
nouns = noun_file.readline()
noun_list = nouns.split(',')
noun_file.close()

adj_file = open("adjectives.txt", 'r')
adjectives = adj_file.readline()
adj_list = adjectives.split(',')
adj_file.close()

verb_file = open("verbs.txt", 'r')
verbs = verb_file.readline()
verb_list = verbs.split(',')
verb_file.close()

adverb_file = open("adverbs.txt", 'r')
adverbs = adverb_file.readline()
adverb_list = adverbs.split(',')
adverb_file.close()

noun = random.choice(noun_list)
adj = random.choice(adj_list)
verb = random.choice(verb_list)
adverb = random.choice(adverb_list)

print("The", adj, noun, verb, adverb + '.')
