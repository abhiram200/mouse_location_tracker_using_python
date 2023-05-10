import pyautogui
import tkinter as tk

def show_timer(root, label, count_down):
    if count_down >= 0:
        label.config(text="Timer: {} seconds".format(count_down))
        root.after(1000, show_timer, root, label, count_down - 1)
    else:
        root.destroy()

def start_timer():
    root = tk.Tk()
    root.geometry("200x100")
    root.title("Timer")
    label = tk.Label(root, text="Timer: 5 seconds")
    label.pack()
    show_timer(root, label, 5)
    root.mainloop()



count = 0

loc = pyautogui.prompt("How many mouse locations you want to fetch?")

while count < loc:
    start_timer()
    x, y = pyautogui.position()
    print("Mouse is at (x, y): ({}, {})".format(x, y))
    count = count + 1
