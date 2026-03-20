import tkinter as tk
from tkinter import messagebox

sabores = ["Chocolate", "Vainilla", "Frutilla", "Dulce de leche", "Limón", "Pistacho", "Granizado", "Mascarpone con frutos del bosque", "Banana Split"]
sabores_elegidos = []

def calcular_precio(opcion):
    if opcion == 1: return 700
    if opcion == 2: return 1200
    if opcion == 3: return 1600
    if opcion == "1/4 kg": return 2000
    if opcion == "1/2 kg": return 2700
    if opcion == "1 kg": return 3100
    if opcion == "Pizza": return 1500

def ver_sabores():
    lista = ""
    for i in range(len(sabores)):
        lista += sabores[i] + "\n"
    messagebox.showinfo("Sabores disponibles", lista)

def abrir_pedido():
    ventana_pedido = tk.Toplevel()
    ventana_pedido.title("Hacer Pedido")
    ventana_pedido.geometry("720x700")
    ventana_pedido.configure(bg="lightyellow")
    
    sabores_elegidos.clear()

    tk.Label(ventana_pedido, text="¿Qué vas a llevar?", bg="lightyellow").pack(pady=5)

    opcion_var = tk.StringVar()
    tk.Radiobutton(ventana_pedido, text="1 Bocha ($700)",bg="lightyellow", variable=opcion_var, value="1").pack()
    tk.Radiobutton(ventana_pedido, text="2 Bochas ($1200)",bg="lightyellow", variable=opcion_var, value="2").pack()
    tk.Radiobutton(ventana_pedido, text="3 Bochas ($1600)",bg="lightyellow", variable=opcion_var, value="3").pack()
    tk.Radiobutton(ventana_pedido, text="1/4 kg (2 sabores) - $2000",bg="lightyellow", variable=opcion_var, value="1/4 kg").pack()
    tk.Radiobutton(ventana_pedido, text="1/2 kg (3 sabores) - $2700",bg="lightyellow", variable=opcion_var, value="1/2 kg").pack()
    tk.Radiobutton(ventana_pedido, text="1 kg (4 sabores) - $3100",bg="lightyellow", variable=opcion_var, value="1 kg").pack()
    tk.Radiobutton(ventana_pedido, text="Pizza Congelada - $1500",bg="lightyellow", variable=opcion_var, value="Pizza").pack()

    tk.Label(ventana_pedido, text="Elegí un sabor y tocá 'Agregar'", bg="lightyellow").pack(pady=10)

    lista_sabores = tk.Listbox(ventana_pedido, selectmode="single")
    for i in range(len(sabores)):
        lista_sabores.insert(tk.END, sabores[i])
    lista_sabores.pack()

    label_seleccionados = tk.Label(ventana_pedido, text="Elegidos: ", bg="lightyellow", fg="blue")
    label_seleccionados.pack()

    def agregar_al_pedido():
        seleccion = lista_sabores.curselection()
        if seleccion:
            indice = seleccion[0]
            gusto = sabores[indice]
            sabores_elegidos.append(gusto)
            
            texto = "Elegidos: "
            for i in range(len(sabores_elegidos)):
                texto += sabores_elegidos[i] + ", "
            label_seleccionados.config(text=texto)

    tk.Button(ventana_pedido, text="Agregar Sabor", command=agregar_al_pedido).pack(pady=5)

    def confirmar_pedido():
        opcion = opcion_var.get()
        if opcion == "":
            messagebox.showwarning("Error", "Elegí qué vas a comprar")
            return

        cant_sabores = 0
        if opcion == "1": cant_sabores = 1
        elif opcion == "2": cant_sabores = 2
        elif opcion == "3": cant_sabores = 3
        elif opcion == "1/4 kg": cant_sabores = 2
        elif opcion == "1/2 kg": cant_sabores = 3
        elif opcion == "1 kg": cant_sabores = 4
        elif opcion == "Pizza": cant_sabores = 0

        if len(sabores_elegidos) != cant_sabores:
            messagebox.showwarning("Error", f"Tenés que elegir {cant_sabores} sabores")
            return

        if opcion in ["1", "2", "3"]:
            precio = calcular_precio(int(opcion))
        else:
            precio = calcular_precio(opcion)

        resumen = f"Pedido: {opcion}\nSabores:\n"
        for i in range(len(sabores_elegidos)):
            resumen += f"- {sabores_elegidos[i]}\n"
        resumen += f"\nTotal: ${precio}"
        
        messagebox.showinfo("Resumen del pedido", resumen)

    tk.Button(ventana_pedido, text="Confirmar Pedido", command=confirmar_pedido).pack(pady=20)

ventana = tk.Tk()
ventana.title("Heladería Dulce Frío")
ventana.geometry("1920x1080")
ventana.configure(bg="#a5f3ff")

tk.Label(ventana, text="𝐻𝑒𝓁𝒶𝒹𝑒𝓇𝒾𝒶 𝒟𝓊𝓁𝒸𝑒 𝐹𝓇𝒾𝑜 🍦", bg="#a5f3ff", fg="#e0b06d", font=("Arial", 40)).pack(pady=20)
tk.Button(ventana, text="Ver Sabores", command=ver_sabores).pack(pady=10)
tk.Button(ventana, text="Hacer Pedido", command=abrir_pedido).pack(pady=10)
tk.Button(ventana, text="Salir", command=ventana.destroy).pack(pady=10)

ventana.mainloop()