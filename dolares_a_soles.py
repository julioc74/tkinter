import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.resizable(width= "False", height= "False")
root.title("CONVERTIDOR DE DOLARES A SOLES")

etiqueta_dolares = tk.Label(root,
                            font= ("Arial", 20),
                            text= "Ingrese cantidad en dolares",
                            bg= "blue",
                            fg= "yellow")
etiqueta_dolares.pack()

entrada_dolares = tk.Entry(root, 
        font= ("Arial", 20) )
entrada_dolares.pack()

root.mainloop()