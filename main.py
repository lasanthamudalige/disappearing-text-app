from tkinter import *
from pynput.keyboard import Key, Listener


root = Tk()


def main():
    root.title("Disappearing text app")
    root.geometry("1000x600")

    text = Text(root, height=40, width=100)
    text.pack(pady=10)

    root.mainloop()


main()
