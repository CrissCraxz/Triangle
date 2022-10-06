
from tkinter import *
from tkinter import messagebox

#Ejercicio de triangulo
#Codigo Fuente 


def type_triangle():

    
    if ((a.get()+b.get()) > c.get() and (a.get()+c.get()) > b.get() and (b.get()+c.get()) > a.get()) and (a.get().is_integer() and b.get().is_integer() and c.get().is_integer()) and (a.get()>0 and b.get()>0 and c.get()>0):
      
        messageRta = "Ingreso correcto " 
        if (a.get() ==b.get() and a.get()==c.get()):
            messageTipo = "Es un Triangulo Equilatero"
           
        elif (a.get() != b.get() and a.get() != c.get()):
            messageTipo = "Es un Triangulo Escaleno"
            
        else:
            messageTipo = "Es un Triangulo Isoceles"
            
        messagebox.showinfo(message=messageTipo,title=messageRta)       
            
        
    else:
        
        messageRta = "No es triangulo, ingreso incorrecto, vuelva a ingresar sus datos"
        messagebox.showerror(message=messageRta)
   


#interfaz grafica 

interfaz = Tk()
interfaz.geometry("380x180+790+480")
interfaz.title("Triangulos")


lblA= Label(text="Ingrese el primer lado del triangulo: ").grid(row=0,column=0)
a= DoubleVar()
txtA= Entry(textvariable=a).grid(row=0,column=1)

lblB= Label(text="Ingrese el segundo lado del triangulo: ").grid(row=1,column=0)
b= DoubleVar()
txtB= Entry(textvariable=b).grid(row=1,column=1)

lblC= Label(text="Ingrese el tercer lado del triangulo: ").grid(row=2,column=0)
c= DoubleVar()
txtC= Entry(textvariable=c).grid(row=2,column=1)

btnComprobar = Button(text="Comprobar", command=type_triangle).place(x=130,y=80)
interfaz.mainloop()