
import tkinter as tk

##claudia


# 1. Creamos la ventana principal
ventana_madre = tk.Tk()
ventana_madre.title("Aplicación Principal con Fondo")
ventana_madre.geometry("1024x1024")
ventana_madre.resizable(False, False)

# 2. Cargamos las imágenes
imagen_fondo = tk.PhotoImage(file="imatge1.png")
imagen_personaje = tk.PhotoImage(file="personaje.png")
imagen_personaje2 = tk.PhotoImage(file="personaje2.png")
imagen_personaje3 = tk.PhotoImage(file="personaje3.png")
imagen_personaje4 = tk.PhotoImage(file="personaje4.png")
imagen_personaje5 = tk.PhotoImage(file="personaje5.png")
imagen_personaje6 = tk.PhotoImage(file="personaje6.png")
imagen_personaje7 = tk.PhotoImage(file="personaje7.png")
imagen_personaje8 = tk.PhotoImage(file="personaje8.png")

# 3. Creamos el Canvas
canvas = tk.Canvas(
    ventana_madre,
    width=1024,
    height=1024
)
canvas.pack(fill="both", expand=True)

# 4. Añadimos la imagen de fondo
canvas.create_image(0, 0, image=imagen_fondo, anchor="nw")

# 5. Añadimos el personaje
personaje = canvas.create_image(
    600, 250,
    image=imagen_personaje
)

# 7. Variables de animación
animacion_activa = False

# 8. Función para mover y animar al personaje
def mover_izquierda(event):

    global animacion_activa

    # Movemos al personaje hacia la izquierda
    canvas.move(personaje, -10, 0)

    # Cambiamos la imagen para simular que camina
    canvas.itemconfig(personaje, image=imagen_personaje8)

    # Evitamos que se acumulen animaciones
    if not animacion_activa:
        animacion_activa = True
        ventana_madre.after(200, volver_izquierda)

def mover_derecha(event):

    global animacion_activa

    # Movemos al personaje hacia la izquierda
    canvas.move(personaje, 10, 0)

    # Cambiamos la imagen para simular que camina
    canvas.itemconfig(personaje, image=imagen_personaje6)

    # Evitamos que se acumulen animaciones
    if not animacion_activa:
        animacion_activa = True
        ventana_madre.after(200, volver_derecha)

def mover_arriba(event):

    global animacion_activa

    # Movemos al personaje hacia arriba
    canvas.move(personaje, 0, -10)

    # Cambiamos la imagen para simular que camina
    canvas.itemconfig(personaje, image=imagen_personaje4)

    if not animacion_activa:
        animacion_activa = True
        ventana_madre.after(200, volver_atras)


def mover_abajo(event):

    global animacion_activa

    # Movemos al personaje hacia abajo
    canvas.move(personaje, 0, 10)

    # Cambiamos la imagen para simular que camina
    canvas.itemconfig(personaje, image=imagen_personaje2)

    if not animacion_activa:
        animacion_activa = True
        ventana_madre.after(200, volver_normal)

# 9. Volvemos a la imagen original
def volver_normal():

    global animacion_activa

    canvas.itemconfig(personaje, image=imagen_personaje)
    animacion_activa = False

def volver_atras():

    global animacion_activa

    canvas.itemconfig(personaje, image=imagen_personaje3)
    animacion_activa = False

def volver_derecha():

    global animacion_activa

    canvas.itemconfig(personaje, image=imagen_personaje5)
    animacion_activa = False

def volver_izquierda():

    global animacion_activa

    canvas.itemconfig(personaje, image=imagen_personaje7)
    animacion_activa = False

# 10. Vinculamos la tecla espacio
ventana_madre.bind("<a>", mover_izquierda)
ventana_madre.bind("<d>", mover_derecha)
ventana_madre.bind("<w>", mover_arriba)
ventana_madre.bind("<s>", mover_abajo)

# 11. Bucle principal
ventana_madre.mainloop()