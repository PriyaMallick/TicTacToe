from tkinter import *
import tkinter.messagebox

main = Tk()
main.title("TIC TAC TOE")
# variables
p1_score = StringVar()
p2_score = StringVar()
ptr1 = 0
ptr2 = 0
flag = True
count = 1


# to check the value of button
def play(btn):
    global flag, count
    if btn["text"] == " " and flag == True:
        flag = False
        btn["text"] = "X"
        count += 1
        Check()
    elif btn["text"] == " " and flag == False:
        flag = True
        btn["text"] = "O"
        count += 1
        Check()
    else:
        tkinter.messagebox.showinfo("Warning", "Not allowed!")


# to clear the button values after 1 round
def ClearButton():
    b1["text"] = " "
    b2["text"] = " "
    b3["text"] = " "
    b4["text"] = " "
    b5["text"] = " "
    b6["text"] = " "
    b7["text"] = " "
    b8["text"] = " "
    b9["text"] = " "


# to check if player has won
def Check():
    global ptr1, ptr2, p1_score, p2_score, count,flag
    if (b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X' or
            b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X' or
            b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X' or
            b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X' or
            b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X' or
            b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X' or
            b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X' or
            b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X' or
            b7['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X'):
        ClearButton()
        tkinter.messagebox.showinfo("Hurray!", "Player1 wins!")
        ptr1 += 1
        count = 0
        flag = True
        p1_score.set(ptr1)

    elif (b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O' or
          b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O' or
          b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O' or
          b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O' or
          b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O' or
          b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O' or
          b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O' or
          b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O' or
          b7['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O'):
        ClearButton()
        tkinter.messagebox.showinfo("Hurray!", "Player2 wins!")
        ptr2 += 1
        count = 0
        flag = True
        p2_score.set(ptr2)

    elif (count == 0):
        tkinter.messagebox.showinfo("Oops!", "It is a Tie!")
        flag = True


# buttons
b1 = Button(main, text=" ", font="Arial", bg='yellow', fg='Black', bd=5, height=3, width=5,
            command=lambda: play(b1))
b1.grid(row=1, column=0)

b2 = Button(main, text=" ", font="Arial", bg='yellow', fg='Black', bd=5, height=3, width=5,
            command=lambda: play(b2))
b2.grid(row=1, column=1)

b3 = Button(main, text=" ", font="Arial", bg='yellow', fg='Black', bd=5, height=3, width=5,
            command=lambda: play(b3))
b3.grid(row=1, column=2)

b4 = Button(main, text=" ", font="Arial", bg='yellow', fg='Black', bd=5, height=3, width=5,
            command=lambda: play(b4))
b4.grid(row=2, column=0)

b5 = Button(main, text=" ", font="Arial", bg='yellow', fg='Black', bd=5, height=3, width=5,
            command=lambda: play(b5))
b5.grid(row=2, column=1)

b6 = Button(main, text=" ", font="Arial", bg='yellow', fg='Black', bd=5, height=3, width=5,
            command=lambda: play(b6))
b6.grid(row=2, column=2)

b7 = Button(main, text=" ", font="Arial", bg='yellow', fg='Black', bd=5, height=3, width=5,
            command=lambda: play(b7))
b7.grid(row=3, column=0)

b8 = Button(main, text=" ", font="Arial", bg='yellow', fg='Black', bd=5, height=3, width=5,
            command=lambda: play(b8))
b8.grid(row=3, column=1)

b9 = Button(main, text=" ", font="Arial", bg='yellow', fg='Black', bd=5, height=3, width=5,
            command=lambda: play(b9))
b9.grid(row=3, column=2)

label = Label(main, text="Player 1:", font='Arial', bg='green', fg='white')
label.grid(row=4,column=0,columnspan=2)
p1=Entry(main,textvariable=p1_score,bd=5,width=6)
p1.grid(row=4,column=2)

label = Label(main, text="Player 2:", font='Arial', bg='blue', fg='white')
label.grid(row=5,column=0,columnspan=2)
p2=Entry(main,textvariable=p2_score,bd=5,width=6)
p2.grid(row=5,column=2)

main.mainloop()