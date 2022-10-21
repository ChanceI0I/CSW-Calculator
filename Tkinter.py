
import random
import tkinter as tk
from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from sympy import symbols, solve
# from scipy.optimize import fsolve


window = tk.Tk()

window.resizable(False, False)
window.attributes("-alpha", 1)     # window's transparency 
window.attributes("-topmost", 1)   # Window stacking
window.title("Calculator")         # Title

window.configure(background="black")         # Backgroung Colors
window.iconbitmap("calculator.ico")  # Set Icon


style = ttk.Style()
style.theme_use("default")

style.configure("FrameMain.TFrame", background="black")
style.configure("FrameBtn.TFrame", background="black")

style.configure("InputField.TEntry", fieldbackground="black", foreground="white", insertcolor="white")

style.configure("num.TButton", foreground="white", background="#0d0d0d", borderwidth=2, relief=RAISED)
style.map("num.TButton",
    foreground=[('pressed', 'white'), ('active', 'white')],
    background=[('pressed', 'grey0'), ('active', 'grey')]
    )

style.configure("Function.TButton", foreground="white", background="#363636", borderwidth=2, relief=RAISED)
style.map("Function.TButton",
    foreground=[('pressed', 'white'), ('active', 'white')],
    background=[('pressed', 'grey0'), ('active', 'grey')]
    )



mainFrame = ttk.Frame(window, style="FrameMain.TFrame")
mainFrame.grid(column=0, row=0)

btnFrame = ttk.Frame(mainFrame, style="FrameBtn.TFrame")
btnFrame.grid(column=0, row=1)


expression = StringVar()
history = []

InputField = ttk.Entry(
    mainFrame, 
    textvariable=expression,
    style="InputField.TEntry",
    font=("Helvetica 25"),
    )

InputField.grid(column=0, row=0, padx=10, pady=20)


def inputExpression(value):
    expression.set(expression.get()+value)

def calculate(expressionIn):

    ans = "Unknown"

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

    expression.set(ans)

    history.append(str(len(history)) + " --> " + str(expressionIn) + " = " + str(ans))

def calculateEnter(event):
    calculate(expression.get())

def clearAll():
    expression.set("")

def backSpace():
    expression.set((expression.get())[:-1])

def saveHistory():
    with open("Calaulator-History.txt", "w") as f:
        for i in history:
            f.write(i)
            f.write("\n")

def changeBtnRelief(styleChoose):
    style = ttk.Style()
    style.configure("num.TButton", relief=styleChoose)
    style.configure("Function.TButton", relief=styleChoose)

def changeAlpha(a):
    window.attributes("-alpha", a)

def changeTheme(themeChoose):
    style = ttk.Style()
    style.theme_use(themeChoose)


menuBar = Menu(window)
window.config(menu=menuBar)
fileMenu = Menu(menuBar, tearoff=False, background="white", activebackground="grey")
StyleMenu = Menu(menuBar, tearoff=False, background="white", activebackground="grey")
subMenuBtn = Menu(StyleMenu, tearoff=0)
subMenuAlpha = Menu(StyleMenu, tearoff=0)
subMenuTheme = Menu(StyleMenu, tearoff=0)

fileMenu.add_command( label="Save History", command=saveHistory,)
fileMenu.add_separator()
fileMenu.add_command( label="Exit", command=window.destroy,)


menuBar.add_cascade( label="File", menu=fileMenu, underline=0)
menuBar.add_cascade( label="Style", menu=StyleMenu, underline=0)

StyleMenu.add_cascade( label="Button Style", menu=subMenuBtn,)

subMenuBtn.add_command( label="Rsised", command=lambda:changeBtnRelief(RAISED),)
subMenuBtn.add_command( label="Flat", command=lambda:changeBtnRelief(FLAT),)
subMenuBtn.add_command( label="Sunken", command=lambda:changeBtnRelief(SUNKEN),)
subMenuBtn.add_command( label="Groove", command=lambda:changeBtnRelief(GROOVE),)
subMenuBtn.add_command( label="Ridge", command=lambda:changeBtnRelief(RIDGE),)

StyleMenu.add_cascade( label="Alpha", menu=subMenuAlpha,)

subMenuAlpha.add_command(label="Alpha 1", command=lambda:changeAlpha(1))
subMenuAlpha.add_command(label="Alpha 0.9", command=lambda:changeAlpha(0.9))
subMenuAlpha.add_command(label="Alpha 0.5", command=lambda:changeAlpha(0.5))
subMenuAlpha.add_command(label="Alpha 0.1", command=lambda:changeAlpha(0.1))

StyleMenu.add_cascade( label="Theme", menu=subMenuTheme,)

subMenuTheme.add_command(label="Winnative", command=lambda:changeTheme("winnative"))
subMenuTheme.add_command(label="Clam", command=lambda:changeTheme("clam"))
subMenuTheme.add_command(label="Alt", command=lambda:changeTheme("alt"))
subMenuTheme.add_command(label="Default", command=lambda:changeTheme("default"))
subMenuTheme.add_command(label="Classic", command=lambda:changeTheme("classic"))
subMenuTheme.add_command(label="Vista", command=lambda:changeTheme("vista"))
subMenuTheme.add_command(label="Xpnative", command=lambda:changeTheme("xpnative"))


