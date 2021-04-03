import Secret_Santa
import tkinter as tk
from tkinter import messagebox

#Class to Start tkinter App
class SecretSanta(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(GreetingPage)

    def switch_frame(self, frame_class, *args, **kwargs):
        new_frame = frame_class(self, *args, **kwargs)
        if self._frame is not None:
           self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

#Start Screen of the application with a simple button to move to next page
class GreetingPage(tk.Frame):
   def __init__(self, master):
       tk.Frame.__init__(self, master)
       
       greeting = tk.Label(self, text = 'Secret Santa Generator')
       greeting.pack(side="top", fill="both", expand=True)
       start_button = tk.Button(self, text='Start', width = 25, height = 5, bg = 'Blue', fg = 'black', command = lambda: master.switch_frame(NumberParticipantsPage))
       start_button.pack()

# Page to enter the number of people playing
class NumberParticipantsPage(tk.Frame):
   def __init__(self, master):
       tk.Frame.__init__(self, master) 
       
       label = tk.Label(self, text="Enter the Number of Participants")
       label.pack(side="top", fill="both", expand=True)

       entry = tk.Entry(self)
       entry.pack(side="top")
       
       # Added variable and assigned variable to allow for an easy to way to the enty value
       self.ent = entry 

       ok_button = tk.Button(self, text='OK', width = 25, height = 3, bg = 'Green', fg = 'black', command = lambda: master.switch_frame(ParticipantPage,self.getEntry()))
       ok_button.pack()
   
   # To retrieve the entry of the number of contestant to by used by participants page 
   def getEntry(self):
       #Validate that Entry is a whole number and not a string or float
       try: 
           return int(self.ent.get())
       except:  
           messagebox.showerror("error", "Please Enter a whole Number")

class ParticipantPage(NumberParticipantsPage):
   def __init__(self, master, number):
       
       self.n = int(number)

       tk.Frame.__init__(self, master)

       # Initiate the lists to store the entries 
       self.nameList = []
       self.emailList = []
       self.i = 0

       name_label = tk.Label(self, text="Enter name of Participant ")
       name_label.pack(side="top", fill="both", expand=True)
       name_entry = tk.Entry(self)
       name_entry.pack(side="top", expand=False)
       self.name_ent = name_entry

       email_label = tk.Label(self, text="Enter email of Participant ")
       email_label.pack(side="top", fill="both", expand=True)
       email_entry = tk.Entry(self)
       email_entry.pack(side="top", expand=False)
       self.email_ent = email_entry

       ok_button = tk.Button(self, text='OK', width = 15, height = 3, bg = 'Green', fg = 'black', 
                            command = lambda: self.storeEntries())
       ok_button.pack(side="bottom", expand= False)
   
   # Function to retrieve entry values and to be stored in lists
   def storeEntries(self):
       self.i =  self.i + 1
       email = self.email_ent.get()
       if (Secret_Santa.validateEmail(email,self.emailList) == True):
            self.nameList.append(self.name_ent.get())
            self.emailList.append(email)
            self.name_ent.delete(0, 'end')
            self.email_ent.delete(0, 'end')
       else:
            self.i = self.i - 1
            self.email_ent.delete(0, 'end')
            messagebox.showerror("error", "Email Address is not Valid or has already been used")
       # When after retrieving last email & name entry then assign the santas and send the email and destroy page
       if self.i == self.n:
           Secret_Santa.assignSantas(self.nameList, self.emailList, self.nameList.copy())
           self.destroy()

if __name__ == '__main__': 
    app = SecretSanta()
    app.mainloop()

