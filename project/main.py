#! /usr/bin/python3

#Library importation
from lib.functions import WordsModifications, WordmasterApresentation

#Objects declaration
wordmasterapresentation = WordmasterApresentation()
wordsmodifications = WordsModifications()

#Banner executation, insert directory of wordlists
wordmasterapresentation.banner()
initial_wordlist = input("Insert directory of original wordlist: ")
final_wordlist = input("Insert directory of final wordlist: ")

#Read original wordlist
initial_wordlist = open(initial_wordlist, "r")
initial_wordlist = initial_wordlist.readlines()

#Create file to final wordlist
final_wordlist = open(final_wordlist, "w")

#Count words number
words_number = len(initial_wordlist)

#Start execution of wordmaster functions
wordsmodifications.originalWords(initial_wordlist, final_wordlist, words_number, 0)
wordsmodifications.doubleName(initial_wordlist, final_wordlist, words_number, 0)
