from tkinter import *
class tela:
    def __init__(self):
        self.main = Tk()
        self.bt = Button(self.main, text= "Print")
        self.lb = Label(self.main, text="OI")
    def imprimir(self):
        print(self.lb["text"])
    def construir(self):
        self.main.geometry("100x100")
        self.lb.place(x=10,y=20)
        self.bt["command"] = self.imprimir
        self.bt.place(x=10,y=50)
        self.main.mainloop()
root = Tk()
root.geometry("600x600")
marge = 40
x=200
y=200
root["bg"] = "Black"
imagem = PhotoImage(file="C:/Users/User/Pictures/Saved Pictures/586211933-free-live-matrix-wallpaper.png")
bt1 = Button(root,text="Ok",image=imagem,width=100,height=150)
bt2 = Button(root,text="Ok",image=imagem,width=100,height=150)
bt3 = Button(root,text="Ok",image=imagem,width=100,height=150)
bt4 = Button(root,text="Ok",image=imagem,width=100,height=150)
bt5 = Button(root,text="Ok",image=imagem,width=100,height=150)
l = [[bt1,bt2,bt3],[bt4,bt5]]
for elem in range(len(l)):
    for column in range(len(l[elem])):
        l[elem][column].place(x=x*column+marge,y=y*elem+marge)

lb = Label(root,bg="Black",height=10)
lb.pack(side=BOTTOM, fill=X)

bt5 = Button(lb,text="Ok")
bt6 = Button(lb,text="Ok")
bt7 = Button(lb,text="Ok")
bt8 = Button(lb,text="Ok")
o = [[bt5,bt6,bt7],[bt8]]
marge = 0
x = 1
y = 1
for elem in range(len(o)):
    for column in range(len(l[elem])):
        l[elem][column].place(x=x*column+marge,y=y*elem+marge)
root.mainloop()