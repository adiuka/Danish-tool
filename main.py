from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOUR = "#B1DDC6"
current_card = {}
dict_data = {}
# ======================= WORD SETUP ========================= #
try:
    data = pandas.read_csv("data/updated_dict.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/danish_dict_mine - Sheet1.csv")
    dict_data = original_data.to_dict(orient="records")
else:
    dict_data = data.to_dict(orient="records")


# ======================= CARD SETUP ========================= #
def next_card():
    global current_card
    current_card = random.choice(dict_data)
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_word_plural, text="Plural", fill="white")


def flip_card_back():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_word_plural, text="Plural", fill="white")


def flip_card_front():
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(card_title, text="Danish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Danish"], fill="black")
    canvas.itemconfig(card_word_plural, text=current_card["Plural"], fill="black")


def remove_from_dict():
    try:
        dict_data.remove(current_card)
        data = pandas.DataFrame(dict_data)
        data.to_csv(path_or_buf="data/updated_dict.csv")
        next_card()
    except IndexError:
        messagebox.showinfo(title="No more words", message="You have reached the end of your learning with "
                                                           "the current dictionary")


# ======================= UI SETUP =========================== #
# WINDOW
window = Tk()
window.title("Let's Learn Dansk!")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOUR)
# CANVAS
canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front_img = PhotoImage(file="photos/card_front.png")
card_back_img = PhotoImage(file="photos/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_back_img)
canvas.grid(column=0, row=0, columnspan=3)
canvas.config(bg=BACKGROUND_COLOUR)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 260, text="Title", font=("Ariel", 60, "bold"))
card_word_plural = canvas.create_text(400, 340, text="Plural", font=("Ariel", 40, "italic"))
# BUTTONS
flip_card_button_back = Button(text="Flip English", command=flip_card_back)
flip_card_button_back.grid(column=0, row=1)
flip_card_button_front = Button(text="Flip Danish", command=flip_card_front)
flip_card_button_front.grid(column=0, row=2)
remove_card_button = Button(text="Remove from Dictionary", command=remove_from_dict)
remove_card_button.grid(column=1, row=1)
next_card_button = Button(text="Next Card", command=next_card)
next_card_button.grid(column=2, row=1)

next_card()

window.mainloop()
