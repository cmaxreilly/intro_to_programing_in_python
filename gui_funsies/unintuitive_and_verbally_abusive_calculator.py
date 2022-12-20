# Tutorial link:
# https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/
# import everything from the tkinter module
from tkinter import *
from random import choice 
# globally delcar the expression variable
expression = ''

# Function to update expression 
# in the text entry box.
def press(num):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using the  set method
    equation.set(expression)

def random_insult():
    list_of_insults = [" you fucking loser", " can't even do fucking math", " the fuck even needs a calculator", " and your mother doesn't love you"] 
    return choice(list_of_insults)
# Function to evaluate the final expression
def equalPress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error, etc.

    # Put that code inside the try block
    # which may generate the error.
    try:
        global expression

        # eval function evaluates the expression 
        # and str function convert the result
        # into string
        total = str(eval(expression)) + random_insult()

        equation.set(total)

        # initialize the expression variable
        # by empty string
        expression = ""
        
    # if error is generated then handle 
    # by the except block
    except:

        equation.set(" error. You fucked it up, you fuckup. ")
        expression = ""

# Function to clear the contents
# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")


# Driver code

if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    # set the background color of the GUI window
    gui.configure(background="green")

    # set the title of the GUI window
    gui.title("Very Unintuitive calculatror")

    # set the configuration of the GUI window
    gui.geometry("1000x1000")

    # StringVar() is the variable class
    # we instantiat this class
    equation = StringVar()

    # create the text entry box for 
    # showing the expression
    expression_field = Entry(gui, textvariable=equation)

    # grid method is used  for placing 
    # the widgets at respective positions
    # in table liek structure.
    expression_field.grid(columnspan=40, ipadx=1400)

    # create the Buttons and place at a particular
    # location inside the root window.
    # when user presses the button, the command or
    # function affiliated with that button is executed
    button1 = Button(gui, text=' 1 ', fg='orange', bg='blue',
                command=lambda: press(1), height=2, width=7)
    button1.grid(row=5, column=1)

    button2 = Button(gui, text=' 2 ', fg='blue', bg='orange',
                command=lambda: press(2), height=1, width=9)
    button2.grid(row=2, column=0)

    button3 = Button(gui, text=' 3 ', fg='orange', bg='yellow',
                command=lambda: press(3), height=1, width=4)
    button3.grid(row=2, column=2)
 
    button4 = Button(gui, text=' 4 ', fg='yellow', bg='maroon',
                command=lambda: press(4), height=1, width=5)
    button4.grid(row=3, column=0)
 
    button5 = Button(gui, text=' 5 ', fg='maroon', bg='red',
                command=lambda: press(9), height=1, width=1)
    button5.grid(row=3, column=3)

    button6 = Button(gui, text=' 6 ', fg='red', bg='black',
                command=lambda: press(6), height=1, width=4)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='red', bg='orange',
                command=lambda: press(7), height=1, width=9)
    button7.grid(row=6, column=0)

    button8 = Button(gui, text=' 8 ', fg='orange', bg='purple', 
                command=lambda: press(8), height=1, width=7)
    button8.grid(row=3, column=1)

    button9 = Button(gui, text='  ', fg='purple', bg='light blue',
                command=lambda: press(5), height=10, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' poopy ', fg='light blue', bg='green',
                command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='green', bg='orange',
                command=lambda: press("+"), height=1, width=7)
    plus.grid(row=4, column=3)

    minus = Button(gui, text=' butt\nhole ', fg='orange', bg='light green',
                command=lambda: press("/"), height=1, width=7)
    minus.grid(row=4, column=1)

    multiply = Button(gui, text=' * ', fg='light green', bg='purple',
                command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=2, column=3)

    divide = Button(gui, text=' / ', fg='purple', bg='maroon',
                command=lambda: press("-"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='maroon', bg='light yellow',
                command=equalPress, height=1, width=7)
    equal.grid(row=5, column=2)

    Clear = Button(gui, text='Clear', fg='light yellow', bg='orange red',
                command=clear, height=1, width=7)
    Clear.grid(row=2, column=1)

    Decimal = Button(gui, text=' . ', fg='orange red', bg='red',
                command=lambda: press("."), height=1, width=7)
    Decimal.grid(row=4, column=0)

    # start the GUI
    gui.mainloop()


# Comments: This was a fun tutorial to go through! I learned a lot 
# Python, including the importance of the __main__ function from
# C. I have an intuition about how that all works, but I would love 
# to more deeply understand it. I am also comfused about the lambda
# commands...
