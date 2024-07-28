import tkinter as tk
from tkinter import messagebox

def create_window():
    window = tk.Tk()
    window.title("Tic-Tac-Toe")
    window.geometry("300x300")

    buttons = []
    current_player = ["X"]

    def check_winner():
        for row in range(3):
            if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
                return True
        for col in range(3):
            if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
                return True
        if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
            return True
        if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
            return True
        return False

    def on_button_click(row, col):
        if buttons[row][col]["text"] == "":
            buttons[row][col]["text"] = current_player[0]
            if check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player[0]} wins!")
                reset_board()
            else:
                current_player[0] = "O" if current_player[0] == "X" else "X"

    def reset_board():
        for row in range(3):
            for col in range(3):
                buttons[row][col]["text"] = ""

    for row in range(3):
        row_buttons = []
        for col in range(3):
            button = tk.Button(window, text="", width=10, height=3, command=lambda r=row, c=col: on_button_click(r, c))
            button.grid(row=row, column=col)
            row_buttons.append(button)
        buttons.append(row_buttons)
    
    window.mainloop()

if __name__ == "__main__":
    create_window()