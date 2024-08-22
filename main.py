from random import randint,shuffle,choice
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
BG_COL="#FBF5DF"
window=Tk()
window.title("Password Manager")
window.minsize(height=400,width=500)
window.config(padx=50,pady=50,bg=BG_COL)
password=""
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
    global password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list=password_letters+password_symbols+password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    pyperclip.paste()

# ---------------------------- SAVE PASSWORD ------------------------------- #
def search_data():
    web_name=website_entry.get()
    if len(web_name) == 0 :
        messagebox.showinfo(title="Password Manager", message="You have left website field empty")
    else:
        try:
            with open("pwd_data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Password Manager", message="No data File found")
        else:
            if web_name in data:
                # reading file
                em=data[web_name]["email"]
                pw=data[web_name]["password"]
                messagebox.showinfo(title=web_name, message=f"Email={em} \nPassword={pw}")
            else:
                messagebox.showinfo(title="Password Manager", message="Website data not found")



def save():
    website = website_entry.get()
    password =password_entry.get()
    email = email_entry.get()
    new_data={
        website:{
            "email":email,
            "password":password}}
    if len(password) == 0 or len(email) == 0 or len(website)==0:
        messagebox.showinfo(title="Password Manager", message="You have left fields empty")
    else:
        try:
            with open("pwd_data.json", "r") as data_file:
                #reading file
                data1=json.load(data_file)
        except FileNotFoundError:
            #if file is not created then exception handled
            with open("pwd_data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            #updating file
            data1.update(new_data)
            with open("pwd_data.json", "w") as data_file:
                json.dump(data1,data_file,indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
        messagebox.showinfo(title="Password Manager", message="Data saved successfully")


# ---------------------------- UI SETUP ------------------------------- #
#website entry
website_label = Label(text="Website : ",bg=BG_COL)
website_label.grid(row=1,column=0)

website_entry = Entry(window,width=25)
website_entry.focus()
website_entry.grid(row=1,column=1,pady=(0, 10))

#email entry
email_label = Label(text="Email/Username : ",bg=BG_COL)
email_label.grid(row=2,column=0)

email_entry = Entry(window,width=41)
email_entry.insert(0,"abc@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2,pady=(0, 10))

#password entry
password_label = Label(text="Password : ",bg=BG_COL)
password_label.grid(row=3,column=0)

password_entry= Entry(window,width=24)
password_entry.grid(row=3,column=1,pady=(0, 10),padx=(0, 10))

#generate pwd button
generate_button=Button(text="Generate Pwd",bg="white",command=generate_pwd,width=12)
generate_button.grid(row=3,column=2,pady=(0, 10))

#add button
add_button=Button(text="ADD",bg="white",width=35,command=save)
add_button.grid(row=4,column=1,columnspan=2)

#search button
search_button=Button(text="Search",bg="white",width=12,command=search_data)
search_button.grid(row=1,column=2,pady=(0, 10))

canvas=Canvas(width=200,height=200,bg=BG_COL,highlightthickness=0)
pwd_icon=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=pwd_icon)
canvas.grid(column=1,row=0)



#data_dict={"website":}




window.mainloop()