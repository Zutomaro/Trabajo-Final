from tkinter import *
variable=Tk()
variable.geometry('500x500')
variable.config(bg='white')
variable.resizable(width=True,height=True)
variable.title('Menu')
etiqueta=Label(variable,text='Usuario:', font=('Arial',16)).place(x=10,y=50)
nombre=Entry(variable,bd=8,bg='white',show='*')
nombre.place(x=10,y=90)
etiquetaII=Label(variable,text='Contraseña:', font=('Arial',16)).place(x=10,y=130)
contra=Entry(variable,bd=8,bg='white',show='*')
contra.place(x=10,y=170)
etiquetaIII=Label(variable,text='Ping:', font=('Arial',16)).place(x=10,y=210)
pin=Entry(variable,bd=8,bg='white',show='*')
pin.place(x=10,y=250)
botonaceptar=Button(variable,text='Aceptar')
botonaceptar.place(x=10,y=290)
