import tkinter as tk 
import random as rd

form = tk.Tk()
form.geometry('500x500+350+75')
form.title('Deneme')

liste = []

for i in range(5):
    while len(liste) != 6:
        a = rd.randint(0,50)
        if a not in liste:
            liste.append(a)

def göster():
    label.config(text=liste, bg='green')

def saydamlaştır():
    form.wm_attributes('-alpha',0.3)


def döndür():
    form.wm_attributes('-alpha',0.9)

def MaxYap():
    form.state('zoomed')

def MinYap():
    form.state('iconic')


label = tk.Label(form,fg='red',bg='yellow')
label.pack()


göster= tk.Button(form,text='göster',fg='black',bg='white',command=göster)
göster.pack(side=tk.LEFT)


saydamlaştır= tk.Button(form,text='Saydamlaştır',fg='black',bg='white',command=saydamlaştır)
saydamlaştır.pack(side=tk.LEFT)


döndür= tk.Button(form,text='Döndür',fg='black',bg='white',command=döndür)
döndür.pack(side=tk.LEFT)


MaxYap= tk.Button(form,text='Maxyap',fg='black',bg='white',command=MaxYap)
MaxYap.pack(side=tk.RIGHT)


MinYap= tk.Button(form,text='Minyap',fg='black',bg='white',command=MinYap)
MinYap.pack(side=tk.RIGHT)




form.mainloop()