import socket
from threading import *
from tkinter import *
from tkinter import ttk


# import tkinter as tk


# def socket_prog():
#     sock = socket.socket()
#     sock.connect(('192.168.43.112', 3139))
#     while True:
#         if n == True:
#             sock.send(b'hello, world!')
#
#     data = sock.recv(1024)
#     #sock.close()
#     print(data)

def button_prog():
    sock = socket.socket()
    sock.connect(('192.168.43.112', 3139))

    def click():
        print('hhhhh')
        sock.send(b'u')

    root = Tk()
    root.title('Кнопка')

    # btn.tag_configure("center", justify='center')
    # btn.insert("1.0", "text")
    # btn.tag_add("center", "1.0", "end")
    # btn.pack()

    root.resizable(width=False, height=False)
    root.config(bg='black')
    btn = Button(root, text='Нажать', command=click, font=('Comic Sans MS', 40), bg='lime',
                 activebackground='gray')

    # btn.tag_configure("center", justify='center')
    # btn.insert("1.0", "text")
    # btn.tag_add("center", "1.0", "end")

    btn.pack()
    root.mainloop()


# t1 = Thread(target = button_prog)
# t2 = Thread(target = socket_prog)

button_prog()
# socket_prog()
# t1.start()
# t2.start()