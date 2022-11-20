from tkinter import *
from tkinter import messagebox
import random
from time import sleep

###### Variables #####

indexes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
computer_score = 0
user_score = 0

root = Tk()
root.configure(bg="black")
root.title("Tic - Tac - Toe")
root.resizable(False, False)
root.geometry("530x560")

###### Functions ########

def create_button(frame, command):
    button = Button(frame, borderwidth=5, height=1, width=4, text="  ", bg="white", fg="white", font=("DS-DIGITAL",60,"bold"), relief=GROOVE, command=command)
    return button
# -> button click functions

def cm_button1():
    try:
        indexes.remove(1)
        button1.config(text='X', fg="black", font=("Helvetica",49,"bold"))
        main(1)
    except:
        messagebox.showinfo("INFO", "That place is already filled")
        

def cm_button2():
    try:
        indexes.remove(2)
        button2.config(text='X', fg="black", font=("Helvetica",49,"bold"))
        main(2)
    except:
        messagebox.showinfo("INFO", "That place is already filled")

def cm_button3():
    try:
        indexes.remove(3)
        button3.config(text='X', fg="black", font=("Helvetica",49,"bold"))
        main(3)
    except:
        messagebox.showinfo("INFO", "That place is already filled")

def cm_button4():
    try:
        indexes.remove(4)
        button4.config(text='X', fg="black", font=("Helvetica",49,"bold"))
        main(4)
    except:
        messagebox.showinfo("INFO", "That place is already filled")

def cm_button5():
    try:
        indexes.remove(5)
        button5.config(text='X', fg="black", font=("Helvetica",49,"bold"))
        main(5)
    except:
        messagebox.showinfo("INFO", "That place is already filled")

def cm_button6():
    try:
        indexes.remove(6)
        button6.config(text='X', fg="black", font=("Helvetica",49,"bold"))
        main(6)
    except:
        messagebox.showinfo("INFO", "That place is already filled")

def cm_button7():
    try:
        indexes.remove(7)
        button7.config(text='X', fg="black", font=("Helvetica",49,"bold"))
        main(7)
    except:
        messagebox.showinfo("INFO", "That place is already filled")
    
def cm_button8():
    try:
        indexes.remove(8)
        button8.config(text='X', fg="black", font=("Helvetica",49,"bold"))
        main(8)
    except:
        messagebox.showinfo("INFO", "That place is already filled")

def cm_button9():
    try:
        indexes.remove(9)
        button9.config(text='X', fg="black", font=("Helvetica",49,"bold"))
        main(9)
    except:
        messagebox.showinfo("INFO", "That place is already filled")

def destroy():
    confirm = messagebox.askyesno("WARNING", "Do you want to really close !")
    if confirm == True:
        root.destroy()

######## Designing ########

exit = Button(root, text="Exit" , borderwidth=8, bg="black", relief=RIDGE, fg="white",font=("Helvetica",25,"bold"), command=destroy)
exit.place(x=400, y=10)

label1 = Label(root, font=("Girassol",13,"bold"), bg="black", fg="white", text="Your Score : 0")
label1.grid(row = 0,  column = 0, sticky = W,  pady=10)

label2 = Label(root, font=("Girassol",13,"bold"), bg="black", fg="white", text="Computer Score : 0")
label2.grid(row = 1, column = 0, sticky = W, pady=10)
label2.grid_propagate(False)

button1 = create_button(root, cm_button1)
button1.grid(row = 2, column = 0, sticky = W, pady = 0)

button2 = create_button(root, cm_button2)
button2.grid(row = 2, column= 1, sticky = W, pady = 0)

button3 = create_button(root, cm_button3)
button3.grid(row = 2, column= 2, sticky = W, pady = 0)

button4 = create_button(root, cm_button4)
button4.grid(row = 3, column= 0, sticky = W, pady = 0)

button5 = create_button(root, cm_button5)
button5.grid(row = 3, column= 1, sticky = W, pady = 0)

button6 = create_button(root, cm_button6)
button6.grid(row = 3, column= 2, sticky = W, pady = 0)

button7 = create_button(root, cm_button7)
button7.grid(row = 4, column= 0, sticky = W, pady = 0)

button8 = create_button(root, cm_button8)
button8.grid(row = 4, column= 1, sticky = W, pady = 0)

button9 = create_button(root, cm_button9)
button9.grid(row = 4, column= 2, sticky = W, pady = 0)

######### Functions to return indexes ########

def return_indexes():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    
    # x - booleans

    x1 = False
    x2 = False 
    x3 = False
    x4 = False
    x5 = False
    x6 = False
    x7 = False
    x8 = False
    x9 = False

    # y - booleans

    o1 = False
    o2 = False 
    o3 = False
    o4 = False
    o5 = False
    o6 = False
    o7 = False
    o8 = False
    o9 = False
    
    # X conditions

    if button1["text"] == "X":
        x1 = True

    if button2["text"] == "X":
        x2 = True
    
    if button3["text"] == "X":
        x3 = True

    if button4["text"] == "X":
        x4 = True

    if button5["text"] == "X":
        x5 = True
    
    if button6["text"] == "X":
        x6 = True

    if button7["text"] == "X":
        x7 = True

    if button8["text"] == "X":
        x8 = True

    if button9["text"] == "X":
        x9 = True

    # O conditions

    if button1["text"] == "O":
        o1 = True

    if button2["text"] == "O":
        o2 = True
    
    if button3["text"] == "O":
        o3 = True

    if button4["text"] == "O":
        o4 = True

    if button5["text"] == "O":
        o5 = True
    
    if button6["text"] == "O":
        o6 = True

    if button7["text"] == "O":
        o7 = True

    if button8["text"] == "O":
        o8 = True

    if button9["text"] == "O":
        o9 = True
   
    return x1, x2, x3, x4, x5, x6, x7, x8, x9, o1, o2, o3, o4, o5, o6, o7, o8, o9

