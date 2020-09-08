#!/usr/bin/env python

"""Module for cat util that prints pretty"""
import sys
from rich.console import Console
from rich.traceback import install

install()
CONSOLE = Console()

__author__ = "Tyler Sammons"
__version__ = '1.1'
__maintainer__ = "Tyler Sammons"
__status__ = "beta"
__date__ = '9/8/2020'

def getText():
	text = ""
	while True:
		try:
			text += CONSOLE.input("[bold yellow][^C]STDIN[/][bold red]:>[/] ") + '\n'
		except:
			CONSOLE.print('\n')
			break
	return str(text)

def main():
	filenames = sys.argv[1:]
	if len(filenames) == 0:
		filenames = getText()
		CONSOLE.print(filenames)
		return
	else:
		text = ""
		for file in filenames:
			if str(file) != '-':
				try:
					with open(file, 'r', encoding="utf-16") as f:
						text += f.read()
				except:
					with open(file, 'r') as f:
						text += f.read()
			else:
				text += getText()

		CONSOLE.print(text)
	return

if __name__ == '__main__':
	main()
