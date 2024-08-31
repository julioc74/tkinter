# programa que dado una cantidad nos pide elegir convertir de cm a pulg o pulg a cm y de acuerdo a lo que elijamos nos devuelve la conversion

import tkinter as tk

root = tk.Tk()
root.geometry("300x300")
var = tk.StringVar(value= " ")

def funcion():
    if var.get() == "cm a pulg":
        cantidad_cm = float(entrada.get())
        cantidad_pulg = float(cantidad_cm / 2.54)
        solucion.config(text= f"{cantidad_cm}  cm son  {cantidad_pulg:.2f} pulg ")
    
    elif var.get() == "pulg a cm":
        cantidad_pulg = float(entrada.get())
        cantidad_cm = float(cantidad_pulg * 2.54)
        solucion.config(text= f"{cantidad_pulg} pulg son  {cantidad_cm:.2f} cm")
    
    
    

etiqueta = tk.Label(root,
                     text= "Ingrese la cantidad ")

etiqueta.pack()    

entrada = tk.Entry(root,
                    font= "Times")

entrada.pack()

radioboton1 = tk.Radiobutton(root,
                             text= "cm a pulg",
                             value= "cm a pulg",
                             variable= var,
                             command= funcion)  

radioboton1.pack()

    

radioboton2 = tk.Radiobutton(root,
                             text= "pulg a cm",
                             value= "pulg a cm",
                             variable= var,
                             command= funcion)

radioboton2.pack()





solucion = tk.Label(root,
                   font= "Times" )

solucion.pack()






root.mainloop()

