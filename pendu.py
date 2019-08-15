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
		c = hang.getch()
		hang.addstr("GAAAAAAAAAAAA")
		title.addstr("GAAAAAAAAAAAA".center(40,str(curses.ACS_HLINE)[0]))
		title.refresh()
wrapper(main)