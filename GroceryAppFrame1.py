#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 08:41:07 2025

@author: alexiakouletsis
"""

import tkinter as tk

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("600x500")
        self.window.config(borderwidth=20)

        self.frame1 = tk.Frame(self.window)
        self.frame2 = tk.Frame(self.window)
        self.frame3 = tk.Frame(self.window)
        self.frame4 = tk.Frame(self.window)

        self.products = {}
        self.roomies = []

        #LABELS
        entPTxt = tk.Label(self.frame1, text="Enter the products to be bought:")
        entRTxt = tk.Label(self.frame1, text="Enter your roommates:")
        prodTxt = tk.Label(self.frame1, text="Name:")
        costTxt = tk.Label(self.frame1, text="Cost:")
        roomTxt = tk.Label(self.frame1, text="Name:")

        #ENTRY FIELDS
        self.prod = tk.StringVar()
        prodEnt = tk.Entry(self.frame1, textvariable=self.prod)

        self.cost = tk.DoubleVar()
        costEnt = tk.Entry(self.frame1, textvariable=self.cost)

        self.room = tk.StringVar()
        roomEnt = tk.Entry(self.frame1, textvariable=self.room)

        #BUTTONS
        self.prodBtn = tk.Button(self.frame1, text="Enter", command=self.enterProd)
        self.roomBtn = tk.Button(self.frame1, text="Enter", command=self.enterRoom)
        self.proceed = tk.Button(self.frame4, text="Proceed", command = self.processProcButton)

        #PACKING AND GRIDS
        self.frame1.grid(row=0, column=0, sticky="nw")
        self.frame2.grid(row=4, column=0, sticky="nw")
        self.frame3.grid(row=4, column=4, sticky="nw")
        self.frame4.grid(row=6)

        entPTxt.grid(row=1, column=1, columnspan=2)
        entRTxt.grid(row=1, column=3, columnspan=2)
        prodTxt.grid(row=2, column=1)
        costTxt.grid(row=3, column=1)
        roomTxt.grid(row=2, column=3)
        prodEnt.grid(row=2, column=2)
        costEnt.grid(row=3, column=2)
        roomEnt.grid(row=2, column=4)
        
        self.prodBtn.grid(row=4, column=2)
        self.roomBtn.grid(row=3, column=4)
        self.proceed.grid(row=6, column=1, columnspan=4)


    #FUNCTIONS
    def enterProd(self):
        prod = self.prod.get().strip()
        cost = self.cost.get()
        if prod:
            self.products[prod] = cost
            self.prod.set("")
            self.cost.set(0)
            self.refreshProducts()

    def refreshProducts(self):
        #widgets in frame2 are all cleared then created again in order
        for widget in self.frame2.winfo_children():
            widget.destroy()
    
        for i, (prod, cost) in enumerate(self.products.items()):
            message = f"{prod}: {cost:.2f}"
    
            tk.Label(self.frame2, text=message).grid(row=i, column=0, sticky="nw")
            tk.Button(
                self.frame2,
                text="Remove",
                command=lambda p=prod: self.removeProduct(p)).grid(row=i, column=1, sticky="nw")

    def removeProduct(self, prod):
        del self.products[prod]
        self.refreshProducts()

    def enterRoom(self):
        room = self.room.get().strip()
        if room:
            self.roomies.append(room)
            self.room.set("")  # clear field
            self.refreshRoomies()

    def refreshRoomies(self):
        #when this function is called, the widgets in frame3 are all cleared and then created again in order
        for widget in self.frame3.winfo_children():
            widget.destroy()

        for i, name in enumerate(self.roomies):
            tk.Label(self.frame3, text=name).grid(row=i, column=0, sticky="nw")
            tk.Button(self.frame3, text="Remove",
                      command=lambda n=name: self.removeRoommate(n)).grid(row=i, column=1, sticky="nw")

    def removeRoommate(self, name):
        self.roomies.remove(name)
        self.refreshRoomies()

    def run(self):
        self.window.mainloop()
        
    def processProcButton(self):
        if len(self.roomies) == 0 or len(self.products) == 0:
            # error popup window
            errorWindow = tk.Toplevel(self.window) 
            errorWindow.title("Error")
            errorWindow.config(padx = 30, pady = 20, bg= "#e34234")
            errorWindow.grab_set()
            
            
            # error message
            errorLbl = tk.Label(errorWindow, text = "Make sure you enter at least one product and at least one roommate!")
            errorLbl.config(font = ('Times New Roman', 14), fg = "white", bg = "#e34234")
            errorLbl.pack(pady = 10)
            
                
                # OK button to close the error window
            okBtn = tk.Button(errorWindow, text = "OK", command = errorWindow.destroy)
            okBtn.config(font = ('Times New Roman', 15))
            okBtn.config(padx = 20, pady = 5)
            okBtn.pack(pady = 10)
            
            
        else:
            self.window.destroy()
            import GroceryAppFrame2 as g2
            app = g2.Frame2(self.roomies, self.products)
            app.run()
                
                
        
app = GUI()
app.run()