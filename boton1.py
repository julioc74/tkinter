import tkinter as tk

root = tk.Tk()
root.geometry("200x200")

# command= root.destroy especifica la funcion que se ejecutara cuando el boton sea presionado
# en este caso, 'root.destroy' cierra la ventana y termina la aplicacion cuando el boton es clicado.
boton = tk.Button(root,
                  text= "Click aqui",
                  command= root.destroy)

boton.pack(side= "top")

root.mainloop()