from tkinter import *
from tkinter import messagebox
from sys import exit

class Game:
    def __init__(self) -> None:
        self.turn = "O" # Player A -> O; player B -> X
        self.winPos = [
            [1, 2, 3], # horizontally
            [4, 5, 6],
            [7, 8, 9],

            [1, 4, 7], # vertically
            [2, 5, 8],
            [3, 6, 9],

            [1, 5, 9], # diagonally
            [3, 5, 7]
        ]
        self.win = Tk()
        # self.win.configure(bg="black")
        self.win.title("Tic Tac Toe")
        self.bindings()
        self.scoreO, self.scoreX = 0, 0
        self.limit = 5
        self.draw()
        self.win.mainloop()

    def bindings(self):
        self.win.bind('<i>', lambda event: self.info())
        self.win.bind('<Escape>', lambda event: self.exit())

    def info(self):
        messagebox.showinfo("Info", "- First to reach 10 will win.\n- Press 'esc' to exit\n- Press 'i' for info")

    def exit(self):
        if messagebox.askyesno("Sure", "Are you sure you want to exit"):
            self.win.destroy()
            exit()

    def draw(self):
        self.btnDict = {}
        for i in range(1, 10):
            self.btnDict[f"b{i}"] = Button(self.win, text=" ", font=("Comic Sans MS", 35), bg="black", fg="white", activebackground="black", activeforeground="white", height=1, width=5, bd=1.3, cursor="target", command=lambda m = i: self.changeText(m))
            self.btnDict[f"b{i}"].grid(row=((i-1)//3)+1, column=(i-1)%3)

        # scores
        self.playerO = Label(self.win, text=f"O : {self.scoreO}", font=("Comic Sans MS", 35), bg="black", fg="white", width=5)
        self.vs = Label(self.win, text="VS", font=("Comic Sans MS", 35), bg="black", fg="white", width=5)
        self.playerX = Label(self.win, text=f"X : {self.scoreX}", font=("Comic Sans MS", 35), bg="black", fg="white", width=5)

        self.playerO.grid(row=0, column=0)
        self.vs.grid(row=0, column=1)
        self.playerX.grid(row=0, column=2)

        # turn
        self.turnDisplay = Label(self.win, text=f"O turn", font=("Comic Sans MS", 25), bg="black", fg="white", width=15)
        self.turnDisplay.grid(row=4, column=0, columnspan=3, sticky="news", pady=1)

    def changeText(self, i):
        value = self.btnDict[f"b{i}"].cget('text')
        if value == " ":
            self.btnDict[f"b{i}"].configure(text=self.turn)

            # check win
            if self.checkWin():
                if self.turn == "X": self.scoreX += 1
                elif self.turn == "O": self.scoreO += 1
                self.playerO.config(text=f"O : {self.scoreO}")
                self.playerX.config(text=f"X : {self.scoreX}")
                messagebox.showinfo("Win", f"{self.turn} won the game !")

                # check main win
                if self.scoreO == self.limit or self.scoreX == self.limit:
                    win = "X" if self.scoreX == self.limit else "O"
                    messagebox.showinfo("Congratulations", f"{win} won the series of game !")

                    # ask to restart the game
                    if messagebox.askyesno("Again", "Do you want to play again ?"):
                        self.hardReset()
                        return
                    else:
                        self.win.destroy()
                        exit()


                self.reset()

            # check draw
            if self.checkDraw():
                messagebox.showinfo("Draw", "It's a draw !")

                # reset
                self.reset()
                
            # change turn
            self.turn = "O" if self.turn == "X" else "X"
            self.turnDisplay.config(text=f"{self.turn} turn")

        else:
            messagebox.showerror("Error", "Box is already filled !")


    def checkWin(self):
        for i in self.winPos:
            if self.btnDict[f"b{i[0]}"].cget('text') == self.btnDict[f"b{i[1]}"].cget('text') == self.btnDict[f"b{i[2]}"].cget('text') == self.turn and self.btnDict[f"b{i[0]}"].cget('text') != " ":
                for j in range(3):
                    self.btnDict[f"b{i[j]}"].configure(bg="red")
                return True

        return False

    def checkDraw(self):
        draw = True
        for i in range(1, 10):
            if self.btnDict[f"b{i}"].cget('text') == " ":
                draw = False
                break
        return draw


    def reset(self):
        for i in range(1, 10):
            self.btnDict[f"b{i}"].configure(text=" ", bg="black", fg="white")

    def hardReset(self):
        self.reset()
        self.scoreO, self.scoreX = 0, 0
        self.playerO.config(text=f"O : {self.scoreO}")
        self.playerX.config(text=f"X : {self.scoreX}")



if __name__ == "__main__":
    Game()

############# add change turn panel ############### Ok
