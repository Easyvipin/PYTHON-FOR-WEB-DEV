import webbrowser
import sys
import pyperclip
if len(sys.argv) > 1:
    # get address from command arguements
    address = ' '.join(sys.argv[1:])
else:
    # get  address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
