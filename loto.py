from Tkinter import *
import Tkinter
import random

loto_winning_numbers = []

def generator():
    for i in range(0, int(entry_numbers_chosen.get())):
        is_new_random_number = False

        while not is_new_random_number:
            new_random_number = random.randint(1, int(entry_numbers_in_the_game.get()))

            if (new_random_number not in loto_winning_numbers):
                loto_winning_numbers.append(new_random_number)
                is_new_random_number = True
    loto_winning_numbers.sort()
    result_label.config(text=loto_winning_numbers)

def reset():
    global loto_winning_numbers
    loto_winning_numbers = []
    entry_numbers_in_the_game.delete(0, Tkinter.END)
    entry_numbers_chosen.delete(0, Tkinter.END)
    result_label.config(text="")

frame = Tk()
frame.geometry("600x200")
frame.title("LOTO")
greeting = Label(frame, text="Lottery numbers generator\n\n")
greeting.grid (row=0, column=0)

label_numbers_in_the_game = Label(frame, text="How many numbers should be in the box?")
label_numbers_in_the_game.grid(row=1, column=0)
entry_numbers_in_the_game = Entry(frame)
entry_numbers_in_the_game.grid(row=1, column=1)


label_numbers_chosen = Label(frame, text="How many numbers should be guessed?")
label_numbers_chosen.grid(row=2, column=0)
entry_numbers_chosen = Entry(frame)
entry_numbers_chosen.grid(row=2, column=1)

generate_button = Button(frame, text=" Generate ", command = generator)
generate_button.grid (row=1, column=5, rowspan=2)

placeholder_label = Label(frame, text="")
placeholder_label.grid (row=3)
result_label_text = Label(frame, text="Generates numbers are:")
result_label_text.grid (row=4, column=0)
placeholder_label = Label(frame, text="")
result_label = Label(frame, text="")
result_label.grid (row=4, column=1, columnspan=2)

placeholder_label.grid (row=5)
reset_button = Button(frame, text="New Generator", command = reset)
reset_button.grid (row=6, column=0)


frame.mainloop()