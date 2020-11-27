import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Patata",  ## Cambiar contraseña según BD personal
    database="rastreocovid19"
)


def getPersonas():
    listaPersonas = []

    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM people")

    result = cursor.fetchall()

    for x in result:
        listaPersonas.append(x)

    return listaPersonas


def getAmigos(id):
    listaAmigos = []

    tieneAmigos = False

    cursor = mydb.cursor()

    cursor.execute("SELECT ID2 FROM friends where ID1 = " + str(id))

    result = cursor.fetchall()

    selectStrFromPeople = "SELECT * FROM people where ID IN ( "

    for x in result:
        selectStrFromPeople = selectStrFromPeople + str(x[0]) + ","
        tieneAmigos = True

    selectStrFromPeople = selectStrFromPeople[0:len(selectStrFromPeople) - 1] + ")"

    if tieneAmigos:
        cursor.execute(selectStrFromPeople)

        result = cursor.fetchall()

        for x in result:
            listaAmigos.append(x)

    return listaAmigos


def getDisponibles(id):
  listaDisponibles = []

  cursor = mydb.cursor()

  cursor.execute("SELECT ID2 FROM friends where ID1 = " + str(id))

  result = cursor.fetchall()

  selectStrFromPeople = "SELECT * FROM people where ID NOT IN (" + str(id) + ","

  for x in result:
    selectStrFromPeople = selectStrFromPeople + str(x[0]) + ","

  selectStrFromPeople = selectStrFromPeople[0:len(selectStrFromPeople) - 1] + ")"

  cursor.execute(selectStrFromPeople)

  result = cursor.fetchall()

  for x in result:
    listaDisponibles.append(x)

  return listaDisponibles


def agregarAmigo(id1, id2):

    cursor = mydb.cursor()

    cursor.execute("SELECT id FROM people WHERE id = " + id1)

    value1 = cursor.next

    cursor.execute("SELECT id FROM people WHERE id = " + id2)

    value2 = cursor.fetchall()

    if value1 != value2:
        cursor.execute("INSERT INTO friends VALUES(ID1 = " + str(value1) + ", ID2 = " + str(value2) + ");")


def eliminarAmigo(id1, id2):
    cursor = mydb.cursor()

    cursor.execute("DELETE * FROM friends WHERE ID1 = " + str(id1) + " AND ID2 = " + str(id2))



