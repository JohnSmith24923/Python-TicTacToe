import tkinter as tk

def create_window():
    window = tk.Tk()
    window.title("Tic-Tac-Toe")
    window.geometry("300x300")
    window.mainloop()

if __name__ == "__main__":
    create_window()