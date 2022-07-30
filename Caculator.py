from tkinter import *

window = Tk()  #creating the window

window.geometry("330x342") 

window.title("CALCULATOR")

expression = ""

input = StringVar()      #instance of input field

#to update the input field
def click(item):
    global expression
    expression = expression + str(item)
    input.set(expression)

#to clear the input field
def clear():   
    global expression
    expression = ""
    input.set(" ")

#to calculate the result of the expression
def equal():
    global expression
    #evalutes the string expression directly
    result = str(eval(expression)) 
    input.set(result)
    expression = ""

# creating a frame for the input field
input_frame = Frame(window, width = 312, height = 60)
input_frame.pack(side = TOP)

# creating a input field inside the 'Frame'
input_field = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input, width = 50, bg = "#eee", justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10) 

# creating another 'Frame' for the button below the 'input_frame'
btn_frame = Frame(window, width = 400, height = 200, bg = "grey")
btn_frame.pack()

# first row

clear1 = Button(btn_frame, text = "C", fg = "black", width = 34, height = 3, bg = "#eee", cursor = "hand2", command = lambda: clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)

divide = Button(btn_frame, text = "/", fg = "black", width = 10, height = 3, bg = "#eee", cursor = "hand2", command = lambda: click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

# second row

seven = Button(btn_frame, text = "7", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command = lambda: click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)

eight = Button(btn_frame, text = "8", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command = lambda: click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)

nine = Button(btn_frame, text = "9", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command = lambda: click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)

multiply = Button(btn_frame, text = "*", fg = "black", width = 10, height = 3, bg = "#eee", cursor = "hand2", command = lambda: click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)

# third row

four = Button(btn_frame, text = "4", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command = lambda: click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)

five = Button(btn_frame, text = "5", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command = lambda: click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)

six = Button(btn_frame, text = "6", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command = lambda: click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)

minus = Button(btn_frame, text = "-", fg = "black", width = 10, height = 3, bg = "#eee", cursor = "hand2", command = lambda: click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)

# fourth row

one = Button(btn_frame, text = "1", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command = lambda: click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)

two = Button(btn_frame, text = "2", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command = lambda: click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)

three = Button(btn_frame, text = "3", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command = lambda: click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)

plus = Button(btn_frame, text = "+", fg = "black", width = 10, height = 3, bg = "#eee", cursor = "hand2", command = lambda: click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)

# fourth row

zero = Button(btn_frame, text = "0", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command = lambda: click(0)).grid(row = 4, column = 0, columnspan = 1, padx = 1, pady = 1)

mod = Button(btn_frame, text = "%", fg = "black", width = 10, height = 3, bg = "#eee", cursor = "hand2", command = lambda: click("%")).grid(row = 4, column = 1, padx = 1, pady = 1)

point = Button(btn_frame, text = ".", fg = "black", width = 10, height = 3, bg = "#eee", cursor = "hand2", command = lambda: click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)

equals = Button(btn_frame, text = "=", fg = "black", width = 10, height = 3, bg = "Royalblue2", cursor = "hand2", command = lambda: equal()).grid(row = 4, column = 3, padx = 1, pady = 1)

window.mainloop()