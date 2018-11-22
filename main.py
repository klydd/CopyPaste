import win32api
from tkinter import Tk
from time import sleep

letters = {'q':'й','w':'ц', 'e':'у', 'r':'к', 't':'е', 'y':'н', 'u':'г', 'i':'ш', 'o':'щ', 'p':'з', '{':'х',
           '}':'ъ', 'a':'ф', 's':'ы', 'd':'в', 'f':'а', 'g':'п', 'h':'р', 'j':'о', 'k':'л', 'l':'д', ';':'ж',
           "'":'э', 'z':'я', 'x':'ч', 'c':'с', 'v':'м', 'b':'и', 'n':'т', 'm':'ь', ',':'б', '.':'ю', '/':'.'}

inverted_letters = {value: key for key, value in letters.items()}

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return str(k)

def letters_swap(buf):
    buflow = buf.lower ()
    paste = str()

    print (buf)
    print ('test')

    for i in buflow:
        if i in letters:
            paste += letters.get(i)
        elif i in inverted_letters:
            paste += inverted_letters.get(i)
        else:
            paste += i

    tk.clipboard_clear ()
    tk.clipboard_append (paste)

print (inverted_letters)
tk = Tk ()
tk.withdraw ()
##print (buf)
left_key = win32api.GetKeyState (0x25)
right_key = win32api.GetKeyState (0x27)
#0 or 1 - key up
#-128 or -127 - key down

while True:
    sleep (1)
    left_key = win32api.GetKeyState (0x25)
    right_key = win32api.GetKeyState (0x27)
    if left_key < 0 and right_key < 0:  
        buf = tk.clipboard_get()
        letters_swap (buf)
