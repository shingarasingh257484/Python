from tkinter import *
from tkinter import messagebox

# Initialize window
root = Tk()
root.geometry('700x550')
root.config(bg='#d3f3f5')
root.title('Shingara Contact Book')
root.resizable(0, 0)

contactlist = [
    ['Siddharth Nigam', '9854746512'],
    ['Gaurav Patil', '8211575222'],
    ['Abhishek Nikam', '7894506614'],
    ['Sakshi Gaikwad', '9588745246'],
    ['Mohit Paul', '7095846975'],
    ['Karan Patel', '6850647892'],
    ['Sam Sharma', '8978685320'],
    ['John Maheshwari', '9856489785'],
    ['Ganesh Pawar', '8567967412'],
    ['Shingara Singh','6280778872']
]

Name = StringVar()
Number = StringVar()

# Create frame
frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Times new roman', 16), bg="#f0fffc", width=20, height=20, borderwidth=3, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)

# Function to get selected value
def Selected():
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please Select the Name")
    else:
        return int(select.curselection()[0])

# Function to add new contact
def AddContact():
    if Name.get() != "" and Number.get() != "":
        contactlist.append([Name.get(), Number.get()])
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Successfully Add New Contact")
    else:
        messagebox.showerror("Error", "Please fill the information")

# Function to update contact details
def UpdateDetail():
    if Name.get() and Number.get():
        contactlist[Selected()] = [Name.get(), Number.get()]
        messagebox.showinfo("Confirmation", "Successfully Update Contact")
        EntryReset()
        Select_set()
    elif not Name.get() and not Number.get() and not len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please fill the information")
    else:
        if len(select.curselection()) == 0:
            messagebox.showerror("Error", "Please Select the Name and \n press Load button")
        else:
            message1 = """To Load the all information of \n selected row press Load button\n."""
            messagebox.showerror("Error", message1)

# Function to delete contact entry
def Delete_Entry():
    if len(select.curselection()) != 0:
        result = messagebox.askyesno('Confirmation', 'You Want to Delete Contact\n Which you selected')
        if result:
            del contactlist[Selected()]
            Select_set()
    else:
        messagebox.showerror("Error", 'Please select the Contact')

# Function to view selected contact
def VIEW():
    NAME, PHONE = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)

# Function to reset entry fields
def EntryReset():
    Name.set("")
    Number.set("")

# Function to exit application
def EXIT():
    root.destroy()

# Function to update listbox
def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for name, phone in contactlist:
        select.insert(END, name)

Select_set()

# Define buttons, labels, and entry widgets
Label(root, text='Name', font=("Times new roman", 22, "bold"), bg='SlateGray3').place(x=30, y=20)
Entry(root, textvariable=Name, width=30).place(x=200, y=30)
Label(root, text='Contact No.', font=("Times new roman", 20, "bold"), bg='SlateGray3').place(x=30, y=70)
Entry(root, textvariable=Number, width=30).place(x=200, y=80)

Button(root, text=" ADD", font='Helvetica 18 bold', bg='#e8c1c7', command=AddContact, padx=20).place(x=50, y=140)
Button(root, text="EDIT", font='Helvetica 18 bold', bg='#e8c1c7', command=UpdateDetail, padx=20).place(x=50, y=200)
Button(root, text="DELETE", font='Helvetica 18 bold', bg='#e8c1c7', command=Delete_Entry, padx=20).place(x=50, y=260)
Button(root, text="VIEW", font='Helvetica 18 bold', bg='#e8c1c7', command=VIEW).place(x=50, y=325)
Button(root, text="RESET", font='Helvetica 18 bold', bg='#e8c1c7', command=EntryReset).place(x=50, y=390)
Button(root, text="EXIT", font='Helvetica 24 bold', bg='tomato', command=EXIT).place(x=250, y=470)

# Function to get selected value
def Selected():
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please select a contact")
        return None
    return int(select.curselection()[0])

# Function to add new contact with duplicate check
def AddContact():
    if Name.get() and Number.get():
        if any(contact[0] == Name.get() or contact[1] == Number.get() for contact in contactlist):
            messagebox.showerror("Error", "Contact already exists")
        else:
            contactlist.append([Name.get(), Number.get()])
            Select_set()
            EntryReset()
            messagebox.showinfo("Confirmation", "Successfully added new contact")
    else:
        messagebox.showerror("Error", "Please fill out all information")

# Function to update contact details
def UpdateDetail():
    index = Selected()
    if index is not None and Name.get() and Number.get():
        contactlist[index] = [Name.get(), Number.get()]
        messagebox.showinfo("Confirmation", "Successfully updated contact")
        EntryReset()
        Select_set()
    elif index is None:
        messagebox.showerror("Error", "Please select a contact to update")
    else:
        messagebox.showerror("Error", "Please fill out all information")

# Function to view selected contact
def VIEW():
    index = Selected()
    if index is not None:
        NAME, PHONE = contactlist[index]
        Name.set(NAME)
        Number.set(PHONE)


root.mainloop()
