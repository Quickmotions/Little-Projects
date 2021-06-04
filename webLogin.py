import tkinter as tk
import csv



def importCSV(usernames, passwords):
    with open('CSV/logins.csv', 'r') as file:
        for line in file.readlines():
            split = line.split(",")
            usernames.append(split[0])
            passwords.append(split[1][:-1])
        return usernames, passwords

            


def submitForm(usernames, passwords):
    for itemNum in range(len(usernames)):
        if entryName.get() == usernames[itemNum] and entryPassword.get() == passwords[itemNum]:
            print("correct")
            exit()
        else:
            print("incorrect")

if __name__ == "__main__":
    usernames, passwords = [], []
    usernames, passwords = importCSV(usernames, passwords)
    print(passwords,usernames)
    root = tk.Tk()
    labelName = tk.Label(root, text="Username:")
    labelPassword = tk.Label(root, text="Password:")
    entryName = tk.Entry(root)
    entryPassword = tk.Entry(root, show="*")
    submit = tk.Button(root, text="submit", command= lambda: submitForm(usernames, passwords))
    labelName.grid(row=0)
    labelPassword.grid(row=1)
    entryName.grid(row=0, column=1)
    entryPassword.grid(row=1,column=1)
    submit.grid(row=2, column=1)
    root.mainloop()
