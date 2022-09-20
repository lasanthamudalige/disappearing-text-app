from tkinter import *


root = Tk()


def main():
    root.title("Disappearing text app")
    root.geometry("1000x600")

    global text
    text = Text(root, height=40, width=100, font=25)
    text.pack(padx=20, pady=20)

    root.bind('<KeyPress>', on_press)
    root.bind('<KeyRelease>', on_release)

    root.mainloop()


def on_press(key):
    try:
        root.after_cancel(delete_id)
    except NameError:
        pass


def on_release(key):
    global delete_id
    delete_id = root.after(5000, delete_text)


def delete_text():
    text.delete("1.0", END)


main()
