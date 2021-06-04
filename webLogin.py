import tkinter as tk


def importCSV(usernames, passwords):
    with open('CSV/logins.csv', 'r') as file:
        for line in file.readlines():
            split = line.split(",")
            usernames.append(split[0])
            passwords.append(split[1][:-1])
        file.close()
        return usernames, passwords
        

def submitForm(usernames, passwords,  entryName, entryPassword):
    for itemNum in range(len(usernames)):
        if entryName.get() == usernames[itemNum] and entryPassword.get() == passwords[itemNum]:
            print("correct")
            exit() #continue program with login
        else:
            print("incorrect")
def createNew(usernames, passwords, root):
    root.destroy()
    root2 = tk.Tk()
    enterName = tk.Entry(root2)
    enterNameLabel = tk.Label(root2, text="Enter Username:")
    enterPassword = tk.Entry(root2, show="*")
    enterPasswordLabel = tk.Label(root2, text="Enter Password:")
    ConfirmPassword = tk.Entry(root2, show="*")
    ConfirmPasswordLabel = tk.Label(root2, text="Confirm Password:")
    ConfirmButton = tk.Button(root2,text="Submit",command= lambda: ConfirmNew(usernames, passwords, enterPassword, enterName, ConfirmPassword, root2))

    enterNameLabel.grid(row=0)
    enterName.grid(row=0,column=1)
    enterPasswordLabel.grid(row=1)
    enterPassword.grid(row=1,column=1)
    ConfirmPasswordLabel.grid(row=2)
    ConfirmPassword.grid(row=2, column=1)
    ConfirmButton.grid(row=3,column=1)
    root2.mainloop()


def ConfirmNew(usernames, passwords,enterPassword, enterName, ConfirmPassword, root2):
    if enterPassword.get() == ConfirmPassword.get():
        with open('CSV/logins.csv', 'a+', newline ='') as file: 
            from csv import writer
            writer = writer(file)
            row = enterName.get(),enterPassword.get()
            writer.writerow(row)
            root2.destroy()
            file.close()
            startMain()
            

def startMain():
    if __name__ == "__main__":
        usernames, passwords = [], []
        usernames, passwords = importCSV(usernames, passwords)
        root = tk.Tk()
        createButton = tk.Button(root, text="Create New", command= lambda: createNew(usernames, passwords, root))
        labelName = tk.Label(root, text="Username:")
        labelPassword = tk.Label(root, text="Password:")
        entryName = tk.Entry(root)
        entryPassword = tk.Entry(root, show="*")
        submit = tk.Button(root, text="Submit", command= lambda: submitForm(usernames, passwords, entryName, entryPassword))
        labelName.grid(row=0)
        labelPassword.grid(row=1)
        entryName.grid(row=0, column=1)
        entryPassword.grid(row=1,column=1)
        submit.grid(row=2, column=1)
        createButton.grid(row=2)
        root.mainloop()
startMain()
