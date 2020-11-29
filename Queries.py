import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",  ## Cambiar contraseña según BD personal
    database="rastreocovid19"
)


def getPersonas():
    try:

        listaPersonas = []

        cursor = mydb.cursor()

        cursor.execute("SELECT * FROM people")

        result = cursor.fetchall()

        for x in result:
            listaPersonas.append(x)

    except:
        listaPersonas = []

    finally:

        return listaPersonas


def getAmigos(id):
    try:
        listaAmigos = []

        cursor = mydb.cursor()

        cursor.execute("SELECT ID2 FROM friends where ID1 = " + str(id))

        result = cursor.fetchall()

        selectStrFromPeople = "SELECT * FROM people where ID IN ( "

        for x in result:
            selectStrFromPeople = selectStrFromPeople + str(x[0]) + ","

        selectStrFromPeople = selectStrFromPeople[0:len(selectStrFromPeople) - 1] + ")"

        cursor.execute(selectStrFromPeople)

        result = cursor.fetchall()

        for x in result:
            listaAmigos.append(x)

    except:
        listaAmigos = []

    return listaAmigos


def getDisponibles(id):
    try:

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

    except:
        listaDisponibles = []

    return listaDisponibles


def agregarAmigo(id1, id2):

    cursor = mydb.cursor()

    if id1 != id2:
       cursor.execute("INSERT INTO `rastreocovid19`.`friends` (`ID1`, `ID2`) VALUES ('" + id1 + "', '" + id2 + "');")
       mydb.commit() 

       cursor.execute("INSERT INTO `rastreocovid19`.`friends` (`ID1`, `ID2`) VALUES ('" + id2 + "', '" + id1 + "');")
       mydb.commit() 


def eliminarAmigo(id1, id2):
    cursor = mydb.cursor()

    if id1 != id2:
        cursor.execute("DELETE FROM `rastreocovid19`.`friends` WHERE (`ID1` = '" + id1 + "') and (`ID2` = '" + id2 + "');")
        mydb.commit()

        cursor.execute("DELETE FROM `rastreocovid19`.`friends` WHERE (`ID1` = '" + id2 + "') and (`ID2` = '" + id1 + "');")
        mydb.commit()


