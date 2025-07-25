import tkinter as tk


form = tk.Tk()

form.title('Entry Dersi')
form.geometry('500x450+350+75')


giris = tk.Entry(fg='white', bg='black')
giris.pack(side=tk.LEFT)
giris2=tk.Entry(fg='red',bg='white')
giris2.pack(side=tk.RIGHT)



















form.mainloop()