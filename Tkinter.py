# Coded By Chance

# Import Packages
from sympy.solvers import solve        
from sympy.core.symbol import symbols 
import math
from math import log, radians
import random
import tkinter as tk
from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create Window
window = tk.Tk()

# Window properties
window.resizable(False, False)     # user can't resize window
window.attributes("-alpha", 1)     # window's transparency 
window.attributes("-topmost", 1)   # Window stacking
window.title("Calculator")         # Title

window.configure(background="black")         # Backgroung Colors
window.iconbitmap("calculator.ico")          # Set Icon


# Create Style for ttk widgets
style = ttk.Style()

# Set Theme
style.theme_use("default")

# Set background color for ttkFrame
style.configure("FrameMain.TFrame", background="black")
style.configure("FrameBtn.TFrame", background="black")

# Set ttkEntry color
style.configure("InputField.TEntry", fieldbackground="black", foreground="white", insertcolor="white")

# Number Button Style
style.configure("num.TButton", foreground="white", background="#0d0d0d", borderwidth=2, relief=RAISED)
style.map("num.TButton",
    foreground=[('pressed', 'white'), ('active', 'white')],
    background=[('pressed', 'grey0'), ('active', 'grey')]
    )

# Function button style
style.configure("Function.TButton", foreground="white", background="#363636", borderwidth=2, relief=RAISED)
style.map("Function.TButton",
    foreground=[('pressed', 'white'), ('active', 'white')],
    background=[('pressed', 'grey0'), ('active', 'grey')]
    )

# Set Frame Position and apply style
mainFrame = ttk.Frame(window, style="FrameMain.TFrame")
mainFrame.grid(column=0, row=0)

# Frame for all buttons
btnFrame = ttk.Frame(mainFrame, style="FrameBtn.TFrame")
btnFrame.grid(column=0, row=1)

# Global Virable 
expression = StringVar() # Store entry value
history = []  # Store History

# Create Entry widget
InputField = ttk.Entry(
    mainFrame, 
    textvariable=expression,
    style="InputField.TEntry",
    font=("Helvetica 25"),
    )
# Assign Position
InputField.grid(column=0, row=0, padx=10, pady=20)

# Helper Function

def inputExpression(value):    # Button Input
    expression.set(expression.get()+value)

def calculate(expressionIn):   # Calculate expression
    ans = "Unknown"

    # Error Handling
    try:
        eval(expressionIn)
    except ZeroDivisionError:
        ans = "Zero Division Error"
    except SyntaxError:
        ans = "Syntax Error"
    except NameError:
        ans = "Invaild Input"
    else:
        ans = eval(expressionIn)

    # Show result
    expression.set(ans)

    # Add both expression and answer to history
    history.append(str(len(history)) + " --> " + str(expressionIn) + " = " + str(ans))

# Allow User use "Enter" to calculate
def calculateEnter(event):
    calculate(expression.get())

# Clear entry field
def clearAll():
    expression.set("")

# Backspace function
def backSpace():
    expression.set((expression.get())[:-1])

# Save history to a txt file
def saveHistory():
    with open("Calaulator-History.txt", "w") as f:
        for i in history:
            f.write(i)
            f.write("\n")

# Button style changing function 
def changeBtnRelief(styleChoose):
    style = ttk.Style()
    style.configure("num.TButton", relief=styleChoose)
    style.configure("Function.TButton", relief=styleChoose)

# Window -alpha changing function
def changeAlpha(a):
    window.attributes("-alpha", a)

# Theme changing function 
def changeTheme(themeChoose):
    style = ttk.Style()
    style.theme_use(themeChoose)

# Sin Cos and Tan, using math package
def SIN(x):
    return math.sin(math.radians(x))

def COS(x):
    return math.cos(math.radians(x))

def TAN(x):
    return math.tan(math.radians(x))

# Round Value function 
def Round():
    calculate(expression.get()) # Prevent rounding expression
    num = expression.get()
    expression.set(round(eval(num),2))

# Check expression, use in Plot()
def check(b:list, a:str) -> bool:
    for i in b:
        if i in a:
            return True
    return False


