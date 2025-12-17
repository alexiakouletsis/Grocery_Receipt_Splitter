# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 08:57:38 2025

@author: alexia.kouletsis25
"""

import tkinter as tk

class Frame2:
    
    def __init__(self, r = [], g = {}):
        
        # initializing inputted lists from the first window
        self.roommates = r
        self.groceries = g
        
        
        # creating main window
        self.window2 = tk.Tk()
        self.window2.config(padx = 50, pady= 40)
        
        
        # two frames
        frame1 = tk.Frame(self.window2)
        frame2 = tk.Frame(self.window2)
        
        frame1.pack()
        frame2.pack()
        
        
        # summary label
        sumLbl = tk.Label(frame1, text = "Summary:")
        sumLbl.config(font = ('Times New Roman', 15, 'bold'))
        sumLbl.grid(columnspan = 500)  
       
        
        # grocery item labels
        list_of_groceries = list(self.groceries.keys())
        for i, item in enumerate(list_of_groceries):
            itemLbl = tk.Label(frame1, text = item)
            itemLbl.grid(row = i + 4, column = 1, sticky = 'w')
        
        
            #s pacer labels
            itemLbl = tk.Label(frame1, text = ' ' * 10)
            itemLbl.grid(row = i + 4, column = 2)
        
        
            # euro symbol labels
            itemLbl = tk.Label(frame1, text = '€')
            itemLbl.grid(row = i + 4, column = 3, sticky = 'w')
        
        
            # spacer labels
            itemLbl = tk.Label(frame1, text = ' ' * 5)
            itemLbl.grid(row = i + 4, column = 4)
        
        
        # grocery price labels
        list_of_prices = list(self.groceries.values())
        for i, item in enumerate(list_of_prices):
            itemLbl = tk.Label(frame1, text = (f"{item: >.2f}"))
            itemLbl.grid(row = i + 4, column = 5, sticky = 'e') 
        
        
            # spacer labels
            itemLbl = tk.Label(frame1, text = ' ' * 5)
            itemLbl.grid(row = i + 4, column = 6)
            
            
        # checkboxes
        self.list_of_checkboxes_2D = []
        self.list_of_chkvariables_2D = []
        
        for x in range(len(list_of_groceries)):
            list_of_checkboxes = []  
            list_of_chkvariables = []  
            
            for y in range(len(self.roommates)):
                v = tk.IntVar()
                chk = tk.Checkbutton(frame1, variable = v, command = self.processCheckButton)
                chk.grid(row = x + 4, column = y + 7)
                list_of_checkboxes.append(chk)
                list_of_chkvariables.append(v)
               
                
            
            self.list_of_checkboxes_2D.append(list_of_checkboxes)
            self.list_of_chkvariables_2D.append(list_of_chkvariables)
            
            
        # labels of roomate initials above check boxes
        roommate_initials = self.processInitials()
        
        for i, item in enumerate(roommate_initials):
            initialLbl = tk.Label(frame1, text = item)
            initialLbl.grid(row = 3, column = i + 7)
            
        # spacer between "Summary" and roommate initials
        itemLbl = tk.Label(frame1, text = ' ')
        itemLbl.grid(row = 2, columnspan = 20)
        
        
        # clear checkboxes button
        numOfRows = frame1.size()[1]
        clearBtn = tk.Button(frame1, text = "Clear", command = self.processClearButton)
        clearBtn.config(padx = 2, pady = 1)
        clearBtn.grid(row = numOfRows + 1, columnspan = 20, sticky = 'e')
        
        
        # proceed button
        proceedBtn = tk.Button(frame2, text = "Proceed", command = self.processProcButton)
        proceedBtn.config(padx = 15, pady= 7, font = ('Times New Roman', 15))
        proceedBtn.grid(row = 2, columnspan = 20)
        
        
    def processCheckButton(self):
       for x in range(len(self.list_of_chkvariables_2D)):
           for y in range(len(self.list_of_chkvariables_2D[x])):
               
               var = self.list_of_chkvariables_2D[x][y]
               checkbox = self.list_of_checkboxes_2D[x][y]
               
               if var.get() == 1:
                   checkbox.config(bg = "light green")
                  
               else:
                   checkbox.config(bg = "SystemButtonFace")
        
    
    def processProcButton(self):
        # check to make sure each grocery item has at least one person who wants it
        isEveryItemAccountedFor = True
        for x in range(len(self.list_of_chkvariables_2D)):
            totalchks = 0
            for y in range(len(self.list_of_chkvariables_2D[x])):
                totalchks += self.list_of_chkvariables_2D[x][y].get()
            
            if totalchks < 1:
                isEveryItemAccountedFor = False
                break
        
        
        if isEveryItemAccountedFor:
            # proceed to next window! yay!
            self.window2.destroy()
            import GroceryAppFrame3 as g3
        
            app = g3.Frame3(self.roommates, self.groceries, self.list_of_chkvariables_2D)
            app.run()
            
        else:
            # error popup window
            errorWindow = tk.Toplevel(self.window2)
            errorWindow.title("Error")
            errorWindow.config(padx = 30, pady = 20, bg= "#e34234")
            errorWindow.grab_set()
            
            
            # error message
            errorLbl = tk.Label(errorWindow, text = "Make sure at least one person wants each grocery item!")
            errorLbl.config(font = ('Times New Roman', 14), fg = "white", bg = "#e34234")
            errorLbl.pack(pady = 10)
            
            
            # OK button to close the error window
            okBtn = tk.Button(errorWindow, text = "OK", command = errorWindow.destroy)
            okBtn.config(font = ('Times New Roman', 15))
            okBtn.config(padx = 20, pady = 5)
            okBtn.pack(pady = 10)
    
        
    def processClearButton(self):
        for x in range(len(self.list_of_chkvariables_2D)):
            for y in range(len(self.list_of_chkvariables_2D[x])):
                
                var = self.list_of_chkvariables_2D[x][y]
                var.set(0)
                self.list_of_checkboxes_2D[x][y].config(bg = "SystemButtonFace")
                
               
    def processInitials(self):
        # method that returns a list of initials from the list of names for display purposes
        # honestly I just moved this code into a method to make the constructor cleaner
        roommate_i = []
        for i, name in enumerate(self.roommates):
            # first letter of name
            for x in range(1, len(name) + 1):
                initial = name[0:x].lower()
                
                # check if any other roommate's name starts with same initial
                is_unique = True
                for j, other_name in enumerate(self.roommates):
                    if i != j and other_name.lower() != name.lower() and other_name.lower().startswith(initial):
                        is_unique = False
                        break
                
                if is_unique:
                    roommate_i.append(initial.capitalize())
                    break
        
        return roommate_i
    
        
    def run(self):
        # method to run GUI
        self.window2.mainloop()

