# Author:  Sean Blayney
# Class: CS 361
# Program Name:  D&D Equipment Companion
# Program Description:  This program will allow the user to pick a character class from Dungeons and Dragons.
#                       Once they have chosen a class, they can add weapons and armor from dropdown menus and can
#                       view more information about their equipment, compare their current equipment to different items,
#                       and check that their current class is proficient with their selected equipment.

from tkinter import *
from PIL import ImageTk, Image

# Global Variables
current_class = None
equipped_weapons = []
equipped_armor = []

def openClassSelection():
    class_list = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk"]
    clicked = StringVar()
    clicked.set("Select a Class")

    popup = Toplevel(root)
    class_instructions = Label(popup, text="To begin, choose a character class and click Submit")
    submit_button = Button(popup, text="Submit", command=lambda:closeClassSelection(popup, clicked))
    class_dropdown = OptionMenu(popup, clicked, *class_list)

    class_instructions.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    class_dropdown.grid(row=1, column=0, padx=10, pady=10)
    submit_button.grid(row=1, column=1, padx=10, pady=10)

def closeClassSelection(popup, clicked):
    if clicked.get() != "Select a Class":
        class_label.config(text=clicked.get())
        current_class = clicked.get()
        class_pic_import = Image.open('C:\CS361\DnD-Project\Class-Images\\' + clicked.get() + '.png')
        class_pic_resize = class_pic_import.resize((210, 309))
        class_pic = ImageTk.PhotoImage(class_pic_resize)
        class_portrait.configure(image=class_pic)
        class_portrait.image = class_pic
        popup.destroy()

def openWeaponSelection():
    Weapon_list = ["Club", "Dagger", "Handaxe", "Javelin"]
    clicked = StringVar()
    clicked.set("Select a Weapon")

    popup = Toplevel(root)
    weapon_instructions = Label(popup, text="Choose a Weapon to add to the character")
    submit_button = Button(popup, text="Submit", command=lambda: closeWeaponSelection(popup, clicked))
    class_dropdown = OptionMenu(popup, clicked, *Weapon_list)

    weapon_instructions.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    class_dropdown.grid(row=1, column=0, padx=10, pady=10)
    submit_button.grid(row=1, column=1, padx=10, pady=10)

def closeWeaponSelection(popup, clicked):
    if clicked.get() != "Select a Weapon":
        if equipped_weapons == []:
            equipped_weapons.append(clicked.get())
            new_weapon = Label(root, text=clicked.get())
            view_stats = Button(root, text="View Stats")
            remove_weapon = Button(root, text="Remove Weapon")

            new_weapon.grid(row=4, column=0)
            view_stats.grid(row=4, column=1)
            remove_weapon.grid(row=4, column=2)
        else:
            equipped_weapons.append(clicked.get())
            new_weapon = Label(root, text=clicked.get())
            view_stats = Button(root, text="View Stats")
            remove_weapon = Button(root, text="Remove Weapon")

            new_weapon.grid(row=5, column=0)
            view_stats.grid(row=5, column=1)
            remove_weapon.grid(row=5, column=2)
        popup.destroy()

def openArmorSelection():
    Armor_list = ["Padded", "Leather", "Chainmail", "Platemail"]
    clicked = StringVar()
    clicked.set("Select an Armor")

    popup = Toplevel(root)
    armor_instructions = Label(popup, text="Choose an Armor to add to the character")
    submit_button = Button(popup, text="Submit", command=lambda: closeArmorSelection(popup, clicked))
    armor_dropdown = OptionMenu(popup, clicked, *Armor_list)

    armor_instructions.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    armor_dropdown.grid(row=1, column=0, padx=10, pady=10)
    submit_button.grid(row=1, column=1, padx=10, pady=10)

def closeArmorSelection(popup, clicked):
    if clicked.get() != "Select an Armor":
        if equipped_armor == []:
            equipped_armor.append(clicked.get())
            new_armor = Label(root, text=clicked.get())
            view_stats = Button(root, text="View Stats")
            remove_armor = Button(root, text="Remove Armor", command=lambda:RemoveArmor(new_armor, view_stats, remove_armor))

            new_armor.grid(row=8, column=0)
            view_stats.grid(row=8, column=1)
            remove_armor.grid(row=8, column=2)
        else:
            equipped_armor.append(clicked.get())
            new_armor = Label(root, text=clicked.get())
            view_stats = Button(root, text="View Stats")
            remove_armor = Button(root, text="Remove Armor", command=lambda:RemoveArmor(new_armor, view_stats, remove_armor))

            new_armor.grid(row=9, column=0)
            view_stats.grid(row=9, column=1)
            remove_armor.grid(row=9, column=2)
        popup.destroy()

def RemoveArmor(armor, stats, remove):
    equipped_armor.clear()
    armor.grid_remove()
    stats.grid_remove()
    remove.grid_remove()

# Setting up Tkinter
root = Tk()
root.title("D&D Equipment Companion")
root.geometry('700x600')



title_label = Label(root, text="Dungeons and Dragons Equipment Companion", pady=30, font=("Times New Roman", 20))

class_title_label = Label(root, text="Character Class:", pady=15)
class_label = Label(root, text=current_class)
class_button = Button(root, text="Choose a Class", command=openClassSelection)
class_pic_import = Image.open("C:\CS361\DnD-Project\Class-Images\Barbarian.png")
class_pic_resize = class_pic_import.resize((210,309))
class_pic = ImageTk.PhotoImage(class_pic_resize)
class_portrait = Label(image=class_pic)

weapon_title_label = Label(root, text="Weapons:", pady=15)
weapon_add_button = Button(root, text="Add", command=openWeaponSelection)

armor_title_label = Label(root, text="Armor:", pady=15)
armor_add_button = Button(root, text="Add", command=openArmorSelection)

compare_button = Button(root, text="Compare Items")
check_button = Button(root, text="Check Proficiency")
reset_button = Button(root, text="Reset Character")
help_button = Button(root, text="Help")

# Laying out the Elements
title_label.grid(row=0, column=0, columnspan=4)
class_title_label.grid(row=1, column=0)
class_label.grid(row=2, column=0)
class_portrait.grid(row=1, column=3, columnspan=3, rowspan=7)
class_button.grid(row=2, column=1)
weapon_title_label.grid(row=3, column=0)
weapon_add_button.grid(row=6, column=0)
armor_title_label.grid(row=7, column=0)
armor_add_button.grid(row=10, column=0)
compare_button.grid(row=11, column=0, padx=10, pady=20)
check_button.grid(row=11, column=1, padx=10, pady=20)
reset_button.grid(row=11, column=2, padx=10, pady=20)
help_button.grid(row=11, column=3, padx=10, pady=20)

# Runs tkinter
root.mainloop()