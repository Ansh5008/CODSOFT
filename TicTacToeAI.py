import tkinter as tk
from tkinter import messagebox, simpledialog
import math

HUMAN = ''
AI = ''
EMPTY = ' '

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe AI")
        self.board = [[EMPTY for _ in range(3)] for _ in range(3)]
        self.buttons = [[None]*3 for _ in range(3)]
        self.current_player = None

        self.ask_player_symbol()
        self.create_gui()

        if self.current_player == AI:
            self.root.after(500, self.ai_move)

    def ask_player_symbol(self):
        global HUMAN, AI
        while True:
            choice = simpledialog.askstring("Choose Symbol", "Do you want to be X or O?", parent=self.root)
            if choice is None:
                exit()
            choice = choice.upper()
            if choice in ['X', 'O']:
                HUMAN = choice
                AI = 'O' if HUMAN == 'X' else 'X'
                self.current_player = HUMAN if HUMAN == 'X' else AI
                break
            else:
                messagebox.showerror("Invalid Input", "Please enter X or O")

    def create_gui(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for i in range(3):
            for j in range(3):
                btn = tk.Button(frame, text='', font=('Arial', 32), width=5, height=2,
                                command=lambda r=i, c=j: self.human_move(r, c))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

        reset_btn = tk.Button(self.root, text='Restart Game', font=('Arial', 14),
                              command=self.reset_game)
        reset_btn.pack(pady=10)

    def reset_game(self):
        self.board = [[EMPTY for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', state=tk.NORMAL)
        self.current_player = HUMAN if HUMAN == 'X' else AI
        if self.current_player == AI:
            self.root.after(500, self.ai_move)

    def human_move(self, row, col):
        if self.board[row][col] == EMPTY and self.current_player == HUMAN:
            self.board[row][col] = HUMAN
            self.buttons[row][col].config(text=HUMAN)
            if self.check_game_over():
                return
            self.current_player = AI
            self.root.after(500, self.ai_move)

    def ai_move(self):
        best_score = -math.inf
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == EMPTY:
                    self.board[i][j] = AI
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = EMPTY
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        if best_move:
            i, j = best_move
            self.board[i][j] = AI
            self.buttons[i][j].config(text=AI)
        self.check_game_over()
        self.current_player = HUMAN

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner(AI):
            return 10 - depth
        if self.check_winner(HUMAN):
            return depth - 10
        if self.is_full():
            return 0

        if is_maximizing:
            best = -math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == EMPTY:
                        board[i][j] = AI
                        val = self.minimax(board, depth + 1, False)
                        board[i][j] = EMPTY
                        best = max(best, val)
            return best
        else:
            best = math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == EMPTY:
                        board[i][j] = HUMAN
                        val = self.minimax(board, depth + 1, True)
                        board[i][j] = EMPTY
                        best = min(best, val)
            return best

    def check_game_over(self):
        if self.check_winner(HUMAN):
            self.end_game("You win!")
            return True
        elif self.check_winner(AI):
            self.end_game("AI wins!")
            return True
        elif self.is_full():
            self.end_game("It's a draw!")
            return True
        return False

    def check_winner(self, player):
        b = self.board
        win_states = [
            [b[0][0], b[0][1], b[0][2]],
            [b[1][0], b[1][1], b[1][2]],
            [b[2][0], b[2][1], b[2][2]],
            [b[0][0], b[1][0], b[2][0]],
            [b[0][1], b[1][1], b[2][1]],
            [b[0][2], b[1][2], b[2][2]],
            [b[0][0], b[1][1], b[2][2]],
            [b[0][2], b[1][1], b[2][0]],
        ]
        return [player]*3 in win_states

    def is_full(self):
        return all(self.board[i][j] != EMPTY for i in range(3) for j in range(3))

    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state=tk.DISABLED)

# Start GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
