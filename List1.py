from tkinter import *
import random

root = Tk()

root.title("Luck friend wheel")
root.geometry("500x500")

list1 = ["Aaron", "Ayaan", "Amol", "Bisman", "Niska", "Rudra"]
print(list1)

def randomNumber():
    random_no = random.randint(0,4)
    print(random_no)
    random_lucky_friend = list1[random_no]
    print("Your lucky friend is : " + random_lucky_friend)


btn = Button(root)
btn = Button(root, text="Who is your lucky friend?", command=randomNumber)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()