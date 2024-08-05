import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
root.resizable(height= "False", width= "False")
root.title("Suma de dos numeros")

def sumar():
    primer_numero = int(primer_numero_entrada.get())
    segundo_numero = int(segundo_numero_entrada.get())
    suma = primer_numero + segundo_numero
    
    resultado.config(text= f'La suma es : {suma}')

# Colocando etiqueta de primer numero
primer_numero_etiqueta = tk.Label(root,
                                  font= ("Times", 20),
                                  text= "Ingrese primer numero")
primer_numero_etiqueta.pack()

# Cambiando la fuente y el tamanio 
primer_numero_entrada = tk.Entry(root, 
                                 font= ("Times", 20))
primer_numero_entrada.pack()

# Colocando etiqueta de segundo numero 
segundo_numero_etiqueta = tk.Label(root,
                                  font= ("Times", 20),
                                  text= "Ingrese segundo numero")
segundo_numero_etiqueta.pack()

# Cambiando la fuente y el tamanio
segundo_numero_entrada = tk.Entry(root, 
                                  font= ("Times", 20))
segundo_numero_entrada.pack()

# Cambiando la fuente y tamanio
boton = tk.Button(root,
                  text= "Sumar",
                  font= ("Times", 20),
                  command= sumar)
boton.pack() 

resultado = tk.Label(root,
                     font= ("Times", 20),
                     text= "")
resultado.pack()


    
root.mainloop()    
