from tkinter import *
from funtras import *

class Interfaz:
    
    def __init__(self, ventana): # Constructor de la clase Interfaz
        #Inicializar la ventana con un título
        self.ventana = ventana
        self.ventana.title("Calculadora NumPy")
        self.ventana.geometry("390x620")
        self.ventana.resizable(False, False)
        self.ventana.configure(background="#1f1f1f")

        #Agregar una caja de texto para que sea la pantalla de la calculadora
        self.pantalla = Text(self.ventana, font=('arial',23,'bold'), bd = 20, bg = "powder blue")
        self.pantalla.place(x = 20, y = 20, width = 350, height = 80)

        self.textoX = Label(self.ventana, text="Variable X =", justify= "center", font=("Helvetica", 13, "bold"), bg="#6c7073", borderwidth=6, relief="groove")
        self.textoX.place(x = 20, y = 120, width = 120, height = 50)
        
        self.entradaX = Text(self.ventana, font=('arial',16,'bold'), bd=10, bg="powder blue", )
        self.entradaX.place(x = 150, y = 120, width = 220, height = 50)

        self.textoY = Label(self.ventana, text="Variable Y =", justify= "center", font=("Helvetica", 13, "bold"), bg="#6c7073", borderwidth=6, relief="groove")
        self.textoY.place(x=20, y=180, width=120, height=50)
        
        self.entradaY = Text(self.ventana, font=('arial', 16, 'bold'), bd=10, bg="powder blue")
        self.entradaY.place(x = 150, y = 180, width = 220, height = 50)

        #Crear los botones de la calculadora
        self.botonReset = Button(self.ventana, font = ('arial', 16, 'bold') , text = "Reiniciar", bg="#f6f6f6", command= self.reiniciar, bd=3)
        self.botonReset.place(x=100, y=240, width=190, height=50)

        self.botonSenh = Button(self.ventana, font = ('arial', 12, 'bold') , text = "senh(x)", bg="#f6f6f6", command= self.reiniciar, bd=3)
        self.botonSenh.place(x=20, y=310, width=80, height=50)

        self.botonCosh = Button(self.ventana, font = ('arial', 12, 'bold') , text = "cosh(x)", bg="#f6f6f6", command= self.reiniciar, bd=3)
        self.botonCosh.place(x=110, y=310, width=80, height=50)

        self.botonTanh = Button(self.ventana, font = ('arial', 12, 'bold') , text = "tanh(x)", bg="#f6f6f6", command= self.reiniciar, bd=3)
        self.botonTanh.place(x=200, y=310, width=80, height=50)

        self.botonAsen = Button(self.ventana, font = ('arial', 12, 'bold') , text = "asen(x)", bg="#f6f6f6", command= self.reiniciar, bd=3)
        self.botonAsen.place(x=290, y=310, width=80, height=50)

        self.botonAcos = Button(self.ventana, font = ('arial', 12, 'bold') , text = "acos(x)", bg="#f6f6f6", command= self.reiniciar, bd=3)
        self.botonAcos.place(x=20, y=370, width=80, height=50)

        self.botonAtan = Button(self.ventana, font = ('arial', 12, 'bold') , text = "atan(x)", bg="#f6f6f6", command= self.reiniciar, bd=3)
        self.botonAtan.place(x=110, y=370, width=80, height=50)

        self.botonSec = Button(self.ventana, font = ('arial', 12, 'bold') , text = "sec(x)", bg="#f6f6f6", command= self.reiniciar, bd=3)
        self.botonSec.place(x=200, y=370, width=80, height=50)

        self.botonCsc = Button(self.ventana, font = ('arial', 12, 'bold') , text = "csc(x)", bg="#f6f6f6", command= self.reiniciar, bd=3)
        self.botonCsc.place(x=290, y=370, width=80, height=50)

        self.botonCot = Button(self.ventana, font = ('arial', 12, 'bold') , text = "cot(x)", bg="#f6f6f6", command= self.reiniciar, bd=3)
        self.botonCot.place(x=20, y=430, width=80, height=50)

        self.botonSen = Button(self.ventana, font = ('arial', 12, 'bold') , text = "sen(x)", bg="#f6f6f6", command= self.reiniciar, bd=3)
        self.botonSen.place(x=110, y=430, width=80, height=50)

        self.botonTan = Button(self.ventana, font = ('arial', 12, 'bold') , text = "tan(x)", bg="#f6f6f6", command= self.reiniciar, bd=3)
        self.botonTan.place(x=200, y=430, width=80, height=50)

        self.botonLn = Button(self.ventana, font = ('arial', 12, 'bold') , text = "ln(x)", bg="#f6f6f6", command= self.reiniciar, bd=3)
        self.botonLn.place(x=290, y=430, width=80, height=50)

        self.botonlog10 = Button(self.ventana, font = ('arial', 12, 'bold') , text = "log₁₀(x)", bg="#f6f6f6", command= self.reiniciar, bd=3)
        self.botonlog10.place(x=20, y=490, width=80, height=50)

        self.botonlogy = Button(self.ventana, font = ('arial', 12, 'bold') , text = "logᵧ(x)", bg="#f6f6f6", command= self.reiniciar, bd=3)
        self.botonlogy.place(x=110, y=490, width=80, height=50)

        self.botonDiv = Button(self.ventana, font = ('arial', 12, 'bold') , text = "1/x", bg="#f6f6f6", command= self.reiniciar, bd=3)
        self.botonDiv.place(x=200, y=490, width=80, height=50)

        self.botonRaiz2 = Button(self.ventana, font = ('arial', 12, 'bold') , text = "√x", bg="#f6f6f6", command= self.reiniciar, bd=3)
        self.botonRaiz2.place(x=290, y=490, width=80, height=50)

        self.botonRaizY = Button(self.ventana, font = ('arial', 12, 'bold') , text = "ʸ√x", bg="#f6f6f6", command= self.reiniciar, bd=3)
        self.botonRaizY.place(x=20, y=550, width=80, height=50)

        self.botonExp = Button(self.ventana, font = ('arial', 12, 'bold') , text = "exp(x)", bg="#f6f6f6", command= self.reiniciar, bd=3)
        self.botonExp.place(x=110, y=550, width=80, height=50)

        self.botonEle = Button(self.ventana, font = ('arial', 12, 'bold') , text = "x^y", bg="#f6f6f6", command= self.reiniciar, bd=3)
        self.botonEle.place(x=200, y=550, width=80, height=50)

        self.botonFact = Button(self.ventana, font = ('arial', 12, 'bold') , text = "x!", bg="#f6f6f6", command= self.reiniciar, bd=3)
        self.botonFact.place(x=290, y=550, width=80, height=50)
    
    def reiniciar (self):
        self.pantalla.delete('1.0', END)
        self.entradaX.delete('1.0', END)
        self.entradaY.delete('1.0', END)

#------------------ Final de la Clase Interfaz --------------------
 
# Inicio de la Aplicacion Instanciando una nueva calculadora
ventana = Tk()
calculadora = Interfaz(ventana)
ventana.mainloop()
