import tkinter as tk;
from tkinter import messagebox;
from conversiones import*

def salir():
    cerrar = messagebox.askquestion("Salir", "¿Desea salir?");
    
    if cerrar == "yes":
        window.destroy()

def limpiar():
    txt_salida.delete(0, "end")

#temperaturas
def temp1():
    limpiar()
    try:
        txt_salida.insert(0, centigrados_fahrenheit(txt_entrada.get()))
    except:
        messagebox.showerror("Error", "Solo acepto numero")

def temp2():
    limpiar()
    try:
        txt_salida.insert(0, fahrenheit_centigrados(txt_entrada.get()))
    except:
        messagebox.showerror("Error", "Solo acepto numero")

def temp3():
    limpiar()
    try:
        txt_salida.insert(0, centigrados_kelvin(txt_entrada.get()))
    except:
        messagebox.showerror("Error", "Solo acepto numero")

def temp4():
    limpiar()
    txt_salida.insert(0, kelvin_centigrados(txt_entrada.get()))

#distancias
def dis1():
    limpiar()
    try:
        txt_salida.insert(0, metros_kilometros(txt_entrada.get()))
    except:
        messagebox.showerror("Error", "Solo acepto numero")

def dis2():
    limpiar()
    try:
        txt_salida.insert(0, pulgadas_centimetros(txt_entrada.get()))
    except:
        messagebox.showerror("Error", "Solo acepto numero")
    
def dis3():
    limpiar()
    try:
        txt_salida.insert(0, milimetros_pulgadas(txt_entrada.get()))
    except:
        messagebox.showerror("Error", "Solo acepto numero")

def dis5():
    limpiar()
    try:
        txt_salida.insert(0, kilometros_yardas(txt_entrada.get()))
    except:
        messagebox.showerror("Error", "Solo acepto numero")
    
def dis6():
    limpiar()
    try:
        txt_salida.insert(0, centimetros_pugadas(txt_entrada.get()))
    except:
        messagebox.showerror("Error", "Solo acepto numero")

def dis7():
    limpiar()
    try:
        txt_salida.insert(0, pulgadas_milimetros(txt_entrada.get()))
    except:
        messagebox.showerror("Error", "Solo acepto numero")

def dis8():
    limpiar()
    try:
        txt_salida.insert(0, yarda_kilometros(txt_entrada.get()))
    except:
        messagebox.showerror("Error", "Solo acepto numero")

#peso
def pes1():
    limpiar()
    try:
        txt_salida.insert(0, kilogramos_libras(txt_entrada.get()))
    except:
        messagebox.showerror("Error", "Solo acepto numero")

def pes2():
    limpiar()
    try:
        txt_salida.insert(0, kilogramos_piedras(txt_entrada.get()))
    except:
        messagebox.showerror("Error", "Solo acepto numero")

def pes3():
    limpiar()
    try:
        txt_salida.insert(0, onzas_gramos(txt_entrada.get()))
    except:
        messagebox.showerror("Error", "Solo acepto numero")

def pes4():
    limpiar()
    try:
        txt_salida.insert(0, onzas_libras(txt_entrada.get()))
    except:
        messagebox.showerror("Error", "Solo acepto numero")

def pes5():
    limpiar()
    try:
        txt_salida.insert(0, libras_kilogramos(txt_entrada.get()))
    except:
        messagebox.showerror("Error", "Solo acepto numero")

def pes6():
    limpiar()
    try:
        txt_salida.insert(0, piedras_kilogramos(txt_entrada.get()))
    except:
        messagebox.showerror("Error", "Solo acepto numero")

def pes7():
    limpiar()
    try:
        txt_salida.insert(0, gramos_onzas(txt_entrada.get()))
    except:
        messagebox.showerror("Error", "Solo acepto numero")

def pes8():
    limpiar()
    try:
        txt_salida.insert(0, libras_onzas(txt_entrada.get()))
    except:
        messagebox.showerror("Error", "Solo acepto numero")

#Ventana principal
window = tk.Tk()
window.title("Conversor Metrico")
window.config(width=350, height=250)
window.resizable(height=False, width=False)

#Menu
menu = tk.Menu(window)
menu_temperatura = tk.Menu(menu, tearoff=0)
menu_distancia = tk.Menu(menu, tearoff=0)
menu_peso = tk.Menu(menu, tearoff=0)
menu_salir = tk.Menu(menu, tearoff=0)

#menu temperaturas
menu_temperatura.add_cascade(label="Centigrador a Fahrenheit", command=temp1)
menu_temperatura.add_cascade(label="Centigrador a Kelvin", command=temp2)
menu_temperatura.add_cascade(label="Fahrenheit a centigrados", command=temp3)
menu_temperatura.add_cascade(label="Kelvin Centigrador", command=temp4)

#menu distancias
menu_distancia.add_cascade(label="Metros a kilometros", command=dis1)
menu_distancia.add_cascade(label="Pulgadas a centimetros", command=dis2)
menu_distancia.add_cascade(label="Milimetros a pulgadas", command=dis3)
menu_distancia.add_cascade(label="kilometro a yarda", command=dis5)
menu_distancia.add_cascade(label="Centimetros a pulgadas", command=dis6)
menu_distancia.add_cascade(label="Pulgadas a milimetros", command=dis7)
menu_distancia.add_cascade(label="Yarda a kilometro", command=dis8)

#menu peso
menu_peso.add_cascade(label="Kilogramos a libras", command=pes1)
menu_peso.add_cascade(label="Kilogramos a piedras", command=pes2)
menu_peso.add_cascade(label="Onzas a gramos", command=pes3)
menu_peso.add_cascade(label="Onzas a libras", command=pes4)
menu_peso.add_cascade(label="Libras a kilogramos", command=pes5)
menu_peso.add_cascade(label="Piedras a kilogramos", command=pes6)
menu_peso.add_cascade(label="Gramos a onzas", command=pes7)
menu_peso.add_cascade(label="Libras a onzas", command=pes8)

#menu salir
menu_salir.add_cascade(label="Salir", command=salir)

#menu agregado a la ventana
menu.add_cascade(label="Temperatura", menu=menu_temperatura)
menu.add_cascade(label="Distancia", menu=menu_distancia)
menu.add_cascade(label="Peso", menu=menu_peso)
menu.add_cascade(label="Salir", menu=menu_salir)

#Paneles de texto
txt_entrada = tk.Entry(window, width=50)
txt_entrada.grid(column=1, row=0, padx=10, pady=10)

txt_salida = tk.Entry(window, width=50)
txt_salida.grid(column=1, row=1, padx=10, pady=10)

#label
label_convertir = tk.Label(window, width=10, text="Convertir: ")
label_convertir.grid(column=0, row=0, padx=2, pady=2)

label_convertido = tk.Label(window, width=10, text="Convertido: ")
label_convertido.grid(column=0, row=1, padx=2, pady=2)


window.config(menu=menu)
window.mainloop()