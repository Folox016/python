
import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Cult of the Lamb")
ventana.geometry("1000x650")
ventana.resizable(False, False)
ventana.configure(bg="#171014")

canvas = tk.Canvas(
    ventana,
    width=1024,
    height=1024,
    bg="#171014",
    highlightthickness=0
)
canvas.pack()

#FONDO

canvas.create_rectangle(
    0, 0, 1024, 1024,
    fill="#171014",
    outline=""
)

#TITULO

canvas.create_text(
    500, 120,
    text="CULT OF THE LAMB",
    fill="#eee4d5",
    font=("Arial", 38, "bold")
)

#USUARIO

canvas.create_text(
    500, 240,
    text="USUARIO",
    fill="#eee4d5",
    font=("Arial", 15, "bold")
)

usuario = tk.Entry(
    ventana,
    font=("Arial", 14),
    bg="#302129",
    fg="#eee4d5",
    insertbackground="white",
    relief="flat",
    justify="center"
)

canvas.create_window(
    500, 280,
    window=usuario,
    width=300,
    height=40
)

#CONTRASEÑA

canvas.create_text(
    500, 355,
    text="CONTRASEÑA",
    fill="#eee4d5",
    font=("Arial", 15, "bold")
)

contrasena = tk.Entry(
    ventana,
    font=("Arial", 14),
    bg="#302129",
    fg="#eee4d5",
    justify="center",
    show="*"
)

canvas.create_window(
    500, 395,
    window=contrasena,
    width=300,
    height=40
)

#INICIAR SESION

def iniciar_sesion():
    nombre = usuario.get()
    clave = contrasena.get()

    if nombre == "" or clave == "":
        messagebox.showwarning(
            "Aviso",
            "Introduce tu usuario y contraseña."
        )
    else:
        messagebox.showinfo(
            "Bienvenido",
            "¡Bienvenido a Cult of the Lamb!"
        )

boton = tk.Button(
    ventana,
    text="INICIAR SESIÓN",
    command=iniciar_sesion,
    font=("Arial", 15, "bold"),
    bg="#8f202b",
    fg="#f4e8d8",
    activebackground="#c13c45",
    activeforeground="white",
    relief="flat",
    width=18,
    cursor="hand2",
    bd=0
)

canvas.create_window(
    500, 480,
    window=boton,
    width=240,
    height=45
)

ventana.mainloop()