import tkinter as tk
from tkinter import *

# from ctypes import windll                         #Apply when blur
# windll.shcore.SetProcessDpiAwareness(1)

window = tk.Tk()

# window.resizable(False, False)
window.attributes("-alpha", 1)  # window's transparency 
window.attributes("-topmost", 1)  # Window stacking
window.title("Tkinter")           # Title
# window.geometry("270x350")        # size
window.config(bg="white")         # Backgroung Colors

# window.columnconfigure(index=0, weight=1)
# window.columnconfigure(index=1, weight=1)
# window.columnconfigure(index=2, weight=1)
# window.columnconfigure(index=3, weight=1)

window.iconbitmap("C:/Users/Cheng/Desktop/Tkinter Calculator/calculator.ico")  # Set Icon

# mainFrame = Frame(window, borderwidth=1, bg="red")
# mainFrame.grid()
# mainFrame.rowconfigure(index=0, weight=1)
# mainFrame.rowconfigure(index=1, weight=2)

expression = StringVar()

# canvas = Canvas(window, bd=0).grid_anchor(N)
# inputField_Frame = Frame(window, borderwidth=2, bg="blue")
# inputField_Frame.grid(column=0, row=0, columnspan=4)
InputField = tk.Entry(
    window, 
    # width=17,
    # foreground="black", 
    # background="white", 
    textvariable=expression,
    # font=('Helvetica 25'),
    )
# InputField.config(highlightthickness=1, highlightbackground="black")
# InputField.grid(column=0, row=0, columnspan=4)
InputField.grid(column=0, row=0, columnspan=3, padx=5, pady=15)

btnFrame = Frame(window)
btnFrame.grid(column=0, row=1, columnspan=4, rowspan=5)

for c in range(0, 4):
    for r in range(0, 4):
        Button(btnFrame, text=c, width=10, height=4).grid(column=c, row=r, padx=2, pady=2)

# InputBtn_Frame = Frame(window).grid()





window.mainloop()