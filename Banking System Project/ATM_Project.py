from tkinter import *
from tkinter import messagebox
import numpy as np
from PIL import ImageTk,Image

accountnumber = [] # global variables
names = []
balance = []
def Show_balance(): # index bug
    balancetxt = "Your balance is: "+ str(balance[index-1])
    messagebox.showinfo("Balance",balancetxt)
def Make_Deposit(): # index bug
    if(float(depositentry.get())>0):
        #add deposit to the current balance
        balance[index-1] = float(depositentry.get())+balance[index-1]
        value = str(balance[index-1])
        messagebox.showinfo("Balance","the deposit was successful and the new balance is : "+value)#without bonuce
        #with bonuce
        #write in file the new deposite
        write_in_file()
    else:
        messagebox.showinfo("error","the value must be positive value")

def Make_Withdraw(): # index bug
    if(float(withdrawentry.get())>0 and balance[index-1] - float(withdrawentry.get()) >= 0 ):
        #add deposit to the current balance
        balance[index-1] = balance[index-1] - float(withdrawentry.get())
        textmess = str(balance[index-1])
        messagebox.showinfo("Balance","the withdarwal transaction was successful and the new balance is : "+textmess)#without bonuce
        #with bonuce
        #write in file the new deposite
        write_in_file()
    elif(float(withdrawentry.get())>0):
        messagebox.showinfo("error","the value must be less than your balance value")
    else:
        messagebox.showinfo("error","the value must be positive value")

def Exit(): 
    messagebox.showinfo("goodbye","the system is shutdown now mr : " + names[index-1])
    screen.destroy()

def screen_deposit():
    global depscreen
    global depositentry
    depscreen = Toplevel()
    Label(depscreen,bg = "grey", text = "Welcome to our bank project", font= "ar 15 bold").pack()
    Label(depscreen,text = "please enter the amount you want to deposit").pack()
    depositentry = Entry(depscreen)
    Label(depscreen,text = "").pack()
    depositentry.pack()
    depositbutton = Button(depscreen, text = "deposit", height = "1", width = "15", command = Make_Deposit)
    depositbutton.pack()
    Label(depscreen,text = "").pack()
    
def screen_withdraw():
    global withdrscreen
    global withdrawentry
    withdrscreen = Toplevel()
    Label(withdrscreen,bg = "grey", text = "Welcome to our bank project", font= "ar 15 bold").pack()
    Label(withdrscreen,text = "please enter the amount you want to withdraw").pack()
    withdrawentry = Entry(withdrscreen)
    Label(withdrscreen,text = "").pack()
    withdrawentry.pack()
    withdrawbutton = Button(withdrscreen, text = "withdraw", height = "1", width = "15", command = Make_Withdraw)
    withdrawbutton.pack()
    Label(withdrscreen,text = "").pack()
    
def welcome_screen(idx):
    global top
    global index
    index = idx
    top = Toplevel()
    nametxt = "Welcome Mr " + names[idx-1]
    screen.geometry("300x200")
    screen.title("hager")
    balancetxt = "Your balance is: "+ str(balance[idx-1])
    Label(top,bg = "grey", text = "Welcome to our bank project", font= "ar 15 bold").pack()
    Label(top,text = nametxt).pack()
    Button(top, text = "Show Balance", height = "1", width = "15", command = Show_balance).pack()
    Button(top, text = "Make a Deposit", height = "1", width = "15", command = screen_deposit).pack()
    Button(top, text = "Make Withdrawal", height = "1", width = "15", command = screen_withdraw).pack()
    Button(top, text = "Exit", height = "1", width = "15", command = Exit).pack()
    Label(top,text = "").pack()
    

def read_from_file():
    f=open("datafile.txt", "r")
    content = f.read()
    #print(content)
    li = []
    count = 1
    content = content.replace("\n",",") 
    list = content.split(",")
    list = list
    #print(list)
    for x in list:
        if(count == 1):
            accountnumber.append(int(x))
            count += 1
        elif(count == 2):
            names.append(x)
            count += 1
        elif(count == 3):
            balance.append(float(x))
            count = 1
    f.close()
def write_in_file():
    f = open("datafile.txt", "w")
    f.truncate()
    #accountnumber + names + balance
    count = 0
    for i in accountnumber:
        if(count == len(accountnumber)-1):
            line = str(i)+","+str(names[count])+","+str(balance[count])
        else:
            line = str(i)+","+str(names[count])+","+str(balance[count])+"\n"
        f.write(str(line))
        count +=1
    f.close()
    
def account_number_exsist(acn):
    count =0
    for x in accountnumber:
        count +=1
        if(x==acn):
            return count
    return -1

def login():
    try:
        accountnum = int(accountnumentry.get())
    except ValueError:
        messagebox.showinfo("error","enter a valid account number")
    else:
        read_from_file()
        idx = account_number_exsist(accountnum)
        if(idx !=-1):
            welcome_screen(idx)
        else:
            messagebox.showinfo("error","this account number dosn`t exsist !!!")
        # check if the account number is exist or print message say that "enter a valid account number"
    

def main_screen():
     global screen
     global accountnumentry
     screen = Tk()
     screen.geometry("300x200")
     screen.title("hager")
     Label(screen,bg = "grey", text = "Welcome to our bank project", font= "ar 15 bold").pack()
     Label(text = "").pack()
     account = Label(screen, text = "Account Number " )
     account.pack()
     accountnumentry = Entry(screen)
     accountnumentry.pack()
     Label(text = "").pack()
     loginbutton = Button(screen, text = "Login", height = "1", width = "15", command = login)
     loginbutton.pack()
     screen.mainloop()

main_screen()
