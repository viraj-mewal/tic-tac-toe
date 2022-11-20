from tkinter import *
from tkinter import messagebox


class Game:
    def __init__(self) -> None:
        self.turn = "X" # X -> Player ; O -> comp
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
        self.win.title("Tic Tac Toe")
        self.draw()
        self.win.mainloop()

    def draw(self):
        self.btnDict = {}
        for i in range(1, 10):
            self.btnDict[f"b{i}"] = Button(self.win, text=" ", font=("Comic Sans MS", 35), bg="black", fg="white", activebackground="black", activeforeground="white", height=1, width=5, bd=1.3, cursor="target", command=lambda m = i: self.changeText(m))
            self.btnDict[f"b{i}"].grid(row=(i-1)//3, column=(i-1)%3)

    def changeText(self, i):
        value = self.btnDict[f"b{i}"].cget('text')
        if value == " ":
            self.btnDict[f"b{i}"].configure(text=self.turn)

            # check win
            if self.checkWin():
                messagebox.showinfo("Win", f"{self.turn} won !")

                # reset
                self.reset()

            # check draw
            if self.checkDraw():
                messagebox.showinfo("Draw", "It's a draw !")

                # reset
                self.reset()
            # change turn
            self.turn = "O" if self.turn == "X" else "X"

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
            print(self.btnDict[f"b{i}"].cget('text'))
            if self.btnDict[f"b{i}"].cget('text') == " ":
                draw = False
                break
        return draw


    def reset(self):
        for i in range(1, 10):
            self.btnDict[f"b{i}"].configure(text=" ", bg="black", fg="white")



if __name__ == "__main__":
    Game()
