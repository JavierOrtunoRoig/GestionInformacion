import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Patata_325",  ## Cambiar contraseña según BD personal
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

    cursor = mydb.cursor()

    cursor.execute("SELECT ID2 FROM friends where ID1 = " + str(id))

    result = cursor.fetchall()

    selectStrFromPeople = "SELECT * FROM people where ID IN ("

    for x in result:
        selectStrFromPeople = selectStrFromPeople + str(x[0]) + ","

    selectStrFromPeople = selectStrFromPeople[0:len(selectStrFromPeople) - 1] + ")"

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

  selectStrFromPeople = "SELECT * FROM people where ID NOT IN (" + "'" + str(id) + "',"

  for x in result:
    selectStrFromPeople = selectStrFromPeople + str(x[0]) + ","

  selectStrFromPeople = selectStrFromPeople[0:len(selectStrFromPeople) - 1] + ")"

  cursor.execute(selectStrFromPeople)

  result = cursor.fetchall()

  for x in result:
    listaDisponibles.append(x)

  return listaDisponibles
