#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial (rachel note: 2nd one on instruction screen)

This script centers a small window on the screen.

author: Jan Bodnar
last modified: January 2011
website: www.zetcode.com
http://zetcode.com/gui/tkinter/introduction/
"""

from tkinter import *
#again just like last time I de-capped Tkinter and
#imported * rather than frame and both, which is what
#the original Bodnar version says to transcribe.

class Example(Frame):

  def __init__(self, parent):
		Frame.__init__(self, parent, background="white")

		self.parent = parent
		self.parent.title("Blentered Window")
		self.pack(fill=BOTH, expand=1)
		self.centerWindow()

	def centerWindow(self):
		w = 290
		h = 150

		sw = self.parent.winfo_screenwidth()
		sh = self.parent.winfo_screenheight()

		x = (sw - w)/2
		y = (sh - h)/2
		self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

def main():
	root = Tk()
	ex = Example(root)
	root.mainloop()

if __name__ == '__main__':
	main()
