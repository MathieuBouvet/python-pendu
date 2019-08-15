#!/usr/bin/python3
# -*-coding:Utf-8 -*

import curses
from curses import wrapper

def main(stdscr):
	stdscr.clear()
	screenWidth = curses.COLS-1

	title = curses.newwin(5,screenWidth,0,0)
	hang = curses.newwin(25,screenWidth,5,0)
	word = curses.newwin(5,screenWidth,30,0)
	letters = curses.newwin(5,screenWidth,35,0)
	feedback = curses.newwin(5,screenWidth,40,0)
	
	title.addstr(2,1,"PENDU".center(screenWidth))
	letters.addstr(1,1, "Lettres essayées : ")

	hang.border()
	title.border()
	word.border()
	letters.border()
	feedback.border()

	title.refresh()
	hang.refresh()
	word.refresh()
	letters.refresh()
	feedback.refresh()
	

	while True:
		c = letters.getch()
		try:
			letters.addstr(chr(c))
		except ValueError:
			feedback.addstr("error") 
		letters.refresh()
		feedback.refresh()
wrapper(main)