def insertElementInAListbox(listbox, posicion, listaElementos):

    for element in listaElementos:

        id, firstname, lastname = element
        listbox.insert(posicion, "ID: " + str(id) + "       firstname: " + firstname + "        lastname: " + lastname)