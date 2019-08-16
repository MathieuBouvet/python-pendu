#!/usr/bin/python3
# -*-coding:Utf-8 -*

NB_TRY = 8

def loadWord():
	# TODO : load word from file
	return "test".upper()

def hiddenWord(word):
	return "".join([ "_" for i in word])

def displayHidden(word):
	i = 0
	hidden=""
	while(i<len(word)):
		hidden += word[i]+" "
		i += 1
	print(hidden)
