#!/usr/bin/python3
# -*-coding:Utf-8 -*

NB_TRY = 8

def loadWord():
	# TODO : load word from file
	return "test".upper()

def hiddenWord(word):
	return " ".join([ "_" for i in word])