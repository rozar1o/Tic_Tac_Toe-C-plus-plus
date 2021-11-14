#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


from tkinter import *
import tkinter.messagebox

tk= Tk()
tk.title('Tic Tac Toe game with Artificial Intelligence!!')

pa = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()

player1_name = Entry(tk, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)
player2_name = Entry(tk, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)

bclick = True
flag = 0

def disableButton():
    btn1.configure(state=DISABLED)
    btn2.configure(state=DISABLED)
    btn3.configure(state=DISABLED)
    btn4.configure(state=DISABLED)
    btn5.configure(state=DISABLED)
    btn6.configure(state=DISABLED)
    btn7.configure(state=DISABLED)
    btn8.configure(state=DISABLED)
    btn9.configure(state=DISABLED)



def btn_clicked(btns):
    global bclick, flag, player2_name, player1_name, playerb, pa
    if btns["text"] == " " and bclick == True:
        btns["text"] = "X"
        bclick = False
        playerb = p2.get() + " You Win!"
        pa = p1.get() + " You  Win!"
        checkForWin()
        flag += 1


    elif btns["text"] == " " and bclick == False:
        btns["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo('Tic-Tac-Toe', 'Button already Clicked!')

def checkForWin():
    if (btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X' or
        btn4['text'] == 'X' and btn5['text'] == 'X' and btn6['text'] == 'X' or
        btn7['text'] =='X' and btn8['text'] == 'X' and btn9['text'] == 'X' or
        btn1['text'] == 'X' and btn5['text'] == 'X' and btn9['text'] == 'X' or
        btn3['text'] == 'X' and btn5['text'] == 'X' and btn7['text'] == 'X' or
        btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X' or
        btn1['text'] == 'X' and btn4['text'] == 'X' and btn7['text'] == 'X' or
        btn2['text'] == 'X' and btn5['text'] == 'X' and btn8['text'] == 'X' or
        btn7['text'] == 'X' and btn6['text'] == 'X' and btn9['text'] == 'X'):
        disableButton()
        tkinter.messagebox.showinfo('Tic Tac Toe', pa)

    elif(flag == 8):
        tkinter.messagebox.showinfo('Tic Tac Toe', 'Match Tied')

    elif (btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O' or
          btn4['text'] == 'O' and btn5['text'] == 'O' and btn6['text'] == 'O' or
          btn7['text'] == 'O' and btn8['text'] == 'O' and btn9['text'] == 'O' or
          btn1['text'] == 'O' and btn5['text'] == 'O' and btn9['text'] == 'O' or
          btn3['text'] == 'O' and btn5['text'] == 'O' and btn7['text'] == 'O' or
          btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O' or
          btn1['text'] == 'O' and btn4['text'] == 'O' and btn7['text'] == 'O' or
          btn2['text'] == 'O' and btn5['text'] == 'O' and btn8['text'] == 'O' or
          btn7['text'] == 'O' and btn6['text'] == 'O' and btn9['text'] == 'O'):
        disableButton()
        tkinter.messagebox.showinfo('Tic Tac Toe', playerb)


btns = StringVar()
        

pl1 = Label(tk,text='Player 1: ',font='Arial 24 bold',bg='white',fg='red')
pl1.grid(row=1, column=0)
pl2 = Label(tk,text='Player 2: ',font='Arial 24 bold',bg='white',fg='red')
pl2.grid(row=2, column=0)

btn1= Button(tk, text= ' ', font='Arial 24 bold',bg='yellow',height=4,width=8,command= lambda:btn_clicked(btn1))
btn1.grid(row=3,column=0)

btn2= Button(tk, text= ' ', font='Arial 24 bold',bg='yellow',height=4,width=8,command= lambda:btn_clicked(btn2))
btn2.grid(row=3,column=1)

btn3= Button(tk, text= ' ', font='Arial 24 bold',bg='yellow',height=4,width=8,command= lambda:btn_clicked(btn3))
btn3.grid(row=3,column=2)

btn4= Button(tk, text= ' ', font='Arial 24 bold',bg='yellow',height=4,width=8,command= lambda:btn_clicked(btn4))
btn4.grid(row=4,column=0)

btn5= Button(tk, text= ' ', font='Arial 24 bold',bg='yellow',height=4,width=8,command= lambda:btn_clicked(btn5))
btn5.grid(row=4,column=1)

btn6= Button(tk, text= ' ', font='Arial 24 bold',bg='yellow',height=4,width=8,command= lambda:btn_clicked(btn6))
btn6.grid(row=4,column=2)

btn7= Button(tk, text= ' ', font='Arial 24 bold',bg='yellow',height=4,width=8,command= lambda:btn_clicked(btn7))
btn7.grid(row=5,column=0)

btn8= Button(tk, text= ' ', font='Arial 24 bold',bg='yellow',height=4,width=8,command= lambda:btn_clicked(btn8))
btn8.grid(row=5,column=1)

btn9= Button(tk, text= ' ', font='Arial 24 bold',bg='yellow',height=4,width=8,command= lambda:btn_clicked(btn9))
btn9.grid(row=5,column=2)
tk.mainloop()



def btn_clicked():
    tkinter.messagebox.showinfo('clicked!','btn1')