# Create menu bar
menuBar = Menu(window)
window.config(menu=menuBar)
#Three main menu - File, Style, Math
fileMenu = Menu(menuBar, tearoff=False, background="white", activebackground="grey")
StyleMenu = Menu(menuBar, tearoff=False, background="white", activebackground="grey")
MathMenu = Menu(menuBar, tearoff=False, background="white", activebackground="grey")

# Sub menu in "Style"
subMenuBtn = Menu(StyleMenu, tearoff=0)
subMenuAlpha = Menu(StyleMenu, tearoff=0)
subMenuTheme = Menu(StyleMenu, tearoff=0)

# Add three main menu to the menu bar
menuBar.add_cascade( label="File", menu=fileMenu, underline=0)
menuBar.add_cascade( label="Style", menu=StyleMenu, underline=0)
menuBar.add_cascade( label="Math", menu=MathMenu, underline=0)

# File menu element
fileMenu.add_command( label="Save History", command=saveHistory,)
fileMenu.add_separator()
fileMenu.add_command( label="Exit", command=window.destroy,)

# Style menu element with three sub menu contain 16 option total
StyleMenu.add_cascade( label="Button Style", menu=subMenuBtn,)

# Element under Button Style
subMenuBtn.add_command( label="Rsised", command=lambda:changeBtnRelief(RAISED),)
subMenuBtn.add_command( label="Flat", command=lambda:changeBtnRelief(FLAT),)
subMenuBtn.add_command( label="Sunken", command=lambda:changeBtnRelief(SUNKEN),)
subMenuBtn.add_command( label="Groove", command=lambda:changeBtnRelief(GROOVE),)
subMenuBtn.add_command( label="Ridge", command=lambda:changeBtnRelief(RIDGE),)

StyleMenu.add_cascade( label="Alpha", menu=subMenuAlpha,)

# Element under Alpha
subMenuAlpha.add_command(label="Alpha 1", command=lambda:changeAlpha(1))
subMenuAlpha.add_command(label="Alpha 0.9", command=lambda:changeAlpha(0.9))
subMenuAlpha.add_command(label="Alpha 0.5", command=lambda:changeAlpha(0.5))
subMenuAlpha.add_command(label="Alpha 0.1", command=lambda:changeAlpha(0.1))

StyleMenu.add_cascade( label="Theme", menu=subMenuTheme,)

# Element under Theme
subMenuTheme.add_command(label="Winnative", command=lambda:changeTheme("winnative"))
subMenuTheme.add_command(label="Clam", command=lambda:changeTheme("clam"))
subMenuTheme.add_command(label="Alt", command=lambda:changeTheme("alt"))
subMenuTheme.add_command(label="Default", command=lambda:changeTheme("default"))
subMenuTheme.add_command(label="Classic", command=lambda:changeTheme("classic"))
subMenuTheme.add_command(label="Vista", command=lambda:changeTheme("vista"))
subMenuTheme.add_command(label="Xpnative", command=lambda:changeTheme("xpnative"))

# Element under Math 
MathMenu.add_command(label="Log(x, Base)", command=lambda:inputExpression("log("))
MathMenu.add_command(label="Round", command=Round)

