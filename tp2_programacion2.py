
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
    • Cada registro de venta debe contener:
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



""" 2) Realizar un algoritmo que permita saber si una palabra que pertenece a un 
oración ingresada es un palíndromo o no, en caso afirmativo debe contar la 
cantidad de palíndromos encontrados en dicha oración. El algoritmo termina 
una vez que la cadena ingresada es un #. Al finalizar, debe informar la 
cantidad de palabras palíndromos que encontró. 
Una vez que tiene el algoritmo, codificarlo en Python. 
3) 
Realizar un algoritmo que permite contar la cantidad de 
frecuencias/ocurrencias de una palabra. Se debe tener en cuenta que se debe 
contabilizar la cantidad de veces que aparece dicha palabra en una oración. 
Teniendo en cuenta que una oración inicia con una letra A-Z|a-z y termina con 
".". El algoritmo termina cuando la oración finaliza con '#'. Al finalizar, debe 
informar la cantidad de veces que aparece dicha palabra. 
Una vez que tiene el algoritmo, codificarlo en Python. 
4) Realizar un algoritmo que permite adivinar la palabra ingresada a partir de 
un conjunto de caracteres disponibles. Una vez que adivina la palabra 
ingresada debe salir del programa y avisar cuanto tardo en adivinarla.  
Por ejemplo: 
El usuario ingresa la palabra = claseDeUdemm 
El algoritmo debe estar procesando las combinaciones con los caracteres 
disponibles hasta poder adivinar la palabra ingresada. La restricción es que 
no es posible recorrer la palabra ingresada solo poder utilizar el operador de 
igualdad. 
nota: para poder tomar tiempo puede usar el módulo time.  
Una vez que tiene el algoritmo, codificarlo en Python. 
Explicar si es posible implementar dicha solución con las limitaciones del TP. y 
¿cuál cree que es el problema al cual se enfrenta? 
5) Realizar un algoritmo que permita saber de cuántas maneras diferentes se 
podría combinar una cantidad de lanas de un juego de ocho. Para poder 
realizar el algoritmo debe tener en cuenta el cálculo factorial del número de 
f
ichas del juego y debe ser realizado de forma iterativa sí o sí. 
Ejemplo, refresh numero factorial: 
Pensamos en una sola combinación donde tengo un cajón con 5 lanas: - Cuando tomamos la primera, nos quedan 4 para elegir - Cuando tomamos la segunda, nos quedan 3 para elegir - Cuando tomamos la tercera, nos quedan 2 para elegir - Cuando tomamos la cuarta, nos queda 1 para elegir 
Entonces, las combinaciones posibles: 5 x 4 x 3 x 2 x 4 1. => 5! = 120 
El factorial de cero es = 1 
Una vez que tiene el algoritmo, codificarlo en Python. 
6) En una empresa que se encuentra estudiando una mejor prestación de 
vuelo de drones, está trabajando en un estudio para determinar el 
posicionamiento óptimo de drones estático y dinámico en un área 
determinada, para minimizar el costo y maximizar la cobertura. Los drones 
tienen una altitud máxima y mínima de observación. Además, la altura es 
directamente proporcional al tamaño del área observada, a medida que 
aumenta la altura, también lo hace el área observada, así como la energía 
consumida. Nos piden elaborar un programa que permita cargar datos y 
evaluar las distancias, relacionada a la ubicación estática de los drones. 
Dron puede volar a una altura máxima de hmax y una altura mínima de hmin, 
también tiene un área de interés con longitud x y ancho y, que representa el 
área de interés. 
Entonces, para determinar la distancia entre dos puntos en el espacio nos 
ofrece la siguiente fórmula: 
Para un h = 0 sería: 
Nos piden que el programa en esta primera etapa permita, ingresar los 
valores de de x,y,z y permita calcular las distancia e informar el resultado. El 
programa termina cuando todos los valores son -1. 
Por lo tanto, necesitan poder calcular diferentes valores, para probar 
cualquier ubicación arbitraria en el área x e y. También tener en cuenta que 
pueden probar la localización de una posición (x, y, h) en la que un dron 
podría estar. 
Una vez que tiene el algoritmo, codificarlo en Python. 
7)  Realizar un algoritmo que permite generar anagramas. El usuario ingresa 
un conjunto de letras y con su longitud debería generar una cantidad finita de 
combinaciones compuesta por las letras que componen la palabra ingresada. 
Al finalizar, debe imprimir la cantidad de anagramas posible y el total 
generado. 
Nota: para poder realizarlo es necesario utilizar el concepto de factorial. 
Una vez que tiene el algoritmo, codificarlo en Python. 
Fuente:  https://es.wikipedia.org/wiki/Anagrama 
Explicar si es posible implementar dicha solución con las limitaciones del TP. y 
¿cuál cree que es el problema al cual se enfrenta? 
8)  
Eres responsable de digitalizar los registros manuales de un pequeño 
comercio. Debes crear un script en Python que permita al usuario ingresar los 
detalles de varios tickets de compra uno por uno. El sistema debe continuar 
solicitando datos hasta que el usuario ingrese la palabra clave terminado en 
lugar de un ID de ticket. 
Entrada de datos, solicitar repetidamente: 
●     ID del Ticket (debe ser único). 
●     Monto total de la compra (debe ser un número positivo). 
●     Categoría del producto (ej: "Alimentos", "Electrónica", "Ropa"). 
La condición de interrumpirse es cuando el usuario escriba terminado en el 
campo del ID.  
Validación Básica:  Si el monto es negativo o no numérico, mostrar un error y 
pedirlo nuevamente sin avanzar al siguiente ticket. 
Al finalizar, imprimir un resumen con:  El monto total acumulado de todas las 
compras. 
Una vez que tiene el algoritmo, codificarlo en Python. 
9)  
En una compañía que se dedica a la gestión de portfolios de inversiones están 
realizando una actualización de sus sistemas y necesita generar lotes de 
datos para realizar pruebas controladas de testing y pre-producción para 
validar la nueva versión de un sistema de reportes de baja latencia.  Por lo 
tanto es necesario poder generar un algoritmo que permita tomar los datos 
de los stock price y generar un reporte con el total del precio del stock, stock 
name, el date y el precio más alto y más bajo del día. Dicho reporte está 
ordenado por nombre de stock name y fecha. 
Un registro de stock contiene: - name. - default_prize. - default_high. - default_low. - date. - id. 
El orden de todos los registros es name y date. Por lo tanto, para una misma 
fecha pueden existir varios stock prize. Se pide: 
Generar un reporte que contenta: 
el nombre + la fecha + el máximo del stock prize del día + el mínimo del stock 
prize del día + el total price acumulado. 
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
Para poder elaborar el algoritmo, la empresa ya nos provee acceso a las API 
para obtener los registros.  Dicha API es posible utilizarla de la siguiente 
manera en Python: 
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
Se evaluará: - - - - - - - - - 
Inicialización de variables. 
Corte de control. 
Uso de máximos  y mínimos. 
Sentencias de control. 
Uso de bucle. Debe comentar cual es su elección y porque. 
Abstracción y estrategia del algoritmo. Capacidad de manejar la 
complejidad en la resolución del problema. 
Utilizar los recursos que se les da. 
Que cumpla con lo pedido del reporte. 
Todo debe ser resuelto en un solo recorrido. 
- - 
En el caso del reporte de se debe recorrer las estructuras una sola vez. 
Justificar sus elecciones. 
Una vez que tiene el algoritmo, codificarlo en Python. 
Nota a tener en cuenta: 
El uso de la IA es válido como asistente en el proceso de investigación; 
sin embargo, se espera que demuestren su propia comprensión 
mediante la revisión y el análisis profundo del contenido que ustedes 
vayan redactando y asimilando.  
Asimismo, es indispensable adaptar cualquier información a las normas 
APA vigentes, asegurando que las referencias sean verificables y estén 
correctamente formateadas. 
Se tendrá en cuenta también: 
●  Coherencia y estructura de lo que entregue. 
●  Originalidad de la redacción, """