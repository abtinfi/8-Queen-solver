import tkinter as tk
from tkinter import messagebox

class EightQueensSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("8-Queens Solver")
        self.board_size = 8
        self.queens = [-1] * self.board_size  #set queen location in every Column
        self.queens_count = 0
        self.create_board()
        self.solve_button = tk.Button(self.root, text="Solve", command=self.solve)
        self.solve_button.grid(row=self.board_size, column=0, columnspan=self.board_size // 2)
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_board)
        self.reset_button.grid(row=self.board_size, column=self.board_size // 2, columnspan=self.board_size // 2)

    def create_board(self):
        self.tiles = []
        for i in range(self.board_size):
            row = []
            for j in range(self.board_size):
                tile = tk.Button(self.root, width=5, height=3, command=lambda i=i, j=j: self.place_queen(i, j))
                tile.grid(row=i, column=j)
                if (i + j) % 2 == 0:
                    tile.config(bg="white")
                else:
                    tile.config(bg="gray")
                row.append(tile)
            self.tiles.append(row)

    #get gueen from user
    def place_queen(self, row, col):
        #set limit for enter 1 gueen
        if self.queens_count >= 1:
            messagebox.showinfo("Info", "Only one queen can be placed!")
            return

        if self.queens[col] != -1:
            messagebox.showinfo("Info", "Queen already placed in this column!")
            return

        self.queens[col] = row
        self.tiles[row][col].config(text="Q", fg="red")
        self.queens_count += 1  
        self.solve_button.config(state=tk.NORMAL)

    def solve(self):
        if not self.is_valid_initial_state():
            messagebox.showinfo("Info", "Invalid initial state!")
            return

        if self.solve_queens(0):
            self.display_solution()
        else:
            messagebox.showinfo("Info", "No solution exists with the given initial state.")

    # check state is valid or not
    def is_valid_initial_state(self):
        for col in range(self.board_size):
            if self.queens[col] != -1:
                for c in range(col):
                    if self.queens[c] != -1 and (self.queens[c] == self.queens[col] or abs(self.queens[c] - self.queens[col]) == abs(c - col)):
                        return False
        return True

    def solve_queens(self, col):
        if col >= self.board_size:
            return True
        if self.queens[col] != -1:
            return self.solve_queens(col + 1)
        for row in range(self.board_size):
            if self.is_safe(row, col):
                self.queens[col] = row
                if self.solve_queens(col + 1):
                    return True
                self.queens[col] = -1   
        return False

    def is_safe(self, row, col):
        for c in range(self.board_size):
            if self.queens[c] != -1 and (self.queens[c] == row or abs(self.queens[c] - row) == abs(c - col)):
                return False
        return True

    def display_solution(self):
        for col in range(self.board_size):
            row = self.queens[col]
            self.tiles[row][col].config(text="Q", fg="blue")

    def reset_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                self.tiles[i][j].config(text="", bg="white" if (i + j) % 2 == 0 else "gray")
        self.queens = [-1] * self.board_size
        self.queens_count = 0  
        self.solve_button.config(state=tk.NORMAL)


root = tk.Tk()
app = EightQueensSolver(root)
root.mainloop()
