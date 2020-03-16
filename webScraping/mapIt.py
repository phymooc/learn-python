import sys
import webbrowser
import pyperclip
#! python3
# mapIt.py-Launch a map in the browser using an address from  the command line or clipboard


if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])

else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
