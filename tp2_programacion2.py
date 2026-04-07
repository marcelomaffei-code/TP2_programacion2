
""" TP Práctico 
Para este TP, es necesario que utilicen solo: - - - - - - - - 
String. 
La función input. 
Estructuras iterativas, pueden ser for y while. 
Asignación de variables. 
Conditional statement y combinaciones. 
Pueden usar switch. 
lógica booleana. 
Y no es posible utilizar break o continue. Utilizar mejoras por medio de 
condicionales y cambio de variable. 

1) Realizar un algoritmo que permita registrar las ventas diarias de un comercio. El sistema debe procesar múltiples registros de ventas 
hasta que el usuario ingrese el código de venta FIN.
Cada registro de venta debe contener:
    • Código de producto (ej: "FQ-1200", "RQ-0001")
    • Cantidad vendida (número entero positivo)
    • Precio unitario (número decimal positivo)

Al finalizar el ingreso de datos (cuando se ingrese FIN), debe informar:
    • La cantidad total de productos vendidos.
    • El monto total recaudado.
    • El producto más vendido.
    • La cantidad de transacciones procesadas.
Una vez que tiene el algoritmo, codificarlo en Python. 
 """

totalProductosVendidos = 0
montoTotal = 0
transaccionesCont = 0
productoMasVendido = ""
maxCantidadVendida = 0

codigoDeProducto = input("Ingrese código de producto (o 'FIN' para terminar): ")

while codigoDeProducto != "FIN":
        
    cantidadVendida = int(input("Cantidad vendida: "))
    while cantidadVendida <= 0:
        cantidadVendida = int(input("Error. Ingrese cantidad positiva: "))

    precioUnitario = float(input("Precio unitario: "))
    while precioUnitario <= 0:
        precioUnitario = float(input("Error. Ingrese precio positivo: "))

    totalProductosVendidos += cantidadVendida
    montoTotal += cantidadVendida * precioUnitario
    transaccionesCont += 1

    if cantidadVendida > maxCantidadVendida:
        maxCantidadVendida = cantidadVendida
        productoMasVendido = codigoDeProducto

    codigoDeProducto = input("Ingrese código de producto (o 'FIN' para terminar): ")

print("Total productos:", totalProductosVendidos)
print("Total dinero:", montoTotal)
print("Transacciones:", transaccionesCont)
if transaccionesCont == 0:
    print("No se registraron ventas")
else:
    print("Producto más vendido:", productoMasVendido)

""" 
2) Realizar un algoritmo que permita saber si una palabra que pertenece a un oración ingresada es un palíndromo o no, 
en caso afirmativo debe contar la cantidad de palíndromos encontrados en dicha oración. El algoritmo termina 
una vez que la cadena ingresada es un #. Al finalizar, debe informar la cantidad de palabras palíndromos que encontró. 
Una vez que tiene el algoritmo, codificarlo en Python. 
"""

oracion = input("Ingrese una oracion o # para terminar: ")
cantidadPalindromos = 0

while oracion != "#":
    palabras = oracion.split()

    for palabra in palabras:
        palabra = palabra.lower().strip(".,;:!?")

        if palabra != "":
            i = 0
            j = len(palabra) - 1
            esPalindromo = True

            while i < j and esPalindromo:
                if palabra[i] != palabra[j]:
                    esPalindromo = False
                i += 1
                j -= 1

            if esPalindromo:
                print("Palabra palindromo:", palabra)
                cantidadPalindromos += 1

    oracion = input("Ingrese una oracion o # para terminar: ")
print("Cantidad total de palindromos:", cantidadPalindromos)

""" ------------------------------------------------------------------------
3) 
Realizar un algoritmo que permite contar la cantidad de frecuencias/ocurrencias de una palabra. Se debe tener en cuenta que se debe 
contabilizar la cantidad de veces que aparece dicha palabra en una oración. 
Teniendo en cuenta que una oración inicia con una letra A-Z|a-z y termina con ".". El algoritmo termina cuando la oración finaliza con '#'. 
Al finalizar, debe informar la cantidad de veces que aparece dicha palabra. Una vez que tiene el algoritmo, codificarlo en Python. 
"""

palabraBuscada = input("Ingrese la palabra a buscar: ").strip().lower()
    
while not palabraBuscada:
    palabraBuscada = input("Error. Ingrese una palabra válida: ").strip().lower()

