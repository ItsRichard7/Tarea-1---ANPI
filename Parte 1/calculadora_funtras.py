from tkinter import *
from funtras import *

class Interfaz:
    
    def __init__(self, ventana): # Constructor de la clase Interfaz
        #Inicializar la ventana con un título
        self.ventana = ventana
        self.ventana.title("Calculadora FunTras")
        self.ventana.geometry("390x610")
        self.ventana.resizable(False, False)
        self.ventana.configure(background="#1f1f1f")
        icono = PhotoImage(file="Parte 1\iconoCal.png")
        self.ventana.iconphoto(True, icono)

        #Agregar una caja de texto para que sea la pantalla de la calculadora
        self.pantalla = Text(self.ventana, font=('arial',23,'bold'), bd = 20, bg = "powder blue")
        self.pantalla.place(x = 20, y = 20, width = 350, height = 80)

        self.textoX = Label(self.ventana, text="Variable X =", justify= "center", font=("Bahnschrift", 13, "bold"), bg="#6c7073", borderwidth=6, relief="groove")
        self.textoX.place(x = 20, y = 120, width = 120, height = 50)
        
        self.entradaX = Text(self.ventana, font=('arial',16,'bold'), bd=10, bg="powder blue", )
        self.entradaX.place(x = 150, y = 120, width = 220, height = 50)

        self.textoY = Label(self.ventana, text="Variable Y =", justify= "center", font=("Bahnschrift", 13, "bold"), bg="#6c7073", borderwidth=6, relief="groove")
        self.textoY.place(x=20, y=180, width=120, height=50)
        
        self.entradaY = Text(self.ventana, font=('arial', 16, 'bold'), bd=10, bg="powder blue")
        self.entradaY.place(x = 150, y = 180, width = 220, height = 50)

        #Crear los botones de la calculadora
        self.botonReset = Button(self.ventana, font = ('arial', 16, 'bold') , text = "Reiniciar", bg="#f6f6f6", command= self.reiniciar, bd=3)
        self.botonReset.place(x=55, y=240, width=190, height=50)

        self.botonSenh = Button(self.ventana, font = ('arial', 12, 'bold') , text = "senh(x)", bg="#f6f6f6", command= self.calcSenh, bd=3)
        self.botonSenh.place(x=255, y=240, width=80, height=50)

        self.botonCosh = Button(self.ventana, font = ('arial', 12, 'bold') , text = "cosh(x)", bg="#f6f6f6", command= self.calcCosh, bd=3)
        self.botonCosh.place(x=20, y=300, width=80, height=50)

        self.botonTanh = Button(self.ventana, font = ('arial', 12, 'bold') , text = "tanh(x)", bg="#f6f6f6", command= self.calcTanh, bd=3)
        self.botonTanh.place(x=110, y=300, width=80, height=50)

        self.botonAsen = Button(self.ventana, font = ('arial', 12, 'bold') , text = "asen(x)", bg="#f6f6f6", command= self.calcAsen, bd=3)
        self.botonAsen.place(x=200, y=300, width=80, height=50)

        self.botonAcos = Button(self.ventana, font = ('arial', 12, 'bold') , text = "acos(x)", bg="#f6f6f6", command= self.calcAcos, bd=3)
        self.botonAcos.place(x=290, y=300, width=80, height=50)

        self.botonAtan = Button(self.ventana, font = ('arial', 12, 'bold') , text = "atan(x)", bg="#f6f6f6", command= self.calcAtan, bd=3)
        self.botonAtan.place(x=20, y=360, width=80, height=50)

        self.botonSec = Button(self.ventana, font = ('arial', 12, 'bold') , text = "sec(x)", bg="#f6f6f6", command= self.calcSec, bd=3)
        self.botonSec.place(x=110, y=360, width=80, height=50)

        self.botonCsc = Button(self.ventana, font = ('arial', 12, 'bold') , text = "csc(x)", bg="#f6f6f6", command= self.calcCsc, bd=3)
        self.botonCsc.place(x=200, y=360, width=80, height=50)

        self.botonCot = Button(self.ventana, font = ('arial', 12, 'bold') , text = "cot(x)", bg="#f6f6f6", command= self.calcCot, bd=3)
        self.botonCot.place(x=290, y=360, width=80, height=50)

        self.botonSen = Button(self.ventana, font = ('arial', 12, 'bold') , text = "sen(x)", bg="#f6f6f6", command= self.calcSen, bd=3)
        self.botonSen.place(x=20, y=420, width=80, height=50)

        self.botonCos = Button(self.ventana, font = ('arial', 12, 'bold') , text = "cos(x)", bg="#f6f6f6", command= self.calcCos, bd=3)
        self.botonCos.place(x=110, y=420, width=80, height=50)

        self.botonTan = Button(self.ventana, font = ('arial', 12, 'bold') , text = "tan(x)", bg="#f6f6f6", command= self.calcTan, bd=3)
        self.botonTan.place(x=200, y=420, width=80, height=50)

        self.botonLn = Button(self.ventana, font = ('arial', 12, 'bold') , text = "ln(x)", bg="#f6f6f6", command= self.calcLn, bd=3)
        self.botonLn.place(x=290, y=420, width=80, height=50)

        self.botonlog10 = Button(self.ventana, font = ('arial', 12, 'bold') , text = "log₁₀(x)", bg="#f6f6f6", command= self.calcLog10, bd=3)
        self.botonlog10.place(x=20, y=480, width=80, height=50)

        self.botonlogy = Button(self.ventana, font = ('arial', 12, 'bold') , text = "logᵧ(x)", bg="#f6f6f6", command= self.calcLogy, bd=3)
        self.botonlogy.place(x=110, y=480, width=80, height=50)

        self.botonDiv = Button(self.ventana, font = ('arial', 12, 'bold') , text = "1/x", bg="#f6f6f6", command= self.calcDiv, bd=3)
        self.botonDiv.place(x=200, y=480, width=80, height=50)

        self.botonRaiz2 = Button(self.ventana, font = ('arial', 12, 'bold') , text = "√x", bg="#f6f6f6", command= self.calcSqrt, bd=3)
        self.botonRaiz2.place(x=290, y=480, width=80, height=50)

        self.botonRaizY = Button(self.ventana, font = ('arial', 12, 'bold') , text = "ʸ√x", bg="#f6f6f6", command= self.calcRoot, bd=3)
        self.botonRaizY.place(x=20, y=540, width=80, height=50)

        self.botonExp = Button(self.ventana, font = ('arial', 12, 'bold') , text = "exp(x)", bg="#f6f6f6", command= self.calcExp, bd=3)
        self.botonExp.place(x=110, y=540, width=80, height=50)

        self.botonEle = Button(self.ventana, font = ('arial', 12, 'bold') , text = "x^y", bg="#f6f6f6", command= self.calcPower, bd=3)
        self.botonEle.place(x=200, y=540, width=80, height=50)

        self.botonFact = Button(self.ventana, font = ('arial', 12, 'bold') , text = "x!", bg="#f6f6f6", command= self.calcFact, bd=3)
        self.botonFact.place(x=290, y=540, width=80, height=50)
    
    def reiniciar (self):
        self.pantalla.delete('1.0', END)
        self.entradaX.delete('1.0', END)
        self.entradaY.delete('1.0', END)

    def convFloat (self, input, widget):
        try: 
            value = float(input)
            return value
        except: 
            widget.delete('1.0', END)
            widget.insert(END, "Ins. núm. válido")

    def tomarX (self):
        input = self.convFloat(self.entradaX.get("1.0",END), self.entradaX)
        return input
    
    def tomarY (self):
        input = self.convFloat(self.entradaY.get("1.0",END), self.entradaY)
        return input
    
    def mostrarRes(self, res):
        self.pantalla.delete('1.0', END)
        self.pantalla.insert(END, str(res))
    
    def errorMat(self):
        self.pantalla.delete('1.0', END)
        self.pantalla.insert(END, "Error Matemático")
    
    def calcSenh(self):
        res = sinh_t(self.tomarX())
        if res == False: 
            self.entradaY.delete('1.0', END)
            self.errorMat()
        else: 
            self.entradaY.delete('1.0', END)
            self.mostrarRes(res)

    def calcCosh(self):
        res = cosh_t(self.tomarX())
        if res == False: 
            self.entradaY.delete('1.0', END)
            self.errorMat()
        else: 
            self.entradaY.delete('1.0', END)
            self.mostrarRes(res)
    
    def calcTanh(self):
        res = tanh_t(self.tomarX())
        if res == False: 
            self.entradaY.delete('1.0', END)
            self.errorMat()
        else: 
            self.entradaY.delete('1.0', END)
            self.mostrarRes(res)

    def calcAsen(self):
        res = asin_t(self.tomarX())
        if res == False: 
            self.entradaY.delete('1.0', END)
            self.errorMat()
        else: 
            self.entradaY.delete('1.0', END)
            self.mostrarRes(res)

    def calcAcos(self):
        res = acos_t(self.tomarX())
        if res == False: 
            self.entradaY.delete('1.0', END)
            self.errorMat()
        else: 
            self.entradaY.delete('1.0', END)
            self.mostrarRes(res)  

    def calcAtan(self):
        res = atan_t(self.tomarX())
        if res == False: 
            self.entradaY.delete('1.0', END)
            self.errorMat()
        else: 
            self.entradaY.delete('1.0', END)
            self.mostrarRes(res)    

    def calcSec(self):
        res = sec_t(self.tomarX())
        if res == False: 
            self.entradaY.delete('1.0', END)
            self.errorMat()
        else: 
            self.entradaY.delete('1.0', END)
            self.mostrarRes(res)  

    def calcCsc(self):
        res = csc_t(self.tomarX())
        if res == False: 
            self.entradaY.delete('1.0', END)
            self.errorMat()
        else: 
            self.entradaY.delete('1.0', END)
            self.mostrarRes(res)    
  
    def calcCot(self):
        res = cot_t(self.tomarX())
        if res == False: 
            self.entradaY.delete('1.0', END)
            self.errorMat()
        else: 
            self.entradaY.delete('1.0', END)
            self.mostrarRes(res)   

    def calcSen(self):
        res = sen_t(self.tomarX())
        if res == False: 
            self.entradaY.delete('1.0', END)
            self.errorMat()
        else: 
            self.entradaY.delete('1.0', END)
            self.mostrarRes(res)   

    def calcCos(self):
        res = cos_t(self.tomarX())
        if res == False: 
            self.entradaY.delete('1.0', END)
            self.errorMat()
        else: 
            self.entradaY.delete('1.0', END)
            self.mostrarRes(res)   

    def calcTan(self):
        res = tan_t(self.tomarX())
        if res == False: 
            self.entradaY.delete('1.0', END)
            self.errorMat()
        else: 
            self.entradaY.delete('1.0', END)
            self.mostrarRes(res)   

    def calcLn(self):
        res = ln_t(self.tomarX())
        if res == False: 
            self.entradaY.delete('1.0', END)
            self.errorMat()
        else: 
            self.entradaY.delete('1.0', END)
            self.mostrarRes(res)  

    def calcLog10(self):
        res = log_t(self.tomarX(), 10)
        if res == False: 
            self.entradaY.delete('1.0', END)
            self.errorMat()
        else: 
            self.entradaY.delete('1.0', END)
            self.mostrarRes(res)    

    def calcLogy(self):
        res = log_t(self.tomarX(), self.tomarY())
        if res == False: self.errorMat()
        else: 
            self.mostrarRes(res)

    def calcDiv(self):
        res = div_t(self.tomarX())
        if res == False: 
            self.entradaY.delete('1.0', END)
            self.errorMat()
        else: 
            self.entradaY.delete('1.0', END)
            self.mostrarRes(res)

    def calcSqrt(self):
        res = sqrt_t(self.tomarX())
        if res == False: 
            self.entradaY.delete('1.0', END)
            self.errorMat()
        else: 
            self.entradaY.delete('1.0', END)
            self.mostrarRes(res)

    def calcRoot(self):
        res = root_t(self.tomarX(), (self.tomarY()))
        if res == False: self.errorMat()
        else: 
            self.mostrarRes(res)

    def calcExp(self):
        res = exp_t(self.tomarX())
        if res == False: 
            self.entradaY.delete('1.0', END)
            self.errorMat()
        else: 
            self.entradaY.delete('1.0', END)
            self.mostrarRes(res)

    def calcPower(self):
        res = power_t(self.tomarX(), self.tomarY())
        if res == False: self.errorMat()
        else: 
            self.mostrarRes(res)

    def calcFact(self):
        val = self.tomarX()
        if not float.is_integer(val) or val < 0: 
            self.entradaY.delete('1.0', END)
            self.errorMat()
        else: 
            self.entradaY.delete('1.0', END)
            self.mostrarRes(factorial(val))

#------------------ Final de la Clase Interfaz --------------------
 
# Inicio de la Aplicacion Instanciando una nueva calculadora
ventana = Tk()
calculadora = Interfaz(ventana)
ventana.mainloop()
