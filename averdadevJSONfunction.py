from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename

print("Enter Order Number")
OrderNr = input()
print("Enter Order Line")
OrderLine = input()
LSOHNUM = OrderNr + OrderLine #To do >> add to dict

print("Input Actual Lattitude")
LZCOORD1 = input()

print("Input Actual Longitutde")
LZCOORD2 = input()

print("Input Quantity")
LTDLQTY = input()

print("Input Weight")
LDSPLINWEI = input()

print("Input Ship Date")
LSHIDAT = input()

print("Input Ship Time")
LSHIHOU = input()

print("Input Job Status")
LZJOBSTAT = input()

print("Input DMS Route")
LZDMSROU = input()

print("Input Vehicle Plate")
LZVEHPLAT = input()

print("Input Signature Name")
LZSIGNNAM = input()

print("Input Signature Image")#test change to image
#LZSIGNIMG = input()
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
LZSIGNIMG = askopenfilename() # show an "Open" dialog box and return the path to the selected file

print("Input Fulfilment Image")#change to img
#LZFFIMG = input()
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
LZFFIMG = askopenfilename() # show an "Open" dialog box and return the path to the selected file

#return Status
LERR = "0 or 1"

#return Mesage
LMESS = ""

resultDict = {
    "LSOHNUM" : LSOHNUM,
    "LZCOORD1" : LZCOORD1,
    "LZCOORD2" : LZCOORD2,
    "LTDLQTY" : LTDLQTY,
    "LDSPLINWEI" : LDSPLINWEI,
    "LSHIDAT" : LSHIDAT,
    "LSHIHOU" : LSHIHOU,
    "LZJOBSTAT" : LZJOBSTAT,
    "LZDMSROU" : LZDMSROU,
    "LZVEHPLAT" : LZVEHPLAT,
    "LZSIGNNAM" : LZSIGNNAM,
    "LZSIGNIMG" : LZSIGNIMG,
    "LZFFIMG" : LZFFIMG,
    "LERR" : LERR,
    "LMESS" : LMESS
}

import json
print(json.dumps(resultDict))#result in JSON Format
