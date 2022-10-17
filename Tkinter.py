import tkinter as tk
from tkinter import *
from tkinter import ttk

# from ctypes import windll                         #Apply when blur
# windll.shcore.SetProcessDpiAwareness(1)

window = tk.Tk()

window.resizable(False, False)
window.attributes("-alpha", 1)     # window's transparency 
window.attributes("-topmost", 1)   # Window stacking
window.title("Calculator")         # Title
# window.geometry("270x350")       # size
# window.config(bg="blue")         # Backgroung Colors

style = ttk.Style()
style.configure("FrameMain", background="red")
style.configure("FrameBtn", background="yellow")
style.configure("Input", bg="black")
style.theme_use("xpnative")
style.configure("num", bg="purple")


# window.columnconfigure(index=0, weight=1)
# window.columnconfigure(index=1, weight=1)
# window.columnconfigure(index=2, weight=1)
# window.columnconfigure(index=3, weight=1)
mainFrame = ttk.Frame(window, borderwidth=1, style="FrameMain.TFrame")
mainFrame.grid(column=0, row=0)

btnFrame = ttk.Frame(mainFrame, style="FrameBtn.TFrame")
btnFrame.grid(column=0, row=1)

# window.iconbitmap("C:/Users/Cheng/Desktop/Tkinter Calculator/calculator.ico")  # Set Icon


expression = StringVar()

InputField = ttk.Entry(
    mainFrame, 
    #width=13,
    # foreground="black", 
    # background="green", 
    textvariable=expression,
    style="Input.TEntry"
    # font=('Helvetica 25'),
    )
# InputField.config(highlightthickness=1, highlightbackground="black")
# InputField.grid(column=0, row=0, columnspan=4)
InputField.grid(column=0, row=0, columnspan=4)



for c in range(0, 4):
    for r in range(0, 4):
        ttk.Button(btnFrame, text=c, width=5, style="num.TButton").grid(column=c, row=r, padx=2, pady=5)

# InputBtn_Frame = ttk.Frame(window).grid()


# print(btnFrame.winfo_width(), InputField.winfo_width())


window.mainloop()