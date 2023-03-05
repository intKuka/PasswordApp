
from tkinter.font import Font
from cgitb import text
from ctypes import alignment
from datetime import date
import customtkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from turtle import left, width
import json

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")
json_path = r"C:\Users\grafs\Desktop\assords\PasswordApp\info.json"
entry_dict = {}
with open(json_path, "r") as json_file:
    entry_dict=json.load(json_file)


class Entry:

    def __init__(self, name, password, tied_mail):
        self.name = name
        self.password = password
        self.prev_passwords = None
        self.tied_mail = tied_mail
        self.last_changed = date.today().strftime('%B %#d, %Y')

        entry_dict[self.name].append({
            "password": self.password,
            "prev_passwords": self.prev_passwords,
            "tied_mail": self.tied_mail,
            "last_changed": self.last_changed            
        }) 




root = customtkinter.CTk()
root.title("Copy Book")
root.minsize(550, 500)



def change_entry():
    messagebox.showinfo("Change", "succ thissss")

#separate creating and saving processes     
def save_entry(name, password, email):
    with open(json_path, "w") as json_file:        
        Entry(name, password, email)
        json.dump(entry_dict, json_file, indent=4, sort_keys=True)
    messagebox.showinfo("Done", "Mission is complited")



def remove_entry():
    messagebox.showinfo("Deletion", "Succ removed")

'''
def copy():
    messagebox.showinfo("Deletion", )
'''

def fill_list(list):
    list.insert(END, "line1")
    list.insert(END, "line2")
    list.insert(END, "line4")
    list.insert(END, "line3")

#move to a separate class
def open_adding_form():
    #window properties
    creation_window = customtkinter.CTkToplevel(root)
    creation_window.title("Create New")
    creation_window.geometry("300x400")

    #title
    customtkinter.CTkLabel(creation_window, text="New Entry").pack(pady=(5,30))

    #frame placement
    value_frame = customtkinter.CTkFrame(creation_window, corner_radius=0, fg_color="black", border_color="#101010", border_width=3)
    value_frame.pack(padx=10, pady=10, fill=X)

    frame2 = customtkinter.CTkFrame(creation_window, fg_color=None)
    frame2.pack(padx=20, pady=(40, 20), fill=X)

    #UI
    customtkinter.CTkLabel(value_frame, text="Name:").pack(pady=(0, 2), padx=(0,0))
    name_box = customtkinter.CTkEntry(value_frame, state='normal', width=35, height=1, corner_radius=0, placeholder_text="Title...")
    name_box.pack(pady=(0, 10), padx=10, fill=X)

    customtkinter.CTkLabel(value_frame, text="Password:").pack(pady=(0, 2), anchor="w")
    password_box = customtkinter.CTkEntry(value_frame, state='normal', width=35, height=1, corner_radius=0, placeholder_text="Your secret...")
    password_box.pack(pady=(0, 10), padx=10, fill=X)

    customtkinter.CTkLabel(value_frame, text="E-mail:").pack(pady=(0, 2), anchor="w")   
    email_box = customtkinter.CTkEntry(value_frame, state='normal', width=35, height=1, corner_radius=0, placeholder_text="e-mail...")
    email_box.pack(pady=(0, 10), padx=10, fill=X)
    
    customtkinter.CTkButton(frame2, text="Cancel", width=100, command=creation_window.destroy).pack(pady=(0, 10), padx=10)
    customtkinter.CTkButton(frame2, text="Save", width=100, command=lambda: save_entry(name_box.get(),
                                                                                       password_box.get(),
                                                                                       email_box.get())).pack(pady=(0, 10), padx=10)


list_box = customtkinter.CTkFrame(root, width=200, height=400)
list_box.grid(padx=10, pady=10, row=0, column=0, rowspan=2)

buttons_frame = customtkinter.CTkFrame(root, width=300, height=3)
buttons_frame.grid(padx=1, pady=1, row=0, column=1, sticky=N)

info_box = customtkinter.CTkFrame(root)
info_box.grid(padx=10, pady=10, row=1, column=1, sticky=N)


# List section
list = Listbox(list_box, selectmode=SINGLE, width=30, height=28)
list.pack()
fill_list(list)

# Buttons section
customtkinter.CTkButton(buttons_frame, text="Change", command=change_entry).pack(side=LEFT, padx=5)
customtkinter.CTkButton(buttons_frame, text="New", command=open_adding_form).pack(side=LEFT, padx=5)
customtkinter.CTkButton(buttons_frame, text="Remove", command=remove_entry).pack(side=LEFT, padx=5)

# Infobox section
customtkinter.CTkLabel(info_box, text="Name:").pack(anchor=W, pady=(0, 2))
customtkinter.CTkEntry(info_box, state='disabled', width=35, height=1).pack(pady=(0, 10))

customtkinter.CTkLabel(info_box, text=f"E-mail:").pack(anchor=W, pady=(0, 2))
customtkinter.CTkEntry(info_box, state='disabled', width=35, height=1).pack(pady=(0, 10))

customtkinter.CTkLabel(info_box, text="Last Changed:").pack(anchor=W, pady=(0, 2))
customtkinter.CTkEntry(info_box, state='disabled', width=35, height=1).pack(pady=(0, 10))

customtkinter.CTkLabel(info_box, text="Previous passwords:").pack(anchor=W, pady=(0, 2))




root.mainloop()



   

