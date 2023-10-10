import socket
from tkinter import *
import time

#sock.close()

def button_prog():
    # sock = socket.socket()
    # sock.connect(('192.168.43.112', 3139))

    def click():
        print('hhhhh')
        # sock.send(b'u')
        # btn.config(text="Ждите")
        time.sleep(1)
        # btn.config(text="Жмите")


    root = Tk()
    root.title('Кнопка')

    root.resizable(width=False, height=False)
    root.config(bg='black')
    root.eval('tk::PlaceWindow . center')

    btn = Button(root, text='Жмите', command=click, font=('Comic Sans MS', 40), bg='dark green',
                 activebackground='gray')
    btn.pack()
    root.mainloop()

button_prog()

