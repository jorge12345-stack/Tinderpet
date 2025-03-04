import tkinter as tk
from tkinter import Label, Button, OptionMenu, StringVar
from PIL import Image, ImageTk

# Sample pet data (image paths, names, descriptions, zone, price, type)
pets = [
    {"name": "Bella", "image": "pet1.jpg", "description": "A playful and loving golden retriever.", "zone": "Downtown", "price": 50, "type": "Dog"},
    {"name": "Max", "image": "pet2.jpg", "description": "A gentle cat that loves cuddles.", "zone": "Cambridge", "price": 30, "type": "Cat"},
    {"name": "Luna", "image": "pet3.jpg", "description": "A curious bunny with lots of energy.", "zone": "Back Bay", "price": 20, "type": "Rabbit"}
]

current_index = 0
liked_pets = []
favorite_pets = []
filtered_pets = pets

# Filtering function
def filter_pets():
    global filtered_pets, current_index
    selected_zone = zone_var.get()
    selected_type = type_var.get()
    selected_price = price_var.get()
    
    filtered_pets = [p for p in pets if (selected_zone == "All" or p["zone"] == selected_zone) and
                                     (selected_type == "All" or p["type"] == selected_type) and
                                     (selected_price == "All" or p["price"] <= int(selected_price))]
    current_index = 0
    update_pet()

def update_pet():
    if current_index < len(filtered_pets):
        pet = filtered_pets[current_index]
        img = Image.open(pet["image"])
        img = img.resize((250, 250), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
        pet_image_label.config(image=img)
        pet_image_label.image = img
        pet_name_label.config(text=pet["name"])
        pet_desc_label.config(text=f"{pet['description']}\nZone: {pet['zone']}\nPrice: ${pet['price']}\nType: {pet['type']}")
    else:
        pet_name_label.config(text="No more pets!")
        pet_desc_label.config(text="Check your favorites or liked pets.")
        pet_image_label.config(image="")

def like_pet():
    global current_index
    if current_index < len(filtered_pets):
        liked_pets.append(filtered_pets[current_index])
        current_index += 1
        update_pet()

def dislike_pet():
    global current_index
    if current_index < len(filtered_pets):
        current_index += 1
        update_pet()

def favorite_pet():
    global current_index
    if current_index < len(filtered_pets):
        favorite_pets.append(filtered_pets[current_index])
        current_index += 1
        update_pet()

# GUI Setup
root = tk.Tk()
root.mainloop()
root.title("Pet Tinder - Animal Shelter")
root.geometry("400x600")

# Filter options
zone_var = StringVar(value="All")
type_var = StringVar(value="All")
price_var = StringVar(value="All")

zones = ["All", "Downtown", "Cambridge", "Back Bay"]
types = ["All", "Dog", "Cat", "Rabbit"]
prices = ["All", "20", "30", "50"]

zone_menu = OptionMenu(root, zone_var, *zones)
type_menu = OptionMenu(root, type_var, *types)
price_menu = OptionMenu(root, price_var, *prices)

zone_menu.pack()
type_menu.pack()
price_menu.pack()

filter_button = Button(root, text="Filter", command=filter_pets)
filter_button.pack()

pet_image_label = Label(root)
pet_image_label.pack()

pet_name_label = Label(root, text="", font=("Arial", 16, "bold"))
pet_name_label.pack()

pet_desc_label = Label(root, text="", wraplength=350, font=("Arial", 12))
pet_desc_label.pack()

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=20)

btn_dislike = Button(btn_frame, text="❌", fg="red", font=("Arial", 20), command=dislike_pet)
btn_dislike.grid(row=0, column=0, padx=10)

btn_favorite = Button(btn_frame, text="😍", fg="purple", font=("Arial", 20), command=favorite_pet)
btn_favorite.grid(row=0, column=1, padx=10)

btn_like = Button(btn_frame, text="💚", fg="green", font=("Arial", 20), command=like_pet)
btn_like.grid(row=0, column=2, padx=10)

update_pet()
root.mainloop()
