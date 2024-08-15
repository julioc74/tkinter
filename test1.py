import tkinter as tk 

root = tk.Tk()
root.title("Responder correctamente")
root.geometry("500x500")
var = tk.StringVar(value= " ") # Se deja un espacio entre las comillas para que no este seleccionado por defecto ningun boton

def verificar_respuesta():
    if var.get() != "Roma":
        salida.config(text= "Su respuesta es incorrecta")
    else: 
        salida.config(text= "Respuesta correcta!")



pregunta1 = tk.Label(root,
                     text= "Cual es la capital de Italia?",
                     font= ("Times", 20))

pregunta1.pack()

respuesta1 = ["Paris", "Milan", "Londres", "Roma", "Madrid"] 

for opcion in respuesta1:
    radiobutton = tk.Radiobutton(root,
                            font= ("Times", 20),
                            text= opcion,
                            value= opcion,
                            variable= var,
                            command= verificar_respuesta)
    
    

    radiobutton.pack()
    

     
salida = tk.Label(root,
                  font= ("Times", 25),
                  text= "")

salida.pack()

root.mainloop()

