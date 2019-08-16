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

def letterIn(letter, word):
	i = 0
	indexes = []
	found = False
	while( i < len(word)):
		if( letter == word[i]):
			indexes.append(i)
			found = True
		i += 1
	if ( not found):
		indexes.append(-1)
	return indexes

def getUpdatedHidden(hidden, letter, indexes):
	lettersList = [ letter for letter in hidden ]
	for i in indexes:
		lettersList[i] = letter
	return "".join(lettersList)

def getLetterInput(triedLetters):
	letter = ""
	readInputNextTime = True
	while(readInputNextTime):
		readInputNextTime = False
		letter = input("Entrez une lettre : ")
		if(len(letter) > 1 or ord(letter) < 65 or ord(letter) > 122 or letter.upper() in triedLetters):
			readInputNextTime = True
	return letter.upper()


