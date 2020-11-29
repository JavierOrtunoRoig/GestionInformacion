from tkinter import *
from tkinter.font import BOLD
import Queries as Q
import Controlador as C

def crearYColocarcomponentes():
    espacio1Label = Label(text="                                                                                                  ")
    espacio2Label = Label(text="                                                                                                  ")

    personaLabel = Label(text="Personas")
    personaLabel.config(font=("Times New Roman", 24, BOLD))
    amigosLabel = Label(text="Amigos")
    amigosLabel.config(font=("Times New Roman", 24, BOLD))
    disponiblesLabel = Label(text="Disponibles")
    disponiblesLabel.config(font=("Times New Roman", 24, BOLD))

    personaLabel.grid(row=0, column=0)
    amigosLabel.grid(row=0, column=2)
    disponiblesLabel.grid(row=0, column=4)
    espacio1Label.grid(row = 1, column=1)
    espacio2Label.grid(row = 1, column=3)






def main():
    root = Tk()
    root.title("Trabajo")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(f'{width}x{height}')
    fondoImagen = PhotoImage(file = "rastreo covid2.png")
    fondo = Label(root, image = fondoImagen).place(x = 0, y = 0)

    crearYColocarcomponentes()

    personTam = 0
    amigosTam = 0
    disponiblesTam = 0

    person_listbox = Listbox(root, width=60, height=10, exportselection = 0)
    amigos_listbox = Listbox(root, width=60, height=10, exportselection = 0)
    disponibles_listbox = Listbox(root, width=60, height=10, exportselection = 0)
    

    person_listbox.grid(row = 1, column=0, rowspan = 2)
    amigos_listbox.grid(row = 1, column=2, rowspan = 2)
    disponibles_listbox.grid(row = 1, column=4, rowspan = 2)

    listaPersonas = Q.getPersonas()
    C.insertElementInAListbox(person_listbox, personTam, listaPersonas)    

    imagenFlechaRosa = PhotoImage(file = "flechaDerechaRosa2.png")
    imagenFlechaAzul = PhotoImage(file = "flechaIzquierdaAzul2.png")
    

    buttonDer = Button(image = imagenFlechaRosa, command = lambda : C.pasarAmigoDisponible(person_listbox, amigos_listbox, disponibles_listbox, amigosTam))
    buttonDer.grid(row = 2, column = 3)
    buttonIzq = Button(image = imagenFlechaAzul, command = lambda : C.pasarDisponibleAmigo(person_listbox, amigos_listbox, disponibles_listbox, disponiblesTam))
    buttonIzq.grid(row = 1, column = 3)
    buttonIntr = Button(text = "Seleccionar", command = lambda : C.mostrarSeleccionado(person_listbox, amigos_listbox, disponibles_listbox, amigosTam, disponiblesTam))
    buttonIntr.grid(row = 3, column = 0)

    root.mainloop()


if __name__ == "__main__":
    
    main()