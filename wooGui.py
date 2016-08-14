#!/usr/bin/env python
from woocommerce import API
import csv
import json
import tkinter
from tkinter import *
#create a new window
window = tkinter.Tk()

#http://usingpython.com/making-widgets-look-nice/ see this tutorial

window.title("WooCommerce Data Manager")
window.geometry("600x400")

lblApiUrl = tkinter.Label(window, text="Api Url:",  width=600, justify=LEFT, anchor=W, padx=5, pady=5)
lblApiUrl.pack() #add label to window
tbApiUrl = tkinter.Entry(window)
tbApiUrl.pack(fill=X, padx=10)

lblApiKey = tkinter.Label(window, text="Api Key:", width=600, justify=LEFT, anchor=W, padx=5, pady=5)
lblApiKey.pack() #add label to window
tbApiKey = tkinter.Entry(window)
tbApiKey.pack(fill=X, padx=10)

lblApiSecret = tkinter.Label(window, text="Api Secret",width=600, justify=LEFT, anchor=W, padx=5, pady=5)
lblApiSecret.pack(fill=X)
tbApiSecret = tkinter.Entry(window)
tbApiSecret.pack(fill=X, padx=10)

#to compile the exe file for distribution navigate to the folder and run this command:
# pyinstaller.exe --onefile --windowed {filename}.py

def getCategories():

    wcapi = API(
        url=tbApiUrl.get().strip(),
        consumer_key=tbApiKey.get().strip(),
        consumer_secret=tbApiSecret.get().strip()
    )

    wooCategories = wcapi.get("products/categories").json()

    print(wooCategories)
    
    wooCatsList = wooCategories['product_categories']

    for x in wooCatsList:
        print(x)
  
    #headers  description, slug, id, display, image, parent, count, name          

    with open('categories.csv', 'w', newline='') as csvfile:
         csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
       
         count = 0   

         for wc in wooCatsList:

            if count == 0:
                header = wc.keys()

                csvwriter.writerow(header)
                    
            count +=1
        
            csvwriter.writerow(wc.values())


btnGetCategories = tkinter.Button(window, text="GET CATEGORIES", command=getCategories,justify=LEFT,  anchor=W)
btnGetCategories.pack(side=RIGHT, padx=10)

def clearScreen():
    print('clearing')
    tbApiUrl.delete(0, END)


btnClear = tkinter.Button(window, text="CLEAR", command=clearScreen,  justify=LEFT, anchor=W)
btnClear.pack(side=RIGHT, padx=10)


#draw the window, and start the 'application'
window.mainloop()
