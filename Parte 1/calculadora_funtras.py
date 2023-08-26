from tkinter import *
from funtras import *

class Interfaz:
    
    def __init__(self, ventana): # Constructor de la clase Interfaz
        #Inicializar la ventana con un título
        self.ventana = ventana
        self.ventana.title("Calculadora NumPy")
        self.ventana.geometry("390x690")
        self.ventana.resizable(False, False)
        self.ventana.configure(background="#1E0B05")

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

        """boton1 = self.crearBoton("senh(x)")
        boton2 = self.crearBoton("cosh(x)")
        boton3 = self.crearBoton("tanh(x)")
        boton4 = self.crearBoton("asen(x)")
        boton5 = self.crearBoton("acos(x)")
        boton6 = self.crearBoton("atan(x)")
        boton7 = self.crearBoton("sec(x)")
        boton8 = self.crearBoton("cos(x)")
        boton9 = self.crearBoton("tan(x)")
        boton10 = self.crearBoton("ln(x)")
        boton11 = self.crearBoton("log₁₀(x)")
        boton12 = self.crearBoton("logᵧ(x)")
        boton13 = self.crearBoton("1/x")
        boton14 = self.crearBoton("√x")
        boton15 = self.crearBoton("ʸ√x")
        boton16 = self.crearBoton("exp(x)")
        boton17 = self.crearBoton("x^y")
        boton18 = self.crearBoton("x!")

        #Ubicar los botones con el gestor grid
        botones = [boton1, boton2, boton3, boton4, boton5, boton6, boton7, 
                   boton8, boton9, boton10, boton11, boton12, boton13, boton14, boton15, boton16, boton17, boton18]
        contador = 0
        for fila in range(2,8):
            for columna in range(3):
                botones[contador].grid(row = fila , column = columna)
                contador += 1"""
        return
    
    def reiniciar (self):
        self.pantalla.delete('1.0', END)
        self.entradaX.delete('1.0', END)
        self.entradaY.delete('1.0', END)

#------------------ Final de la Clase Interfaz --------------------
 
# Inicio de la Aplicacion Instanciando una nueva calculadora
ventana = Tk()
calculadora = Interfaz(ventana)
ventana.mainloop()