def main(index):
    global indexes
    draw = check()
    if indexes == [] and draw == 0:
        messagebox.showinfo("INFO", "Match was draw")
        reset()
        return
    
    if draw == 1:
        pass
    else:
        computer_choice = random.choice(indexes)
        if computer_choice == 1:
            button1.config(text='O', fg="black", font=("Helvetica",49,"bold"))
        elif computer_choice == 2:
            button2.config(text='O', fg="black", font=("Helvetica",49,"bold"))
        elif computer_choice == 3:
            button3.config(text='O', fg="black", font=("Helvetica",49,"bold"))
        elif computer_choice == 4:
            button4.config(text='O', fg="black", font=("Helvetica",49,"bold"))
        elif computer_choice == 5:
            button5.config(text='O', fg="black", font=("Helvetica",49,"bold"))
        elif computer_choice == 6:
            button6.config(text='O', fg="black", font=("Helvetica",49,"bold"))
        elif computer_choice == 7:
            button7.config(text='O', fg="black", font=("Helvetica",49,"bold"))
        elif computer_choice == 8:
            button8.config(text='O', fg="black", font=("Helvetica",49,"bold"))
        elif computer_choice == 9:
            button9.config(text='O', fg="black", font=("Helvetica",49,"bold"))  
        indexes.remove(computer_choice)

    draw = check()
    if indexes == [] and draw == 0:
        messagebox.showinfo("INFO", "Match was draw")
        reset()
        return

def check():
    global user_score, computer_score
    x1, x2, x3, x4, x5, x6, x7, x8, x9, o1, o2, o3, o4, o5, o6, o7, o8, o9 = return_indexes()
    

    # Vertical position check - x

    if x1 and x2 and x3:
        messagebox.showinfo("Congratulation", "You Won the Game !")
        user_score += 1
        label1.config(text="Your Score : " + str(user_score))
        reset()
        return 1
    
    elif x4 and x5 and x6:
        messagebox.showinfo("Congratulation", "You Won the Game !")
        user_score += 1
        label1.config(text="Your Score : " + str(user_score))
        reset()
        return 1
    
    elif x7 and x8 and x9:
        messagebox.showinfo("Congratulation", "You Won the Game !")
        user_score += 1
        label1.config(text="Your Score : " + str(user_score))
        reset()
        return 1

    # Horizontal position check - x

    elif x1 and x4 and x7:
        messagebox.showinfo("Congratulation", "You Won the Game !")
        user_score += 1
        label1.config(text="Your Score : " + str(user_score))
        reset()
        return 1
    
    elif x2 and x5 and x8:
        messagebox.showinfo("Congratulation", "You Won the Game !")
        user_score += 1
        label1.config(text="Your Score : " + str(user_score))
        reset()
        return 1
    
    elif x3 and x6 and x9:
        messagebox.showinfo("Congratulation", "You Won the Game !")
        user_score += 1
        label1.config(text="Your Score : " + str(user_score))
        reset()
        return 1
    
    # Cross position check - x

    elif x1 and x5 and x9:
        messagebox.showinfo("Congratulation", "You Won the Game !")
        user_score += 1
        label1.config(text="Your Score : " + str(user_score))
        reset()
        return 1
    
    elif x3 and x5 and x7:
        messagebox.showinfo("Congratulation", "You Won the Game !")
        user_score += 1
        label1.config(text="Your Score : " + str(user_score))
        reset()
        return 1



    # Vertical position check - y

    elif o1 and o2 and o3:
        computer_score += 1
        messagebox.showinfo("Congratulation", "Computer won the Game !")
        label2.config(text="Computer Score : " + str(computer_score))
        reset()
        return 1
    
    elif o4 and o5 and o6:
        messagebox.showinfo("Congratulation", "Computer won the Game !")
        computer_score += 1
        label2.config(text="Computer Score : " + str(computer_score))
        reset()
        return 1
    
    elif o7 and o8 and o9:
        messagebox.showinfo("Congratulation", "Computer won the Game !")
        computer_score += 1
        label2.config(text="Computer Score : " + str(computer_score))
        reset()
        return 1

    # Horizontal position check - x

    elif o1 and o4 and o7:
        messagebox.showinfo("Congratulation", "Computer won the Game !")
        computer_score += 1
        label2.config(text="Computer Score : " + str(computer_score))
        reset()
        return 1
    
    elif o2 and o5 and o8:
        messagebox.showinfo("Congratulation", "Computer won the Game !")
        computer_score += 1
        label2.config(text="Computer Score : " + str(computer_score))
        reset()
        return 1

    elif o3 and o6 and o9:
        messagebox.showinfo("Congratulation", "Computer won the Game !")
        computer_score += 1
        label2.config(text="Computer Score : " + str(computer_score))
        reset()
        return 1
    
    # Cross position check - x

    elif o1 and o5 and o9:
        messagebox.showinfo("Congratulation", "Computer won the Game !")
        computer_score += 1
        label2.config(text="Computer Score : " + str(computer_score))
        reset()
        return 1
    
    elif o3 and o5 and o7:
        messagebox.showinfo("Congratulation", "Computer won the Game !")
        computer_score += 1
        label2.config(text="Computer Score : " + str(computer_score))
        reset()
        return 1
    
    else:
        return 0

    
    

    
def reset():
    global indexes
    indexes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    button1.config(text="")
    button2.config(text="")
    button3.config(text="")
    button4.config(text="")
    button5.config(text="")
    button6.config(text="")
    button7.config(text="")
    button8.config(text="")
    button9.config(text="")

root.mainloop()