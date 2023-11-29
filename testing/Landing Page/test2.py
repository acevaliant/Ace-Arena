import random
import tkinter as tk
from tkinter import messagebox

# Game settings
game_title = "Spider Solitaire"
window_width = 800
window_height = 600

# Define colors
background_color = "#b3b3b3"
card_back_color = "#696969"

# Card images
card_back_image = tk.PhotoImage(file="card_back.png")

# Initialize global variables
cards = []
open_cards = []
card_counter = 0


class Card:
    def __init__(self, value, suit, face_up):
        self.value = value
        self.suit = suit
        self.face_up = face_up
        self.canvas_id = None

    def __repr__(self):
        return f"{self.value}{self.suit}"


def new_game():
    global cards, open_cards, card_counter
    card_counter = 0
    open_cards = []
    cards = []
    # Generate 52 cards
    for i in range(1, 14):
        for j in range(4):
            card = Card(i, chr(ord('♥') + j), False)
            cards.append(card)
    # Shuffle the cards
    random.shuffle(cards)
    # Draw the cards
    draw_cards()


def draw_cards():
    global card_counter
    for i in range(10):
        if card_counter < 52:
            open_card(card_counter)
            card_counter += 1


def open_card(card_index):
    card = cards[card_index]
    if card.canvas_id is None:
        if card.face_up:
            canvas_id = canvas.create_image(card_index * 40 + 400, 300, image=card.image, tag=f"card{card_index}")
        else:
            canvas_id = canvas.create_image(card_index * 40 + 400, 300, image=card_back_image, tag=f"card{card_index}")
        card.canvas_id = canvas_id
        open_cards.append(card)


def click_card(event):
    card_index = int(event.widget.tag_names()[1][5:])
    card = cards[card_index]
    if card.face_up:
        if len(open_cards) == 1:
            if card.value == 1:
                messagebox.showinfo("Match Found", "Congratulations! You found a match.")
            else:
                messagebox.showinfo("No Match", "Sorry, no match found.")
        else:
            messagebox.showinfo("Too Many Cards", "Please select only one card at a time.")
    else:
        if len(open_cards) < 10:
            card.face_up = True
            open_card(card_index)
        else:
            messagebox.showinfo("Too Many Open Cards", "Please close some cards first.")


# Create the game window
window = tk.Tk()
window.title(game_title)
window.geometry(f"{window_width}x{window_height}")

# Create the game canvas
canvas = tk.Canvas(window, width=window_width, height=window_height, bg=background_color)
canvas.pack()

# Start a new game
new_game()

# Main game loop
window.mainloop()