"""
intended flow:
1. find min range of password
2. for each range, check for available words first
   save remaining meaningless permutations in another data struct
   !!!check for use of proper nouns
+ point 2 consists of everything in this file

if current english db is unsatisfactory 
	try: https://wordnet.princeton.edu/
	ref: http://androidtech.com/html/wordnet-mysql-20.php

advanced applications (as per plan):
https://www.topbots.com/4-different-approaches-natural-language-processing-understanding/	
"""
# imports - standard imports
from itertools import combinations_with_replacement, combinations
import json

# imports - module imports
from .browser import *



def generate_keys(suggested):
	"""
	suggested is type(list)
	pass_list is type(list)
	Inputs suggested keywords to generate likely list of passwords
	"""
	pass_list = []
	
	for r in range(11,12):
		pass_list = [''.join(x) for x in combinations(''.join(suggested), r)]

	return pass_list


def import_dictionary():
	"""
	will be called by generate_keys function: helps search meaningful words
	"""
    dictionary = []
    try:
        file = open(r"C:\Users\Gavin\Desktop\data\words_dictionary.json") #location of your scrambled word file
        fileContents = list(json.load(file).keys())
	finally:
        file.close()
    for i in range(len(fileContents)):
        dictionary.extend(fileContents[i].split()) #changes the list by removing \n's from line breaks in text file
    return dictionary


def import_scrambled_words():
	"""
	will be called by the generate_keys function: to check for words
	"""
    scrambledWords = []
    try:
        file = """here take input of permutation of select words""" #location of your scrambled word file
        fileContents = list(json.load(file).keys())
        fileContents = file.readlines() #read text file and store each new line as a string
    finally:
        file.close()
    for i in range(len(fileContents)):
        scrambledWords.extend(fileContents[i].split()) #changes the list by removing \n's from line breaks in text file
    return scrambledWords


def unscramble_word(scrambledWord):
	"""
	will be called by generate_keys function: searches meaningful words
	"""
    countToMatch = len(scrambledWord)
    matchedWords = []
    string = ""

    for word in dictionary:
        count = 0
        for x in scrambledWord:
            if x in word:
                count += 1
            if count == countToMatch:
                matchedWords.append(word)
                break
    for matchedWord in matchedWords:
        if len(matchedWord) == len(scrambledWord):
            print(matchedWord)
            string = matchedWord
            break #this returns only one unscrambles word
    return string


if __name__ == '__main__':
    finalString = ""
    try:
        scrambled = import_scrambled_words()
        print(scrambled)
        dictionary = import_dictionary()
        for x in scrambled:
            finalString += unscramble_word(x)
            finalString +=", "
        len(finalString)

        print(finalString)

    except Exception as e:
        print(e)