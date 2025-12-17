# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 08:35:56 2025

@author: alexia.kouletsis25
"""

import tkinter as tk
import tkinter.ttk as ttk

class Frame3:
    
    def __init__(self, r = [], g = {}, c = []):
        
        # initializing inputted lists from the first window
        self.roommates = r
        self.groceries = g
        self.chkVals = c
        
        
        # creating main window
        self.window3 = tk.Tk()
        self.window3.config(padx = 50, pady= 40)
        
        
        # create two frames
        frame1 = tk.Frame(self.window3)
        frame2 = tk.Frame(self.window3)
        
        frame1.pack()
        frame2.pack()

        
        # "receipt" label
        receiptLbl = tk.Label(frame1, text = "Receipt", font = ('Times New Roman', 17, 'bold'))
        receiptLbl.grid(row = 1, columnspan = 20)
       
        
        # line above roommate name labels
        line = ttk.Separator(frame1, orient = 'horizontal')
        line.grid(row = 2, columnspan = 20 , sticky = 'ew', pady = 10)
       
        
        # roommate name labels        
        for i, item in enumerate(self.roommates):
            nameLbl = tk.Label(frame1, text = item, padx = 10)  # Add horizontal padding
            nameLbl.grid(row = 3, column = i * 2)
            nameLbl.config(font = ('Times New Roman', 15, 'bold'))
        
        
        # converting checkvalues from frame2 to be useable here
        converted_chkVals = []
        for row in self.chkVals:
            chkRow = []
            
            for v in row:
                chkRow.append(v.get())
                
            converted_chkVals.append(chkRow)
        self.chkVals = converted_chkVals
        
        
        # column major parsing for what each roommate wants
        thisRoommateWantsThis = []
        list_of_groceries = list(self.groceries.keys())
            
        for y in range (len(self.chkVals[1])):
            iWantThisList = []
            for x in range (len(self.chkVals)):
                if self.chkVals[x][y] == 1:
                    iWantThisList.append(list_of_groceries[x])
                
            thisRoommateWantsThis.append(iWantThisList)
            iWantThisList = []
            
        
        # labels for what each roommate wanted
        for x in range(len(self.roommates)):
            for y in range(len(thisRoommateWantsThis[x])):
                groceryLbl = tk.Label(frame1, text = thisRoommateWantsThis[x][y], padx = 10)
                groceryLbl.grid(row = y + 5, column = x * 2, sticky = 'w')
        
        
        # line below roommate name labels
        line = ttk.Separator(frame1, orient = 'horizontal')
        line.grid(row = 4, columnspan = 20 , sticky = 'ew', pady = 10)   
    
        
        # labels for each roommate's individual total
        roommateTotals = self.calculateTotals()
        
        numOfRows = frame1.size()[1]
        for i, item in enumerate(self.roommates):
            priceLbl = tk.Label(frame1, text = (f"€ {roommateTotals[i]:.2f}"), padx = 10)
            priceLbl.grid(row = numOfRows + 2, column = i * 2) 
             
            
        # line seperating price labels from grocery labels
        line = ttk.Separator(frame1, orient = 'horizontal')
        line.grid(row = numOfRows + 1, columnspan = 20 , sticky = 'ew', pady = 10)   
        
        # another line below individual pricings
        line = ttk.Separator(frame1, orient = 'horizontal')
        line.grid(row = numOfRows + 3, columnspan = 20 , sticky = 'ew', pady = 10)   
        
           
        # lines between roommate columns
        if thisRoommateWantsThis:
            lengths = []
            for items in thisRoommateWantsThis:
                lengths.append(len(items))
                max_items = max(lengths)
        else:
            max_items = 0
        
        total_rows = max_items + 7
        
        for i in range(len(self.roommates) - 1):
                line = ttk.Separator(frame1, orient = 'vertical')
                line.grid(row = 2, column = i * 2 + 1, rowspan = total_rows, sticky = 'ns', pady= 10)
                
        # total!!
        total = 0
        for item in roommateTotals:
            total += item
        
        totalLbl = tk.Label(frame1, text = (f"Total: € {total:.2f}"))
        totalLbl.config(font = ('Times New Roman', 15, 'bold'))
        totalLbl.grid(row = numOfRows + 4, columnspan = 20)
            
    
    def calculateTotals(self):
        # i made this into its own method to clean up the constructor a bit
        # row major parsing for grocery pricings
        divideGroceriesByThisNumber = []
        counter = 0
        
        for x in range (len(self.chkVals)):
            for y in range (len(self.chkVals[x])):
                if self.chkVals[x][y] == 1:
                    counter += 1
                
            divideGroceriesByThisNumber.append(counter)
            counter = 0
        
        
        # calculating cost per grocery
        groceryPrices =  list(self.groceries.values())
        
        splitPrices = []
        for x in range(len(groceryPrices)):
            if divideGroceriesByThisNumber[x] > 0: #should not run into the /0 issue, but just in case
                splitPrices.append(groceryPrices[x] / divideGroceriesByThisNumber[x])
            else:
                splitPrices.append(0)
        
        
        # adding prices each roommate's individual total
        roommateTotals = []
        for y in range (len(self.chkVals[1])):
            roommateTotal = 0
            for x in range (len(self.chkVals)):
                if self.chkVals[x][y] == 1:
                    roommateTotal += splitPrices[x]
                
            roommateTotals.append(roommateTotal)
        
        return roommateTotals
    
        
    def run(self):
        # method to run GUI
        self.window3.mainloop()
        