total = 0
oracion = input("Ingrese una oración o '#' para terminar: ")

while oracion.strip() != "#":
    oracion = oracion.strip()

    if oracion and oracion[0].isalpha() and oracion.endswith("."):
        oracion_limpia = oracion.rstrip(".")
        palabras = oracion_limpia.split()

        for palabra in palabras:
            palabra = palabra.lower().strip(".,;:!?¡¿\"'")
            if palabra == palabraBuscada:
                    total += 1
    else:
        print("Error. La oración debe iniciar con una letra y terminar con un punto.")

    oracion = input("Ingrese una oración (o '#' para terminar): ")
print(f"\nLa palabra '{palabraBuscada}' aparece {total} veces en total.")

"""
4) Realizar un algoritmo que permite adivinar la palabra ingresada a partir de un conjunto de caracteres disponibles. Una vez que adivina la palabra 
ingresada debe salir del programa y avisar cuanto tardo en adivinarla.  

Por ejemplo: 

    El usuario ingresa la palabra = claseDeUdemm

    El algoritmo debe estar procesando las combinaciones con los caracteres disponibles hasta poder adivinar la palabra ingresada. La restricción es
    que no es posible recorrer la palabra ingresada solo poder utilizar el operador de igualdad.

    nota: para poder tomar tiempo puede usar el módulo time.

    Una vez que tiene el algoritmo, codificarlo en Python.

Explicar si es posible implementar dicha solución con las limitaciones del TP. y
¿cuál cree que es el problema al cual se enfrenta?
"""

import time    
palabraAdivinar = input("Ingrese la palabra a adivinar: ")
caracteres = "abcdefghijklmnopqrstuvwxyz"
intento = ""
encontrado = False
inicioTiempo = time.time()

indices = [0] * 20
longitudActual = 1

print("Procesando... por favor espere.")
while not encontrado:
    intento = ""
    for i in range(longitudActual):
        intento += caracteres[indices[i]]
    print(intento)

    if intento == palabraAdivinar:
        encontrado = True
    else:
        pos = 0
        incrementar = True
        while incrementar and pos < longitudActual:
            indices[pos] += 1
            if indices[pos] < len(caracteres):
                incrementar = False
            else:
                indices[pos] = 0
                pos += 1
            
        if incrementar:
            longitudActual += 1
            if longitudActual > len(palabraAdivinar):
                encontrado = True 

finTiempo = time.time()
tiempo_total = finTiempo - inicioTiempo

if intento == palabraAdivinar:
    print(f"¡Palabra adivinada!: {intento}")
    print(f"Tiempo tardado: {tiempo_total:.2f} segundos.")
else:
    print("No se pudo encontrar la palabra con los caracteres disponibles.")

"""
5) Realizar un algoritmo que permita saber de cuántas maneras diferentes se podría combinar una cantidad de lanas de un juego de ocho. 
Para poder realizar el algoritmo debe tener en cuenta el cálculo factorial del número de fichas del juego y debe ser realizado de forma iterativa sí o sí.
Ejemplo, refresh numero factorial:
Pensamos en una sola combinación donde tengo un cajón con 5 lanas: 
    - Cuando tomamos la primera, nos quedan 4 para elegir 
    - Cuando tomamos la segunda, nos quedan 3 para elegir 
    - Cuando tomamos la tercera, nos quedan 2 para elegir 
    - Cuando tomamos la cuarta, nos queda 1 para elegir

Entonces, las combinaciones posibles: 5 x 4 x 3 x 2 x 1. => 5! = 120
El factorial de cero es = 1
Una vez que tiene el algoritmo, codificarlo en Python.
"""

n = int(input("ingrese la cantidad de fichas: "))

