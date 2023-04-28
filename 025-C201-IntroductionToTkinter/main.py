# Tkinter simple interest calculator

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Simple Interest Calculator")
root.geometry("400x400")

def calculate():
    principal = float(entry_principal.get())
    rate = float(entry_rate.get())
    time = float(entry_time.get())

    interest = (principal * rate * time) / 100

    messagebox.showinfo("Interest", f"Interest: {interest}")

principal_label = Label(root, text="Principal ($)")
principal_label.pack(pady=10)

entry_principal = Entry(root, width=30)
entry_principal.pack(pady=10)

rate_label = Label(root, text="Rate (% per annum)")
rate_label.pack(pady=10)

entry_rate = Entry(root, width=30)
entry_rate.pack(pady=10)

time_label = Label(root, text="Time (years)")
time_label.pack(pady=10)

entry_time = Entry(root, width=30)
entry_time.pack(pady=10)

btn_calculate = Button(root, text="Calculate", command=calculate)
btn_calculate.pack(pady=10)

root.mainloop()