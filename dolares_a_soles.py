import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.resizable(width= "False", height= "False")
root.title("CONVERTIDOR DE DOLARES A SOLES")

def convertir():
    
    cantidad_dolares = float(entrada_dolares.get())
    cambio = float(entrada_cambio.get())
    total_soles = cantidad_dolares * cambio 
    
    resultado.config(text= f'La cantidad en soles es {total_soles}')

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

boton = tk.Button(root,
                  text= "convertir",
                  font= ("Arial", 20),
                  command= convertir,
                  )

boton.pack()

resultado = tk.Label(root,
                     font= ("Arial", 20),
                     text= "")

resultado.pack()


root.mainloop()