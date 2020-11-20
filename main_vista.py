from tkinter import *
from tkinter.font import BOLD
import Queries as Q


def insertElementInAListbox(listbox, posicion, listaElementos):

    for element in listaElementos:

        id, firstname, lastname = element
        listbox.insert(posicion, "ID: " + str(id) + "       firstname: " + firstname + "        lastname: " + lastname)

def main():
    root = Tk()
    root.title("Trabajo")
    root.geometry("1920x1080")

    espacio1Label = Label(text="                                                                                                  ")
    espacio2Label = Label(text="                                                                                                  ")

    personaLabel = Label(text="Personas")
    personaLabel.config(font=("Times New Roman", 24, BOLD))
    amigosLabel = Label(text="Amigos")
    amigosLabel.config(font=("Times New Roman", 24, BOLD))
    disponiblesLabel = Label(text="Disponibles")
    disponiblesLabel.config(font=("Times New Roman", 24, BOLD))


    personTam = 0
    amigosTam = 0
    disponiblesTam = 0

    person_listbox = Listbox(root, width=60, height=10)
    amigos_listbox = Listbox(root, width=60, height=10)
    disponibles_listbox = Listbox(root, width=60, height=10)


    personaLabel.grid(row=0, column=0)
    amigosLabel.grid(row=0, column=2)
    disponiblesLabel.grid(row=0, column=4)

    person_listbox.grid(row = 1, column=0)
    espacio1Label.grid(row = 1, column=1)
    amigos_listbox.grid(row = 1, column=2)
    espacio2Label.grid(row = 1, column=3)
    disponibles_listbox.grid(row = 1, column=4)

    listaPersonas = Q.getPersonas()
    insertElementInAListbox(person_listbox, personTam, listaPersonas)    

    root.mainloop()

if __name__ == "__main__":
    
    main()