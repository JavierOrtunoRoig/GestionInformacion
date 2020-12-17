<center><h2> GESTIÓN DE LA INFORMACIÓN </h2></center>

<br>
<br>

#### Descripción de la tecnología

<p style="text-indent: 30px"> Para desarrollar este trabajo de conexión a una base de datos hemos optado por usar ‘Python’ y ‘MySQL’, porque a parte de ser una tecnología acorde con lo que ya hemos estudiado, resulta una muy buena opción gracias a las facilidades que nos aportan para llevar a cabo la tarea. A continuación explicamos cómo funciona dicha tecnología: </p>

<p style="text-indent: 30px"> Para comenzar, ¿cómo se conecta desde ‘Python’ con nuestra base de datos? Para ello, debemos descargar el paquete “mysql-connector-python” y, una vez hecho esto ya simplemente debemos importar mysql.connector y desde este junto con los datos necesarios (host, user, passwd, database..) ya podemos acceder a la base de datos.</p>

```python
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="****",  ## Cambiar contraseña según BD personal
    database="rastreocovid19"
)
```


<p style="text-indent: 30px"> Una vez hecha la conexión, las consultas a la base de datos se realizan por medio de “Queries”. Por cada método que implementemos debemos declarar un cursor, que esté va a ser el que nos permita hacer las consultas a nuestra base de datos obteniendo de esta manera los resultados o modificarla según se requiera. </p>

```python
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
```


#### Ventajas e inconvenientes de la tecnología

<p style="text-indent: 30px"> Con respecto a las partes buenas de la tecnología o ventajas respecto a otras podemos encontrar: </p>

<ul>
  <li> <p style="text-indent: 30px; margin-bottom: 20px"> La comodidad y facilidad para el acceso a una base de datos en MySQL, ya que simplemente tenemos que añadir en el código de la aplicación únicamente los datos correspondientes a la base de datos a la que vayamos a conectarnos. </p> </li>

  <li> <p style="text-indent: 30px; margin-bottom: 50px"> En nuestro caso, también nos ha supuesto una ventaja la similitud que tiene con la tecnología JDBC, tecnología que hemos estudiado anteriormente en clase,  siendo los métodos de conexión a la base de datos bastante similar, pero usando el lenguaje de programación ‘Python’ en vez de ‘Java’. </p></li>
</ul>



<p style="text-indent: 30px"> Respecto a los inconvenientes de la aplicación o aspectos negativos tenemos:</p>

<ul>
  <li> <p style="text-indent: 30px; margin-bottom: 20px"> Uno de los principales y mayores inconvenientes de la tecnología, es que dentro del código de la aplicación, en la parte de conexión a la base de datos, para la correcta conexión debe aparecer la contraseña del usuario que quiera acceder, poniendo en peligro la integridad y privacidad de los datos de los usuarios. </p> </li>

  <li> <p style="text-indent: 30px; margin-bottom: 20px"> Para el uso de esta tecnología también es necesario instalar previamente el paquete ‘mysql-connector-python’, como hemos dicho con anterioridad, el cual tendremos que importar en la aplicación para tener acceso a las clases dentro de Python que te permiten la conexión con la base de datos. Al igual, también hemos tenido que instalar MySQL para la creación y la modificación de la base de datos; cuya instalación podría llegar a ser algo laboriosa. </p></li>

  <li> <p style="text-indent: 30px; margin-bottom: 20px"> En nuestro caso, el trabajar con Python, al ser un lenguaje de programación que no hemos visto en clase, resulta nuevo para la mayoría de nosotros, y aunque no es muy diferente a los lenguajes orientados a objetos que hemos visto, ha sido necesario algo de investigación y documentación sobre este lenguaje. </p></li>
</ul>
