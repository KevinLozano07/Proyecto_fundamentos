from tkinter import *

# Genera la pantalla
Pantalla = Tk()
Pantalla.title("Calculadora de FFMI")
Pantalla.resizable(False, False)
Pantalla.iconbitmap("Calculator.ico")
Pantalla.geometry("800x500")
Pantalla.config(background='#7cdaf9')

Cuadro = Frame(Pantalla)
Cuadro.pack(side="left")
Cuadro.config(background='#f6f7f9', width="700", height="450")
Cuadro.config(highlightbackground="black", highlightthickness=1.5)

Titulo = Label(Cuadro, text="Calculadora", background='#f6f7f9', font=("Arial", 15))
Titulo.place(x=20, y=20)

Estatura = Label(Cuadro, text="Ingrese su altura en metros:", background='#f6f7f9', font=("Arial", 11))
Estatura.place(x=20, y=70)
Cuadro_estatura = Entry(Cuadro)
Cuadro_estatura.place(x=210, y=72)

Kilos = Label(Cuadro, text="Ingrese su peso en kilos:", background='#f6f7f9', font=("Arial", 11))
Kilos.place(x=20, y=110)
Cuadro_kilos = Entry(Cuadro)
Cuadro_kilos.place(x=190, y=112)

Grasa = Label(Cuadro, text="Ingrese su porcentaje graso:", background='#f6f7f9', font=("Arial", 11))
Grasa.place(x=20, y=150)
Cuadro_Grasa = Entry(Cuadro)
Cuadro_Grasa.place(x=212, y=152)

Cuadro_IMC = StringVar()  # Variable de control para el IMC
IMC = Label(Cuadro, text="Su IMC es de:", background='#f6f7f9', font=("Arial", 11))
IMC.place(x=20, y=250)
Entrada_IMC = Entry(Cuadro, textvariable=Cuadro_IMC, state='readonly')
Entrada_IMC.place(x=120, y=252)

Cuadro_GT = StringVar()
GT = Label(Cuadro, text="Su grasa total en kilos es:", background='#f6f7f9', font=("Arial", 11))
GT.place(x=270, y=250)
Entrada_GT = Entry(Cuadro, textvariable=Cuadro_GT, state='readonly')
Entrada_GT.place(x=445, y=252)

Cuadro_ML = StringVar()
ML = Label(Cuadro, text="Su masa libre de grasa en kilo es:", background='#f6f7f9', font=("Arial", 11))
ML.place(x=20, y=300)
Entrada_ML = Entry(Cuadro, textvariable=Cuadro_ML, state='readonly')
Entrada_ML.place(x=250, y=302)

Cuadro_FFMI = StringVar()
FFMI = Label(Cuadro, text="Su  FFMI es de:", background='#f6f7f9', font=("Arial", 11))
FFMI.place(x=20, y=350)
Entrada_FFMI = Entry(Cuadro, textvariable=Cuadro_FFMI, state='readonly')
Entrada_FFMI.place(x=130, y=352)

Cuadro_AFFMI = StringVar()
AFFMI = Label(Cuadro, text="Su  AFFMI aproximadamente es de:", background='#f6f7f9', font=("Arial", 11))
AFFMI.place(x=20, y=400)
Entrada_AFFMI = Entry(Cuadro, textvariable=Cuadro_AFFMI, state='readonly')
Entrada_AFFMI.place(x=260, y=402)

def calcular():
    try:
        kilos = float(Cuadro_kilos.get())
        estatura = float(Cuadro_estatura.get())
        grasa = float(Cuadro_Grasa.get())
        gt = kilos * (grasa/100)
        imc = kilos / (estatura ** 2)
        ml = kilos * (1 - grasa / 100)
        ffmi = ml / (estatura ** 2)
        affmi = ffmi + (6.3 * (1.8 - estatura))
        Cuadro_GT.set(f"{gt:.2f}")
        Cuadro_IMC.set(f"{imc:.2f}")
        Cuadro_ML.set(f"{ml:.2f}")
        Cuadro_FFMI.set(f"{ffmi:.2f}")
        Cuadro_AFFMI.set(f"{affmi:.2f}")
    except ValueError:
        Cuadro_IMC.set("Error")
        Cuadro_IMC.set("Error")
        Cuadro_ML.set("Error")
        Cuadro_FFMI.set("Error")
        Cuadro_AFFMI.set("Error")

Calcular = Button(Cuadro, text="Calcular", command=calcular)
Calcular.place(x=440, y=112)

def limpiar_campos():
    Cuadro_estatura.delete(0, END)
    Cuadro_kilos.delete(0, END)
    Cuadro_Grasa.delete(0, END)
    Cuadro_IMC.set("")
    Cuadro_GT.set("")
    Cuadro_ML.set("")
    Cuadro_FFMI.set("")
    Cuadro_AFFMI.set("")

Limpiar = Button(Cuadro, text="Limpiar", command=limpiar_campos)
Limpiar.place(x=540, y=112)

Pantalla.mainloop()