import tkinter as tk

def create_window():
    window = tk.Tk()
    window.title("Tic-Tac-Toe")
    window.geometry("300x300")

    buttons = []
    current_player = ["X"]

    def on_button_click(row, col):
        if buttons[row][col]["text"] == "":
            buttons[row][col]["text"] = current_player[0]
            current_player[0] = "O" if current_player[0] == "X" else "X"

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
