#!/usr/bin/python3
# -*-coding:Utf-8 -*

from functions import *

theWord = loadWord()
hidden = hiddenWord(theWord)
remainingTries = NB_TRY
triedLetters = []
wordDiscovered = False

while(remainingTries > 0 and not wordDiscovered):
	displayHidden(hidden)
	letter = getLetterInput(triedLetters)
	print(triedLetters.append(letter))
	indexes = letterIn(letter, theWord)
	if( not indexes[0] == -1):
		hidden = getUpdatedHidden(hidden, letter, indexes)
	else:
		remainingTries -= 1
	if(theWord == hidden):
		wordDiscovered = True
	print("Lettres essayées : {0}. {1} tentative(s) restante(s)".format(", ".join(triedLetters), remainingTries))
if(wordDiscovered):
	print("Gagné !")
else:
	print("perdu :(")
