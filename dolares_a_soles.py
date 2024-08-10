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
                           font= ("Arial", 20))
entrada_dolares.pack()

etiqueta_cambio = tk.Label(root,
                          font= ("Arial", 20),
                          text= "Ingrese precio del dolar",
                          bg= "blue",
                          fg= "yellow")

etiqueta_cambio.pack()

entrada_cambio = tk.Entry(root,
                          font= ("Arial", 20))
entrada_cambio.pack()


root.mainloop()