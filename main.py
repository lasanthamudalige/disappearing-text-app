from tkinter import *


root = Tk()


def main():
    root.title("Fade")
    root.geometry("1000x600")

    global text_box
    text_box = Text(root, height=40, width=100, font=25)
    text_box.focus()
    text_box.pack(padx=20, pady=20)

    # When that pressed key is released
    root.bind('<KeyRelease>', on_release)

    root.mainloop()


# When a key is released delete function is going to get call after 5 seconds
def on_release(key):
    text_before = text_box.get("1.0", END)
    root.after(5000, delete_text, text_before)


def delete_text(text):
    text_before = text
    text_now = text_box.get("1.0", END)

    """
    When after calls the delete text function.
    If before letter count == now letter count text.
    Every letter in the textbox is going to get cleared.
    """
    if len(text_before) == len(text_now):
        text_box.delete("1.0", END)


main()
