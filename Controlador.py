import Queries as Q

def insertElementInAListbox(listbox, posicion, listaElementos):

    for element in listaElementos:

        id, firstname, lastname = element
        listbox.insert(posicion, "ID: " + str(id) + "       firstname: " + firstname + "        lastname: " + lastname)

def mostrarSeleccionado(listbox1, listbox2, listbox3, posicion2, posicion3):
    tupla = listbox1.curselection()

    if len(tupla) != 0 :
    
        persona = str(listbox1.get(tupla))
        value = persona.split(" ")[1]

        listbox2.delete(0, listbox2.size())
        listbox3.delete(0, listbox3.size())

        listaElementos = Q.getAmigos(value)

        if listaElementos != None:
            for element in listaElementos:
                id, firstname, lastname = element
                listbox2.insert(posicion2, "ID: " + str(id) + "       firstname: " + firstname + "        lastname: " + lastname)
    

        listaElementos = Q.getDisponibles(value)

        if listaElementos != None:
            for element in listaElementos:

                id, firstname, lastname = element
                listbox3.insert(posicion3, "ID: " + str(id) + "       firstname: " + firstname + "        lastname: " + lastname)



def pasarDisponibleAmigo(listbox1, listbox2, listbox3, posicion):
    tupla1 = listbox1.curselection()
    tupla3 = listbox3.curselection()
    
    if len(tupla1) != 0 and len(tupla3) != 0 :

        persona1 = str(listbox1.get(tupla1))
        value1 = persona1.split(" ")[1]

        persona2 = str(listbox3.get(tupla3))
        value2 = persona2.split(" ")[1]

        listbox2.delete(0, listbox2.size())
        listbox3.delete(0, listbox3.size())

        Q.agregarAmigo(value1, value2)

        mostrarAmigos(listbox2, posicion, Q.getAmigos(value1))
        mostrarDisponibles(listbox3, posicion, Q.getDisponibles(value1))

def pasarAmigoDisponible(listbox1, listbox2, listbox3, posicion):
    tupla1 = listbox1.curselection()
    tupla2 = listbox2.curselection()
    
    if len(tupla1) != 0 and len(tupla2) != 0 :

        persona1 = str(listbox1.get(tupla1))
        value1 = persona1.split(" ")[1]

        persona2 = str(listbox2.get(tupla2))
        value2 = persona2.split(" ")[1]

        listbox2.delete(0, listbox2.size())
        listbox3.delete(0, listbox3.size())

        Q.eliminarAmigo(value1, value2)

        mostrarAmigos(listbox2, posicion, Q.getAmigos(value1))
        mostrarDisponibles(listbox3, posicion, Q.getDisponibles(value1))


def mostrarAmigos(listbox, posicion, listaElementos):
    if listaElementos is not None :    
        for element in listaElementos:

            id, firstname, lastname = element
            listbox.insert(posicion, "ID: " + str(id) + "       firstname: " + firstname + "        lastname: " + lastname)

def mostrarDisponibles(listbox, posicion, listaElementos):
    if listaElementos is not None :
        for element in listaElementos:
            id, firstname, lastname = element
            listbox.insert(posicion, "ID: " + str(id) + "       firstname: " + firstname + "        lastname: " + lastname)



    

