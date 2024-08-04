import tkinter as tk

root = tk.Tk()
root.title("Programa")
root.geometry("1000x1000")
root.resizable(height= "False", width= "False") # metodo que sirve para evitar cambiar el tamanio del contenedor.

etiqueta1 = tk.Label(root,
                     text= "Etiqueta 1",
                    font= ("Times", 20),
                    height= 2,
                    width= 20,
                    bg= "lightblue",
                    fg= "black",
                    padx= 20,
                    pady= 10,
                    relief= "sunken")

etiqueta2 = tk.Label(root,
                     text= "Etiqueta 2",
                     font= ("Times", 20),
                     height= 2,
                     width= 20,
                     bg= "red",
                     fg= "black",
                     padx= 20,
                     pady= 10,
                     relief= "sunken")

# metodo grid a diferencia del metodo pack es mas preciso al momento de controlar la ubicacion de widgets
# con sticky en "w" lo fijamos al lado izquierdo (west) y con "e" lo fijamos al lado derecho (east)
etiqueta1.grid(row= 0, column= 0, padx= 80, pady= 10, sticky= "w")
etiqueta2.grid(row= 0, column= 1, padx= 80, pady= 10, sticky= "e")

root.mainloop()