while n < 0:
    n = int(input("Error!!! Ingrese un numero valido >= 0: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"El factorial de {n} es: {factorial}")
print(f"Cantidad de combinaciones posibles: {factorial}")

"""
6) En una empresa que se encuentra estudiando una mejor prestación de vuelo de drones, está trabajando en un estudio para determinar el posicionamiento óptimo de drones estático y dinámico en un área 
determinada, para minimizar el costo y maximizar la cobertura. Los drones tienen una altitud máxima y mínima de observación. Además, la altura es directamente proporcional al tamaño del área observada, a medida que aumenta la altura, también lo hace el área observada, así como la energía consumida. Nos piden elaborar un programa que permita cargar datos y evaluar las distancias, relacionada a la ubicación estática de los drones. 

Dron puede volar a una altura máxima de hmax y una altura mínima de hmin, también tiene un área de interés con longitud x y ancho y, que representa el área de interés. 

Entonces, para determinar la distancia entre dos puntos en el espacio nos ofrece la siguiente fórmula: 
Para un h = 0 sería: 

Nos piden que el programa en esta primera etapa permita, ingresar los valores de de x,y,z y permita calcular las distancia e informar el resultado. El programa termina cuando todos los valores son -1. 

Por lo tanto, necesitan poder calcular diferentes valores, para probar cualquier ubicación arbitraria en el área x e y. También tener en cuenta que 
pueden probar la localización de una posición (x, y, h) en la que un dron podría estar. 

Una vez que tiene el algoritmo, codificarlo en Python. 
"""

print("ingrese coordenadas de dos puntos en el espacio (x, y, z)")
print("para terminar, ingrese (-1) en x1, y1 y z1")

x1 = float(input("x1: "))
y1 = float(input("y1: "))
z1 = float(input("z1: "))

while not (x1 == -1 and y1 == -1 and z1 == -1):
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    z2 = float(input("z2: "))

    distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5

    print(f"La distancia entre los puntos es: {distancia:.2f}")

    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    z1 = float(input("z1: "))

"""
7)  Realizar un algoritmo que permite generar anagramas. El usuario ingresa un conjunto de letras y con su longitud debería generar una cantidad finita de combinaciones compuesta por las letras que componen la palabra ingresada.
Al finalizar, debe imprimir la cantidad de anagramas posible y el totalgenerado.

Nota: para poder realizarlo es necesario utilizar el concepto de factorial.

Una vez que tiene el algoritmo, codificarlo en Python.
Fuente:  https://es.wikipedia.org/wiki/Anagrama

Explicar si es posible implementar dicha solución con las limitaciones del TP. y 
¿cuál cree que es el problema al cual se enfrenta? 

"""

palabra = input("Ingrese una palabra: ").strip()

while palabra == "":
    palabra = input("Error. Ingrese una palabra válida: ").strip()

n = len(palabra)

# iterativo
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1

print("Cantidad máxima de combinaciones:", factorial)
#No es viable generar todos los anagramas con las restricciones del TP.
#El problema es de complejidad factorial (n!), crece muy rápido.

"""
8)  
Eres responsable de digitalizar los registros manuales de un pequeño comercio. Debes crear un script en Python que permita al usuario ingresar los detalles de varios tickets de compra uno por uno. El sistema debe continuar solicitando datos hasta que el usuario ingrese la palabra clave terminado en lugar de un ID de ticket.
Entrada de datos, solicitar repetidamente:
    ● ID del Ticket (debe ser único).
    ● Monto total de la compra (debe ser un número positivo).
    ● Categoría del producto (ej: "Alimentos", "Electrónica", "Ropa").
La condición de interrumpirse es cuando el usuario escriba terminado en el campo del ID.

Validación Básica:  Si el monto es negativo o no numérico, mostrar un error y pedirlo nuevamente sin avanzar al siguiente ticket.
Al finalizar, imprimir un resumen con:  El monto total acumulado de todas las compras.
Una vez que tiene el algoritmo, codificarlo en Python.
"""

total = 0
idTicket = input("Ingrese ID del ticket o 'terminado': ").strip()

while idTicket.lower() != "terminado":

    montoValido = False
    while not montoValido:
        montoTexto = input("Ingrese monto: ").strip()

        if montoTexto.replace(".", "", 1).isdigit():
            monto = float(montoTexto)
            if monto > 0:
                montoValido = True
            else:
                print("Monto debe ser positivo")
        else:
            print("Debe ingresar un número válido")

    categoria = input("Ingrese categoría: ")
    total += monto
    idTicket = input("Ingrese ID del ticket o 'terminado': ").strip()
print("Total acumulado:", total)

"""
9)  
En una compañía que se dedica a la gestión de portfolios de inversiones están realizando una actualización de sus sistemas y necesita generar lotes de datos para realizar pruebas controladas de testing y pre-producción para validar la nueva versión de un sistema de reportes de baja latencia.  
Por lo tanto es necesario poder generar un algoritmo que permita tomar los datos de los stock price y generar un reporte con el total del precio del stock, stock name, el date y el precio más alto y más bajo del día. Dicho reporte está ordenado por nombre de stock name y fecha. 

Un registro de stock contiene: 
    - name
    - default_prize
    - default_high
    - default_low
    - date
    - id

El orden de todos los registros es name y date. Por lo tanto, para una misma fecha pueden existir varios stock prize. 

Se pide:
Generar un reporte que contenta: 

el nombre + la fecha + el máximo del stock prize del día + el mínimo del stock prize del día + el total price acumulado.

Ejemplo de un listado:

FB, default_prize=75.00, default_high=75.03, default_low=74.90,2023-12-31
FB, default_prize=73.00, default_high=77.05, default_low=71.20,2023-12-30
FB, default_prize=68.00, default_high=71.15, default_low=69.00,2023-12-30
IBM, default_prize=55.00, default_high=60.10, default_low=50.00,2023-12-30

El reporte es:

FB del 2023-12-31 maximo: 75.03 y mínimo: 74.90 total: 75.00 
FB del 2023-12-30 máximo: 77.03 y mínimo: 69.00 total: 141.0 
IBM del 2023-12-30 máximo: 60.10 y mínimo: 50.00 total: 55.0 

Se debe recorrer el listado una sola vez para generar el reporte que nos solicitan.

Para poder elaborar el algoritmo, la empresa ya nos provee acceso a las API para obtener los registros.  Dicha API es posible utilizarla de la siguiente manera en Python:

from apivalo import get_registros, next_record 
get_registros() => retorna una colección de registros

next_record(collection) => recibe una colección de registros y retorna un registro. 
En el caso que la colección no tenga un próximo registro a recorrer retorna False. 

Datos del registro que retorna: 

record.name 
record.default_prize 
record.default_high 
record.default_low 
record.date 

Cada vez que se invoca a next_record, retorna el actual y se posiciona en el 
próximo. 

En este ejercicio: no es posible utilizar diccionarios u otras funciones o 
librerías 3 party para resolver el ejercicio. Solo debe ser resuelto utilizando las 
abstracciones y estrategias de control vistas. 

Se evaluará: 
- Inicialización de variables. 
- Corte de control. 
- Uso de máximos  y mínimos. 
- Sentencias de control. 
- Uso de bucle. Debe comentar cual es su elección y porque. 
- Abstracción y estrategia del algoritmo. Capacidad de manejar la complejidad en la resolución del problema. 
- Utilizar los recursos que se les da. 
- Que cumpla con lo pedido del reporte. 
- Todo debe ser resuelto en un solo recorrido. 
- En el caso del reporte de se debe recorrer las estructuras una sola vez. 
- Justificar sus elecciones.

Una vez que tiene el algoritmo, codificarlo en Python. 

Nota a tener en cuenta: 

El uso de la IA es válido como asistente en el proceso de investigación; sin embargo, se espera que demuestren su propia comprensión mediante la revisión y el análisis profundo del contenido que ustedes vayan redactando y asimilando.  

Asimismo, es indispensable adaptar cualquier información a las normas APA vigentes, asegurando que las referencias sean verificables y estén correctamente formateadas.

Se tendrá en cuenta también: 
●  Coherencia y estructura de lo que entregue. 
●  Originalidad de la redacción,  """

registros = Record.getRegistros()
record = Record.nextRecord(registros)

if record is None:
    print("No hay datos")
else:
    nombreActual = record.name
    fechaActual = record.date

    maximo = record.defaultHigh
    minimo = record.defaultLow
    total = record.defaultPrize
    record = Record.nextRecord(registros)

    while record is not None:

        if record.name == nombreActual and record.date == fechaActual:
            total += record.defaultPrize

            if record.defaultHigh > maximo:
                maximo = record.defaultHigh

            if record.defaultLow < minimo:
                minimo = record.defaultLow

        else:
            print(nombreActual, fechaActual, "max:", maximo, "min:", minimo, "total:", total)

            nombreActual = record.name
            fechaActual = record.date
            maximo = record.defaultHigh
            minimo = record.defaultLow
            total = record.defaultPrize

        record = Record.nextRecord(registros)

    print(nombreActual, fechaActual, "max:", maximo, "min:", minimo, "total:", total)