# Plot() use to creat graph of function
def plot(expressionIn):

    # Creat new window for graph
    graphWindow = Toplevel(window)
    graphWindow.title(f"Graph of {expressionIn}")
    graphWindow.attributes("-topmost", 1)

    # Plot doesn't support sin cos and tan due to package conflict
    notAllow=["SIN", "COS", "TAN"]
    if (check(notAllow, expressionIn)):
        graphWindow.destroy()
        expression.set("Function not supported")

    # Set figure size
    fig = Figure(figsize = (4, 4))

    # Varibles used to store points and roots
    y_res = []
    x_res = []

    x_root=[]
    y_root=[]

    # Roots container 
    rootValue = ""

    # Ploting, passing x value frome -100.00 - 100.00
    for j in range (-10000, 10001):
        x = j/100
        
        # Try calculate y value
        try:
            eval(expressionIn[5:])
        except:
            # If can't calculate, skip to next value
            continue
        else:
            y = eval(expressionIn[5:])
        
        # Add coordinates to the list for future ploting
        x_res.append(x)
        y_res.append(y)

    # Calculate the roots, can't calcuate the roots for log(x) -- Packages Conflict
    if "log" not in expressionIn:
        x = symbols("x")
        expre = eval(expressionIn[5:])
        sol = solve(expre)

        # Store the coordinate for root
        for i in range(len(sol)):

            rootValue += (f"X{i+1} = {sol[i]}   ")
            x_root.append(sol[i])
            y_root.append(0)


    # Graph properties
    graph = fig.add_subplot(111) # Graph shape
    graph.grid(True) # Show Grid

    # Set lable on graph
    graph.tick_params(axis="both", labelsize=6)
    graph.set_title(label=f"{expressionIn}")
    # Set the limit of graph
    graph.set_xlim([-15, 15])
    graph.set_ylim([-15, 15])

    # Dashed line showes x and y axis
    graph.axhline(0, color="black", alpha=0.7, linestyle = "--")
    graph.axvline(0, color="black", alpha=0.7, linestyle = "--")
    # Create lable shows the root
    graph.set_xlabel(rootValue)
    
    # Plot points on the graph and add legend
    graph.plot(x_res,y_res, label=f"{expressionIn}")
    graph.legend(loc="upper left")

    # Plot the root on the graph
    graph.scatter(x_root, y_root, color="red")

    # Draw graph on ttk canvas
    canvas = FigureCanvasTkAgg(fig, master = graphWindow)
    canvas.draw()

    # Save graph function 
    def saveImagePNG():
        graph.figure.savefig(f"{random.randint(1,1000)}.png")
    
    def saveImagePDF():
        graph.figure.savefig(f"{random.randint(1,1000)}.pdf")

    # Creat menu bar on the new window
    menuBar_sub = Menu(graphWindow)
    graphWindow.config(menu=menuBar_sub)
    fileMenu_Sub = Menu(menuBar_sub, tearoff=False, background="white", activebackground="grey")
    fileMenu_Sub.add_command(label="Save as PNG", command=saveImagePNG)
    fileMenu_Sub.add_command(label="Save as PDF", command=saveImagePDF)
    menuBar_sub.add_cascade(label="File", menu=fileMenu_Sub)
    canvas.get_tk_widget().pack()

# Allow user use Enter Key to calculate
window.bind("<Return>", calculateEnter)

# Add all the buttons to the window

# Function buttons
btnClearAll = ttk.Button(btnFrame, text="CA", width=10, takefocus=False, style="Function.TButton", command=clearAll).grid(column=0, row=0, padx=5, pady=10)
btn2BackSpace = ttk.Button(btnFrame, text="B", width=10, takefocus=False, style="Function.TButton", command=backSpace).grid(column=1, row=0, padx=5, pady=10)
btnBracketR = ttk.Button(btnFrame, text="(", width=10, takefocus=False, style="Function.TButton", command=lambda:inputExpression("(")).grid(column=2, row=0, padx=5, pady=10)
btn4BracketL = ttk.Button(btnFrame, text=")", width=10, takefocus=False, style="Function.TButton", command=lambda:inputExpression(")")).grid(column=3, row=0, padx=5, pady=10)

# Number buttons 0-9
btn1 = ttk.Button(btnFrame, text="1", width=10, takefocus=False, style="num.TButton", command=lambda:inputExpression("1")).grid(column=0, row=3, padx=5, pady=10)
btn2 = ttk.Button(btnFrame, text="2", width=10, takefocus=False, style="num.TButton", command=lambda:inputExpression("2")).grid(column=1, row=3, padx=5, pady=10)
btn3 = ttk.Button(btnFrame, text="3", width=10, takefocus=False, style="num.TButton", command=lambda:inputExpression("3")).grid(column=2, row=3, padx=5, pady=10)

