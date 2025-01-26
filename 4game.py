import tkinter as tk
from tkinter import messagebox

class ConnectFour:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four")
        
        self.rows = 6
        self.cols = 7
        self.turn = 1  # Player 1 starts
        self.board = [[0] * self.cols for _ in range(self.rows)]
        
        self.create_widgets()
    
    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=self.cols * 100, height=self.rows * 100)
        self.canvas.pack()
        
        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_game)
        self.restart_button.pack()
        
        self.canvas.bind("<Button-1>", self.handle_click)
        self.draw_board()
    
    def draw_board(self):
        self.canvas.delete("all")
        for row in range(self.rows):
            for col in range(self.cols):
                x0 = col * 100
                y0 = row * 100
                x1 = x0 + 100
                y1 = y0 + 100
                self.canvas.create_rectangle(x0, y0, x1, y1, fill="grey")
                if self.board[row][col] == 1:
                    self.canvas.create_oval(x0 + 10, y0 + 10, x1 - 10, y1 - 10, fill="blue")
                elif self.board[row][col] == 2:
                    self.canvas.create_oval(x0 + 10, y0 + 10, x1 - 10, y1 - 10, fill="green")
    
    def handle_click(self, event):
        col = event.x // 100
        if self.make_move(col):
            if self.check_winner():
                self.draw_board()
                messagebox.showinfo("Game Over", f"Player {self.turn} wins!")
                self.restart_game()
            else:
                self.turn = 3 - self.turn  # Switch turns
                self.draw_board()
    
    def make_move(self, col):
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == 0:
                self.board[row][col] = self.turn
                return True
        return False
    
    def check_winner(self):

        for row in range(self.rows):
            for col in range(self.cols - 3):
                if self.board[row][col] == self.turn and self.board[row][col + 1] == self.turn and self.board[row][col + 2] == self.turn and self.board[row][col + 3] == self.turn:
                    return True
        for row in range(self.rows - 3):
            for col in range(self.cols):
                if self.board[row][col] == self.turn and self.board[row + 1][col] == self.turn and self.board[row + 2][col] == self.turn and self.board[row + 3][col] == self.turn:
                    return True
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if self.board[row][col] == self.turn and self.board[row + 1][col + 1] == self.turn and self.board[row + 2][col + 2] == self.turn and self.board[row + 3][col + 3] == self.turn:
                    return True
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                if self.board[row][col] == self.turn and self.board[row - 1][col + 1] == self.turn and self.board[row - 2][col + 2] == self.turn and self.board[row - 3][col + 3] == self.turn:
                    return True
        return False
    
    def restart_game(self):
        self.board = [[0] * self.cols for _ in range(self.rows)]
        self.turn = 1
        self.draw_board()

if __name__ == "__main__":
    root = tk.Tk()
    game = ConnectFour(root)
    root.mainloop()
