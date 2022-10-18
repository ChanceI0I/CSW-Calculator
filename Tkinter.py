import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font

# from ctypes import windll                         #Apply when blur
# windll.shcore.SetProcessDpiAwareness(1)

window = tk.Tk()

window.resizable(False, False)
window.attributes("-alpha", 1)     # window's transparency 
window.attributes("-topmost", 1)   # Window stacking
window.title("Calculator")         # Title
# window.geometry("270x350")       # size
window.configure(background="black")         # Backgroung Colors

style = ttk.Style()
style.theme_use("default")

style.configure("FrameMain.TFrame", background="black")
style.configure("FrameBtn.TFrame", background="black")

style.configure("InputField.TEntry", fieldbackground="black", foreground="white", )

style.configure("num.TButton", foreground="white", background="black")
style.map("num.TButton",
    foreground=[('pressed', 'white'), ('active', 'white')],
    background=[('pressed', 'grey0'), ('active', 'grey')]
    )

print(style.theme_names())


mainFrame = ttk.Frame(window, style="FrameMain.TFrame")
mainFrame.grid(column=0, row=0)

btnFrame = ttk.Frame(mainFrame, style="FrameBtn.TFrame")
btnFrame.grid(column=0, row=1)



# window.iconbitmap("C:/Users/Cheng/Desktop/Tkinter Calculator/calculator.ico")  # Set Icon


expression = StringVar()

InputField = ttk.Entry(
    mainFrame, 
    textvariable=expression,
    style="InputField.TEntry",
    font=("Helvetica 25")
    )

InputField.grid(column=0, row=0, padx=10, pady=20)



# for c in range(0, 4):
#     for r in range(0, 4):
#         ttk.Button(btnFrame, text=c, width=10, style="num.TButton").grid(column=c, row=r, padx=5, pady=10)

def inputExpression(value):
    expression.set(expression.get()+value)

def calculate(expressionIn):
    ans = eval(expressionIn)
    expression.set(ans)

def clearAll():
    expression.set("")

def backSpace():
    expression.set((expression.get())[:-1])


btnClearAll = ttk.Button(btnFrame, text="CA", width=10, style="num.TButton", command=clearAll).grid(column=0, row=0, padx=5, pady=10)
btn2BackSpace = ttk.Button(btnFrame, text="B", width=10, style="num.TButton", command=backSpace).grid(column=1, row=0, padx=5, pady=10)
btnBracketR = ttk.Button(btnFrame, text="(", width=10, style="num.TButton", command=lambda:inputExpression("(")).grid(column=2, row=0, padx=5, pady=10)
btn4BracketL = ttk.Button(btnFrame, text=")", width=10, style="num.TButton", command=lambda:inputExpression(")")).grid(column=3, row=0, padx=5, pady=10)

btn1 = ttk.Button(btnFrame, text="1", width=10, style="num.TButton", command=lambda:inputExpression("1")).grid(column=0, row=1, padx=5, pady=10)
btn2 = ttk.Button(btnFrame, text="2", width=10, style="num.TButton", command=lambda:inputExpression("2")).grid(column=1, row=1, padx=5, pady=10)
btn3 = ttk.Button(btnFrame, text="3", width=10, style="num.TButton", command=lambda:inputExpression("3")).grid(column=2, row=1, padx=5, pady=10)
btn4 = ttk.Button(btnFrame, text="4", width=10, style="num.TButton", command=lambda:inputExpression("4")).grid(column=0, row=2, padx=5, pady=10)
btn5 = ttk.Button(btnFrame, text="5", width=10, style="num.TButton", command=lambda:inputExpression("5")).grid(column=1, row=2, padx=5, pady=10)
btn6 = ttk.Button(btnFrame, text="6", width=10, style="num.TButton", command=lambda:inputExpression("6")).grid(column=2, row=2, padx=5, pady=10)
btn7 = ttk.Button(btnFrame, text="7", width=10, style="num.TButton", command=lambda:inputExpression("7")).grid(column=0, row=3, padx=5, pady=10)
btn8 = ttk.Button(btnFrame, text="8", width=10, style="num.TButton", command=lambda:inputExpression("8")).grid(column=1, row=3, padx=5, pady=10)
btn9 = ttk.Button(btnFrame, text="9", width=10, style="num.TButton", command=lambda:inputExpression("9")).grid(column=2, row=3, padx=5, pady=10)
btn0 = ttk.Button(btnFrame, text="0", width=10, style="num.TButton", command=lambda:inputExpression("0")).grid(column=1, row=4, padx=5, pady=10)
btnPlus = ttk.Button(btnFrame, text="+", width=10, style="num.TButton", command=lambda:inputExpression("+")).grid(column=3, row=3, padx=5, pady=10)
btnSubtrack = ttk.Button(btnFrame, text="-", width=10, style="num.TButton", command=lambda:inputExpression("-")).grid(column=3, row=2, padx=5, pady=10)
btnMultiply = ttk.Button(btnFrame, text="*", width=10, style="num.TButton", command=lambda:inputExpression("*")).grid(column=3, row=1, padx=5, pady=10)
btnDevide = ttk.Button(btnFrame, text="/", width=10, style="num.TButton", command=lambda:inputExpression("/")).grid(column=3, row=4, padx=5, pady=10)
btnEqual = ttk.Button(btnFrame, text="=", width=10, style="num.TButton", command=lambda:calculate(expression.get())).grid(column=2, row=4, padx=5, pady=10)
btnDot = ttk.Button(btnFrame, text=".", width=10, style="num.TButton", command=lambda:inputExpression(".")).grid(column=0, row=4, padx=5, pady=10)

# InputBtn_Frame = ttk.Frame(window).grid()
# print(btnFrame.winfo_width(), InputField.winfo_width())


window.mainloop()