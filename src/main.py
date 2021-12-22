from CreateFile import CreateFile
from ProofOS import ProofOS
from WebsiteBlocker import WebsiteBlocker
from WebsiteUnblocker import WebsiteUnblocker
from tkinter import *

ProofOS()
CreateFile()
main = Tk()
title = main.title("WebsiteBlocker")
label = Label(main, text="Hi! This is a simple WebsiteBlocker in Python" + ProofOS.nl + 'Put all the sites you want to block in the file called "SitesToBlock.txt"' + ProofOS.nl + "One site per line").pack()
button_BlockSites = Button(main, text="Block Sites", command=WebsiteBlocker).pack(side="left")
button_UnblockSites = Button(main, text="Unblock all Sites", command=WebsiteUnblocker).pack(side="right")
main.mainloop()
