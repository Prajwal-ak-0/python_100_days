from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy Capstone")
window.minsize(400, 400)
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

data = pandas.read_csv("data/french_words.csv")
fr = data.French
en = data.English

correct_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=300, height=300)
logo = PhotoImage(file="images/card_back.png")
canvas.create_image(100, 100, image=logo)

label_1 = Label(text="French")
label_1.config(bg="white",font=('Arial',16,'normal'))
label_1_window = canvas.create_window(150,50,window=label_1)

rand_int = random.randint(0,len(fr)-1)
word = fr[rand_int]
label_2 = Label(text=f"{word}")
label_2.config(bg="white",font=('Arial',40,'normal'))
label_2_window = canvas.create_window(150,150,window=label_2)
canvas.pack()


def on_correct_button_click():
    for i in range(0,len(fr)-1,1):
        if word == fr[i]:
            fr.pop(i)
    print(len(fr))


# Function to replace the first canvas with the second canvas


def on_wrong_button_click():
    new_canvas.destroy()
    can = Canvas(width=300, height=300)
    logo = PhotoImage(file="images/card_back.png")
    can.create_image(100, 100, image=logo)

    label_1 = Label(text="French")
    label_1.config(bg="white", font=('Arial', 16, 'normal'))
    label_1_window = can.create_window(150, 50, window=label_1)

    rand_int = random.randint(0, len(fr) - 1)
    word = fr[rand_int]
    label_2 = Label(text=f"{word}")
    label_2.config(bg="white", font=('Arial', 40, 'normal'))
    label_2_window = can.create_window(150, 150, window=label_2)
    can.pack()
# Schedule the replacement after 3 seconds
window.after(3000)

canvas.destroy()  # Destroy the first canvas
new_canvas = Canvas(width=300, height=300)
new_logo = PhotoImage(file="images/card_back.png")
new_canvas.create_image(100, 100, image=new_logo)
new_canvas.pack()
correct_button = Button(window, image=correct_image, command=on_correct_button_click, bd=0, highlightthickness=0)
wrong_button = Button(window, image=wrong_image, command=on_wrong_button_click, bd=0, highlightthickness=0)

correct_button_window = new_canvas.create_window(0, 300, anchor="sw", window=correct_button)
wrong_button_window = new_canvas.create_window(300, 300, anchor="se", window=wrong_button)


window.mainloop()
