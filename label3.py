import tkinter as tk

root = tk.Tk()
root.title("Aplicacion")
root.geometry("600x600")
root.minsize(width=300, height=300)

etiqueta = tk.Label(root,
                    text= "Etiqueta",
                    font= ("Verdana", 14),
                    bg= "lightblue",
                    fg= "red",
                    padx= 15,
                    pady= 15,
                    relief="raised")


etiqueta.pack()

root.mainloop()