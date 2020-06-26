# ProyectoFinalTSC

***

|Tabla de contenido             |
|-------------------------------|
|[INTRODUCCIÓN](https://github.com/NefilimZbm/ProyectoFinalTSC#introducci%C3%B3n)                   |
|[METODOLOGIA](https://github.com/NefilimZbm/ProyectoFinalTSC#metodolog%C3%ADa)                    |
|[EXPERIMENTOS](https://github.com/NefilimZbm/ProyectoFinalTSC#experimentos)                    |
|[MAPA](https://github.com/NefilimZbm/ProyectoFinalTSC#mapa )                           |
|[BIBLIOGRAFIAS](https://github.com/NefilimZbm/ProyectoFinalTSC#bibliograf%C3%ADas)                  |

## Introducción
Este repositorio fue creado con la finalidad de presentar el proyecto realizado por Kevin Luis Lagunes, Shaní Sánchez Lara y Pedro Miguel Velásquez Cruz, los cuales somos estudiantes de la licenciatura en Matemáticas de la UV, y consiste en la  aplicación de los conocimientos obtenidos en la experiencia educativa de Temas Selectos De Computación impartida por Patricia González Gaspar.

El propósito de este proyecto es mostrar dos tipos de algoritmos de búsqueda que existen los cuales son: la **búsqueda Greedy** y la **búsqueda A***. 
Cada una de estás búsquedas las utilizaremos para encontrar la ruta más adecuada para ir de un lugar a otro según los criterios de cada una de ellas que se mostraran más adelante.
Esta compuesto por documentos escritos en Python los cuales contienen los algoritmos de busqueda, uno para la búsqueda Greedy y otro para la busqueda A*, y la función que nos permitirá calcular las distancias geograficas entre los diversos lugares, ya que está informaión se requiere para realizar ambas búsquedas, y con la finalidad de ilustrar la situación agregamos un html que está ligado a un JavaScript, los cuales nos serviran para mostrar donde están los lugares que ocuparemos a la hora de crear los algoritmos de las búsquedas.
Para ver el mapa de clic [aquí](https://nefilimzbm.github.io/ProyectoFinalTSC/)

Para comprender el repositorio es importante que contestemos las siguientes preguntas: _¿qué es una búsqueda?, ¿para qué sirve? y ¿por qué son importantes?_.

\\Terminar introducción.

## Metodología

La **Busqueda A\*** fue presentada por Peter E. Hart, Nils J. Nilsson y Bertram Raphael en el año 1968. Su función es encontrar siempre y cuando se cumplan determinadas condiciones, el camino de menor costo entre un nodo origen y uno objetivo, es la forma más ampliamente conocida de la búsqueda primero el mejor, siendo la búsqueda A* tanto completa como óptima. En este trabajo la ocuparemos para que nos diga la ruta con menor costo para trasladarnos de un lugar a otro.

![algoritmo A*](images/astar.png)

En esta parte de las busquedas A\* es necesario el uso de un diccionario que contenga posiciones geologícas, puntos aledaños y costos de entrada a cada punto, al momento de entrar nos pedira origen y destino para poder hacer el ejecutar la funcion, después basado en la distancia y el costo minimo en cada punto con respecto a sus vecinos ese generara la ruta mas corta y economica entre ciudades, al momento de terminar los ciclos y condicionales se imprimra la lista de la ruta que el programa considero mas optima.

Las **Busquedas Grerdy**, también conocido como codigo voraz, es una busqueda de la forma heurística, consistente en elegir la opción óptima en cada paso local con la esperanza de llegar a una solución general óptima. Se utilizan generalmente para resolver problemas de optimización (obtener el máximo o el mínimo), suelen ser fáciles y óptimos.
con respecto a nuestro busqueda agregamos un diccionario que contiene todos los elemenos necesarios para la busqueda como son la posicion, vecinos y costos de caseta y cobustible. En adelante acupamos el algorito siguiente:

![algoritmo Greedy](images/algoritmog.png)

Como anteriormente hemos mencionado esto optimisa y gasta menos datos de información, esto en base a los **Diccionarios** quienes contienen la informacion nesesaria bajo una palabra clave para localizar elementos con mayor facilidad como son la posicion geologíca, sus vecino. Al momento de ejecutar el programa nos pedira una clave de partida y otra clave mas del destino al que queremos llegar, dado esto el programa buscara la rutas más rapida comparada en distancia deacuerdo a los criterios que se mencinen en el diccionario siguiendo una ruta para poder llegar a su destino de no hacerlo, buscara las segundas opciones del final al inicio hasta encontrar su destino, al concluir esto, dara como respuesta una lissta de todos los puntos que fueron necesarios pasar para llegar a su destino.

## EXPERIMENTOS

### Para la busqueda Greedy:
#### RUTA ALVARADO-SAN ANDRÉS TUXTLA:
![rutagreedy1](images/alv-sat.png)
#### RUTA BOCA DEL RIO-TEZIUTLÁN:
![rutagreedy2](images/b-tez.png)
### RUTA XALAPA-FORTÍN DE LAS FLORES:
![rutagreedy3](images/x-f.png)
### RUTA VEGA DE ALATORRE-ACAYUCAN:
![rutagreedy4](images/v-a.png)

### Para la búsqueda A*:
#### RUTA ALVARADO-SAN ANDRÉS TUXTLA:
![rutaae1](images/alv-sat1.png)
#### RUTA BOCA DEL RIO-TEZIUTLÁN:
![rutaae2](images/b-tez1.png)
### RUTA XALAPA-FORTÍN DE LAS FLORES:
![rutaae3](images/x-f1.png)
### RUTA VEGA DE ALATORRE-ACAYUCAN:
![rutaae4](images/v-a1.png)

## CONCLUSIONES:
El objetivo de este proyecto es conocer el comportamiento de diversos tipos de búsquedas, y es por ello que a continuación se mostrará lo que sucede con una ruta de Papantla a Agua Dulce para todas las rutas para todas las busquedas, y tomaremos como factor de mayor importancia el tiempo que toman en realizar la busqueda de dicha ruta.
Para ello adjuntaremos las siguientes imagenes:
### BÚSQUEDA DE AMPLITUD
![busquedaamplitud](images/busquedaam.png)
### BÚSQUEDA COSTO UNIFORME
![busquedacostou](images/busquedacu.png)
### BÚSQUEDA GREEDY
![busquedagreedy](images/busquedag.png)
### BÚSQUEDA A*
![busquedaae](images/busquedaae.png)

## TABLA COMPARATIVA
![tablacomparativa](images/tablac.png)

Cómo podemos notar en la tabla anterior, la ruta que es más rápida es la Búsqueda de costo uniforme, y por otra parte la más lenta es la Búsqueda A*, y si lo analizamos esto tiene mucho sentido, ya que la busqueda A* lleva acabo el análisis de diversa información para la creación de su ruta. Por otra parte algo que esperabamos es que la Búsqueda Greedy fuera más rápida que la Búsqueda A*, ya que la primera, a la hora de generar su ruta analiza solo lo que ocurre con las distancias, en cambio la otra debe analizar distancias y costos.

## Bibliografías
* Inteligencia Artificial, Un enfoque moderno, Russell y Norving, capítulos 3 y 4.
* Inteligencia Artificial,Resolución de problemas mediante búsquedas, Dr. Edgard Iván Benítez Guerrero, rescatado de: https://www.uv.mx/personal/edbenitez/files/2010/09/CursoIA10-II-3.pdf
* Descripción de las tecnologías JavaScript, colavoraderes de MDN, rescatado de: https://developer.mozilla.org/es/docs/Web/JavaScript/Descripci%C3%B3n_de_las_tecnolog%C3%ADas_JavaScript
* Markdown & Pygments Lexers Cheat Sheet,Joe di castro, rescatado de: https://joedicastro.com/pages/markdown.html#mark9
* Algoritmo de Búsqueda Heurística A*, EcuRed, rescatado de: https://www.ecured.cu/Algoritmo_de_B%C3%BAsqueda_Heur%C3%ADstica_A*
* Búsqueda Informada, anonimo, rescarado d:https://www.infor.uva.es/~calonso/IAI/Tema4-BusquedaInformada/BusquedaInformada09-00.pdf
//Agrega más fuentes.

