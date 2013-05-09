from PIL import ImageGrab
import os
import time
import win32gui
import re

titleRegex = re.compile("Octgn[ ]+version : [0-9\.]+ : Android-Netrunner",re.IGNORECASE)

def screenGrab(box):
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def winEnumHandler( hwnd, ctx ):
    whereIsOctgn = ()
    coords = ()
    if win32gui.IsWindowVisible( hwnd ):
        if titleRegex.search(win32gui.GetWindowText( hwnd )) != None:
        #if win32gui.GetWindowText( hwnd ) == 'Octgn  version : 3.1.16.99 : Android-Netrunner':
            whereIsOctgn = hwnd
            print (hex(whereIsOctgn))
            coords = win32gui.GetWindowRect(whereIsOctgn)
            print (coords)
            win32gui.SetForegroundWindow(whereIsOctgn)
            screenGrab(coords)

def winListHandler( hwnd, ctx ):
    if win32gui.IsWindowVisible( hwnd ):
        print (hex( hwnd ), win32gui.GetWindowText( hwnd ))

def listWindows():
    win32gui.EnumWindows( winListHandler, None )

def screenGrabOctgn():
    win32gui.EnumWindows( winEnumHandler, None )
         
def main():
    screenGrabOctgn()
    listWindows()
 
if __name__ == '__main__':
    main()