def plot(expressionIn):
    graphWindow = Toplevel(window)
    graphWindow.title(f"Graph of {expressionIn}")
    graphWindow.attributes("-topmost", 1)

    fig = Figure(figsize = (4, 4))
    y_res = []
    x_res = []

    x_root=[]
    y_root=[]

    rootValue = ""

    for j in range (-10000, 10001):
        x = j/100
        
        try:
            eval(expressionIn[5:])
        except:
            continue
        else:
            y = eval(expressionIn[5:])
        
        x_res.append(x)
        y_res.append(y)
    
    x = symbols("x")
    expre = eval(expressionIn[5:])
    sol = solve(expre)
    # print(sol)
    for i in range(len(sol)):
        # ttk.Label(graphWindow, text= f"X{i+1}:{sol[i]}").pack()
        rootValue += (f"X{i+1} = {sol[i]}   ")
        x_root.append(sol[i])
        y_root.append(0)

    


    # if min(y_res) <= 0 and max(y_res) >= 0:
    #     list = [abs(i) for i in y_res]
    #     minY = (min(list))
    #     for element in y_res:
            
    #         if abs(element) == minY:
    #             # print(element, minY)
    #             index = y_res.index(element)
    #             root_x.append(x_res[index])
    #             root_y.append(0)

    # f = lambda x: eval(expressionIn[5:])
    # # fsolve(f, [-100, 100])
    # print(fsolve(f, [-100, 100]))


    graph = fig.add_subplot(111)
    graph.grid(True)
    graph.tick_params(axis="both", labelsize=6)
    graph.set_title(label=f"{expressionIn}")
    graph.set_xlim([-20, 20])
    graph.set_ylim([-20, 20])
    graph.axhline(0, color="black", alpha=0.7, linestyle = "--")
    graph.axvline(0, color="black", alpha=0.7, linestyle = "--")
    graph.set_xlabel(rootValue)
    
    graph.plot(x_res,y_res)
    graph.scatter(x_root, y_root, color="red")

    canvas = FigureCanvasTkAgg(fig, master = graphWindow)
    canvas.draw()

    def saveImagePNG():
        graph.figure.savefig(f"{random.randint(1,1000)}.png")
        # print("save as png")
    
    def saveImagePDF():
        graph.figure.savefig(f"{random.randint(1,1000)}.pdf")
        # print("save as pdf")

    menuBar_sub = Menu(graphWindow)
    graphWindow.config(menu=menuBar_sub)
    fileMenu_Sub = Menu(menuBar_sub, tearoff=False, background="white", activebackground="grey")
    fileMenu_Sub.add_command(label="Save as PNG", command=saveImagePNG)
    fileMenu_Sub.add_command(label="Save as PDF", command=saveImagePDF)
    menuBar_sub.add_cascade(label="File", menu=fileMenu_Sub)

    

    canvas.get_tk_widget().pack()

window.bind("<Return>", calculateEnter)

btnClearAll = ttk.Button(btnFrame, text="CA", width=10, takefocus=False, style="Function.TButton", command=clearAll).grid(column=0, row=0, padx=5, pady=10)
btn2BackSpace = ttk.Button(btnFrame, text="B", width=10, takefocus=False, style="Function.TButton", command=backSpace).grid(column=1, row=0, padx=5, pady=10)
btnBracketR = ttk.Button(btnFrame, text="(", width=10, takefocus=False, style="Function.TButton", command=lambda:inputExpression("(")).grid(column=2, row=0, padx=5, pady=10)
btn4BracketL = ttk.Button(btnFrame, text=")", width=10, takefocus=False, style="Function.TButton", command=lambda:inputExpression(")")).grid(column=3, row=0, padx=5, pady=10)


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
btnPlus = ttk.Button(btnFrame, text="+", width=10, takefocus=False, style="Function.TButton", command=lambda:inputExpression("+")).grid(column=3, row=3, padx=5, pady=10)
btnSubtrack = ttk.Button(btnFrame, text="-", width=10, takefocus=False, style="Function.TButton", command=lambda:inputExpression("-")).grid(column=3, row=2, padx=5, pady=10)
btnMultiply = ttk.Button(btnFrame, text="*", width=10, takefocus=False, style="Function.TButton", command=lambda:inputExpression("*")).grid(column=3, row=1, padx=5, pady=10)
btnDevide = ttk.Button(btnFrame, text="/", width=10, takefocus=False, style="Function.TButton", command=lambda:inputExpression("/")).grid(column=3, row=4, padx=5, pady=10)
btnEqual = ttk.Button(btnFrame, text="=", width=10, takefocus=False, style="Function.TButton", command=lambda:calculate(expression.get())).grid(column=2, row=4, padx=5, pady=10)
btnDot = ttk.Button(btnFrame, text=".", width=10, takefocus=False, style="Function.TButton", command=lambda:inputExpression(".")).grid(column=0, row=4, padx=5, pady=10)

btn = ttk.Button(btnFrame, text="F(x)", width=10, takefocus=False, style="Function.TButton", command=lambda:inputExpression("F(x)=")).grid(column=0, row=5, padx=5, pady=10)
btn = ttk.Button(btnFrame, text="X", width=10, takefocus=False, style="Function.TButton", command=lambda:inputExpression("x")).grid(column=1, row=5, padx=5, pady=10)
btn = ttk.Button(btnFrame, text="Graph", width=10, takefocus=False, style="Function.TButton", command=lambda:plot(expression.get())).grid(column=2, row=5, padx=5, pady=10)
btn = ttk.Button(btnFrame, text="^", width=10, takefocus=False, style="Function.TButton", command=lambda:inputExpression("**")).grid(column=3, row=5, padx=5, pady=10)

window.mainloop()