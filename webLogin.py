import tkinter as tk
import csv

def importCSV():
    


def submitForm():
    print(entryName.get(), entryPassword.get())

if __name__ == "__main__":
    importCSV()
    root = tk.Tk()
    labelName = tk.Label(root, text="Username:")
    labelPassword = tk.Label(root, text="Password:")
    entryName = tk.Entry(root)
    entryPassword = tk.Entry(root, show="*")
    submit = tk.Button(root, text="submit", command=submitForm)
    labelName.grid(row=0)
    labelPassword.grid(row=1)
    entryName.grid(row=0, column=1)
    entryPassword.grid(row=1,column=1)
    submit.grid(row=2, column=1)
    root.mainloop()
