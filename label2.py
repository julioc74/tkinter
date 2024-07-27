import tkinter as tk

root = tk.Tk()
root.title("Aplicacion")

etiqueta = tk.Label(root,
                   text = "Titulo",
                   font= "Times",
                   bg = "lightblue",
                   height = 5,
                   width = 40)

etiqueta.pack()

root.mainloop()