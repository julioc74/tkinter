# importamos la libreria tkinter
import tkinter as tk

# Creacion de la ventana o contenedor principal
root = tk.Tk()
root.title("Primera aplicacion")

# Creacion de elementos(widgets) en este caso una etiqueta o label
etiqueta = tk.Label(root, 
                    text="Titulo",
                    font="Arial")

# el metodo pack() se usa para organizar elementos de manera secuencial ya sea horizontal o verticalmente
etiqueta.pack()

# ejecuta toda la aplicacion
root.mainloop()