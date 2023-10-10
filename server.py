import socket
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

sock = socket.socket()
sock.bind(('', 3139))
sock.listen(1)
conn, addr = sock.accept()

print ('connected:', addr)

i=['C:/Users/User/Pictures/istockphoto-974079490-612x612.jpg',"C:/Users/User/Pictures/scuba diving.jpg"]
j=0
while True:

    data = conn.recv(1024)

    if not data:
        break
    # im2 = ImageTk.PhotoImage(im2)
    # l = Label(image=im2)
    # l.image = im2
    # l.place(x=0, y=0)
    root = Tk()
    root.title('картинка')
    root.geometry('800x800')
    root.resizable(0, 0)
    root.config(bg='black')

    im1 = Image.open(i[j%2])

    im1 = ImageTk.PhotoImage(im1)
    l = Label(image=im1)
    l.image = im1
    l.place(x=0, y=0)
    root.mainloop()


    #conn.send(data)

conn.close()


