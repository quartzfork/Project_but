import socket
from tkinter import *
from PIL import Image, ImageTk


sock = socket.socket()
sock.bind(('', 3139))
sock.listen(1)
conn, addr = sock.accept()

i=['C:/Users/User/Downloads/imgonline-com-ua-Resize-qEmDNe6eob97tMzx.jpg',"C:/Users/User/Downloads/imgonline-com-ua-Resize-e4P23QGX3VTk.jpg"]
j=0

while True:
    data = conn.recv(1024)

    root = Tk()
    root.title('картинка')
    root.geometry('450x600+500+100')
    root.resizable(0, 0)
    root.config(bg='black')
    size = (600, 600)
    im1 = Image.open(i[j % 2])
    im1 = ImageTk.PhotoImage(im1)
    l = Label(image=im1)
    l.image = im1
    l.place(x=0, y=0)
    root.after(1300, lambda: root.destroy())

    root.mainloop()

    if not data:
        break
    if data:
        j+=1

conn.close()

