
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

This script shows a simple window on the screen.

author: Jan Bodnar
last modified: January 2011
website: www.zetcode.com
http://zetcode.com/gui/tkinter/introduction/
"""

from tkinter import *
  #here, it WAS: "from Tkinter import Tk, frame, BOTH" but I think that py3.x
	#had a hard time with that.  so I dropped the cap & said "import it all b"

class Example(Frame):

	def __init__(self, parent):
		Frame.__init__(self,parent, background="white")

		self.parent = parent
		self.initUI()

	def initUI(self):
		self.parent.title("Simple")
		self.pack(fill=BOTH, expand=1)

def main():
	root = Tk()
	root.geometry("250x150+300+300")
	app = Example(root)
	root.mainloop()

if __name__ == '__main__':
	main()
