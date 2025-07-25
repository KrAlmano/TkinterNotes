import tkinter as tk

form = tk.Tk()
form.geometry('500x500')
label = tk.Label(text='Geometri Denemeleri')
label.pack()

buton = tk.Button(text='Bas')
buton.pack(side=tk.LEFT)


form.mainloop()