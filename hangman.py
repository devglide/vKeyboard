from tkinter import *

root = Tk()
root.geometry('900x400+1500+300')

def select(value):
    guess = value
    print(guess)


butt = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 'clear', 'enter']

# left = Frame(root).pack(side=LEFT)
# right = Frame(root).pack(side=RIGHT)

# lab = Label(right, text='', bg='red').grid(row=0, columnspan=1)

# li = Label(root, text="left", font=('Times',78)).grid(row=2, column=0)

varRow = 2
varColumn = 0

for button in butt:
    command = lambda x=button: select(x)
    if butt != "clear" and butt != "enter":
        Button(root, text=button, width=5, padx=4, pady=4, command = command).grid(row=varRow, column=varColumn)
    if butt == "clear":
        Button(root, text=button, width=5, padx=4, pady=4, command = command).grid(row=varRow, column=varColumn)
    if butt == "return":
        Button(root, text=button, width=5, padx=4, pady=4, command = command).grid(row=varRow, column=varColumn)



    varColumn += 1
    if varColumn > 4 and varRow == 2:
        varColumn = 0
        varRow += 1
    if varColumn > 4 and varRow == 3:
        varColumn = 0
        varRow += 1
    if varColumn > 4 and varRow == 4:
        varColumn = 0
        varRow += 1
    if varColumn > 4 and varRow == 5:
        varColumn = 0
        varRow += 1
    if varColumn > 4 and varRow == 6:
        varColumn = 0
        varRow += 1


root.mainloop()