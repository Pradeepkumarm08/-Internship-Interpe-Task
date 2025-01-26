import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()

    def create_buttons(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text=" ", font=('normal', 40), width=5, height=2,
                                   bg="lime green", fg="black",
                                   command=lambda row=row, col=col: self.on_button_click(row, col))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def on_button_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, fg="blue" if self.current_player == "X" else "red")
            if self.check_winner(self.current_player):
                self.highlight_winner(self.current_player)
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
        else:
            messagebox.showwarning("Tic Tac Toe", "Invalid move! Try again.")

    def check_winner(self, player):
        for row in range(3):
            if all([cell == player for cell in self.board[row]]):
                return True
        for col in range(3):
            if all([self.board[row][col] == player for row in range(3)]):
                return True
        if all([self.board[i][i] == player for i in range(3)]) or all([self.board[i][2-i] == player for i in range(3)]):
            return True
        return False

    def check_draw(self):
        return all([cell != " " for row in self.board for cell in row])

    def highlight_winner(self, player):
        for row in range(3):
            if all([cell == player for cell in self.board[row]]):
                for col in range(3):
                    self.buttons[row][col].config(bg="lightgreen")
        for col in range(3):
            if all([self.board[row][col] == player for row in range(3)]):
                for row in range(3):
                    self.buttons[row][col].config(bg="lightgreen")
        if all([self.board[i][i] == player for i in range(3)]):
            for i in range(3):
                self.buttons[i][i].config(bg="lightgreen")
        if all([self.board[i][2-i] == player for i in range(3)]):
            for i in range(3):
                self.buttons[i][2-i].config(bg="lightgreen")

    def reset_game(self):
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ", bg="pink")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