btn4 = ttk.Button(btnFrame, text="4", width=10, takefocus=False, style="num.TButton", command=lambda:inputExpression("4")).grid(column=0, row=2, padx=5, pady=10)
btn5 = ttk.Button(btnFrame, text="5", width=10, takefocus=False, style="num.TButton", command=lambda:inputExpression("5")).grid(column=1, row=2, padx=5, pady=10)
btn6 = ttk.Button(btnFrame, text="6", width=10, takefocus=False, style="num.TButton", command=lambda:inputExpression("6")).grid(column=2, row=2, padx=5, pady=10)

btn7 = ttk.Button(btnFrame, text="7", width=10, takefocus=False, style="num.TButton", command=lambda:inputExpression("7")).grid(column=0, row=1, padx=5, pady=10)
btn8 = ttk.Button(btnFrame, text="8", width=10, takefocus=False, style="num.TButton", command=lambda:inputExpression("8")).grid(column=1, row=1, padx=5, pady=10)
btn9 = ttk.Button(btnFrame, text="9", width=10, takefocus=False, style="num.TButton", command=lambda:inputExpression("9")).grid(column=2, row=1, padx=5, pady=10)
btn0 = ttk.Button(btnFrame, text="0", width=10, takefocus=False, style="num.TButton", command=lambda:inputExpression("0")).grid(column=1, row=4, padx=5, pady=10)

# Other function buttons
btnPlus = ttk.Button(btnFrame, text="+", width=10, takefocus=False, style="Function.TButton", command=lambda:inputExpression("+")).grid(column=3, row=3, padx=5, pady=10)
btnSubtrack = ttk.Button(btnFrame, text="-", width=10, takefocus=False, style="Function.TButton", command=lambda:inputExpression("-")).grid(column=3, row=2, padx=5, pady=10)
btnMultiply = ttk.Button(btnFrame, text="X", width=10, takefocus=False, style="Function.TButton", command=lambda:inputExpression("*")).grid(column=3, row=1, padx=5, pady=10)
btnDevide = ttk.Button(btnFrame, text="/", width=10, takefocus=False, style="Function.TButton", command=lambda:inputExpression("/")).grid(column=3, row=4, padx=5, pady=10)
btnEqual = ttk.Button(btnFrame, text="=", width=10, takefocus=False, style="Function.TButton", command=lambda:calculate(expression.get())).grid(column=2, row=4, padx=5, pady=10)
btnDot = ttk.Button(btnFrame, text=".", width=10, takefocus=False, style="Function.TButton", command=lambda:inputExpression(".")).grid(column=0, row=4, padx=5, pady=10)

btn = ttk.Button(btnFrame, text="F(x)", width=10, takefocus=False, style="Function.TButton", command=lambda:inputExpression("F(x)=")).grid(column=0, row=5, padx=5, pady=10)
btn = ttk.Button(btnFrame, text="X,T,θ,N", width=10, takefocus=False, style="Function.TButton", command=lambda:inputExpression("x")).grid(column=1, row=5, padx=5, pady=10)
btn = ttk.Button(btnFrame, text="Graph", width=10, takefocus=False, style="Function.TButton", command=lambda:plot(expression.get())).grid(column=2, row=5, padx=5, pady=10)
btn = ttk.Button(btnFrame, text="^", width=10, takefocus=False, style="Function.TButton", command=lambda:inputExpression("**")).grid(column=3, row=5, padx=5, pady=10)

btn = ttk.Button(btnFrame, text=",", width=10, takefocus=False, style="Function.TButton", command=lambda:inputExpression(",")).grid(column=0, row=6, padx=5, pady=10)
btn = ttk.Button(btnFrame, text="Sin", width=10, takefocus=False, style="Function.TButton", command=lambda:inputExpression("SIN(")).grid(column=1, row=6, padx=5, pady=10)
btn = ttk.Button(btnFrame, text="Cos", width=10, takefocus=False, style="Function.TButton", command=lambda:inputExpression("COS(")).grid(column=2, row=6, padx=5, pady=10)
btn = ttk.Button(btnFrame, text="Tan", width=10, takefocus=False, style="Function.TButton", command=lambda:inputExpression("TAN(")).grid(column=3, row=6, padx=5, pady=10)

# Keep the window running
window.mainloop()
#END