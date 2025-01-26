from tkinter import * 
from tkinter.ttk import * 
from time import strftime 

root = Tk() 
root.title("Digital Clock") 

def time(): 
    string = strftime('%I:%M:%S %p') 
    label.config(text=string) 
    label.after(1000, time) 
root.configure(bg='black') 
root.geometry('400x200') 
label = Label(root, font=('ds-digital', 80), background='black',foreground='cyan') 
label.pack(pady=50) 
time() 
root.mainloop()
