import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
root.resizable(height= "False", width= "False")

def sumar():
    primer_numero = int(primer_numero_entrada.get())
    segundo_numero = int(segundo_numero_entrada.get())
    suma = primer_numero + segundo_numero
    
    resultado.config(text= f'La suma es : {suma}')


# Cambiando la fuente y el tamanio 
primer_numero_entrada = tk.Entry(root, 
                                 font= ("Times", 20))
primer_numero_entrada.pack()


# Cambiando la fuente y el tamanio
segundo_numero_entrada = tk.Entry(root, 
                                  font= ("Times", 20))
segundo_numero_entrada.pack()

boton = tk.Button(root,
                  text= "Sumar",
                  command= sumar)
boton.pack() 

resultado = tk.Label(root,
                     text= "")
resultado.pack()


    
root.mainloop()    
