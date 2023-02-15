## Introducción.
En este proyecto se explicará el proceso que seguíré para realizar mi primer programa utilizando conceptos de inteligencia artificial, esperando que sea de utilidad para la comunidad, tratando de explicar todo de la forma más simple posible.

## Problema.
En este proyecto se busca optimizar los caminos o rutas en un plano. El plano muestra los diferentes sitios y calles por donde se puede transitar.

Realizar un programa computacional ayudado de la inteligencia artificial (porblema que resolveremos inicialmente con el algortimo Q-Learning) que en cada momento que se solicite, arroje la ruta óptima para ir desde un punto inicial a uno final, con posibles restricciones o imposisciones de paso por algún lugar.

## Desarrollo.

### Planteamiento (1).
Para comenzar me gustaría comzar sencillo, entoces lo que haré en esta parte será solo hacer que aprenda a moverse por los nodos que estan conectados.

De ejemplo crearé un mapa de 16 nodos para hacer las pruebas.
![Diagrama de los nodos del plano de ejemplo](https://drive.google.com/uc?export=view&id=1izct1E1WojqY243KIqCGbX_S1nGUn8tW)

Ahora crearé un diccionario relacionando el nombre del nodo con un valor numero desde 0 hasta el número de nodos que tenemos, en este caso 0 a 15

![Diccionario de realcion nombre del nodo - valor](https://drive.google.com/uc?export=view&id=1EoaO4erhCuvocNVTAJhken5DxG7N3n85)

También haré una matriz llamada **'rewards'** para establecer los nodos que están conectados.

![Matriz de posibles transiciones](https://drive.google.com/uc?export=view&id=18SXUz20WgA7Y-vVuR4krplFdZbCkOOJd)

El funcionamiento de la matriz es el siguiente, las columnas y renglones representan cada uno de los nodos y el punto donde se cruzan será si se puede trancitar de uno a otro por ejemplo. en la matriz **rewards[ X, Y ]** donde **X** es el nodo actual y **Y** son todos los nodos a los que en teoría podria moverse, siendo las acciones que el agente puede tomar.

Ahora lo explicaré, tomemos de ejemplo el primer nodo **A** como podemos observar desde este nodo las transiciones válidas serían **[ B, C y E ]**, ahora observemos el diccionario entoces podemos ver los valeres que le corresponden a cada nodo, las cuales serian:
- **A → 0**
- **B → 1**
- **C → 2**
- **E → 4**

Ahora si volvemos a la matriz y usamos los indices serían **X es igual 0** ya que nos encontramos en el nodo **A** entonces **Y** tiene tres valores diferentes **1, 2 y 4** entonces usando las coordenadas quedarían de la siguiente manera.
- **[0, 1]** para transitar de **A → B**
- **[0, 2]** para transitar de **A → C**
- **[0, 4]** para transitar de **A → E**

Entonces en la matriz le asignamos el valor de **1** en esas coordenadas, y al resto que son las transiciones que no son válidas por lo que les asiganos el valor de **0**.

### Solución planteamiento (1).
Como primer objetivo del primer planteamiento me puse el que pueda hacer las transiciones como ayuda visual creé un funcion para mostrar todas las transiciones posibles de cada nodo, la se muestra a continuación.

![Función monstrar transiciones](https://drive.google.com/uc?export=view&id=1NEqvsikE0qMJKmMbZ50yYdV8pj3Sq_Qn)

En nuestro ejemplo la función mostrara como reslutado lo siguiente.

![Función monstrar transiciones](https://drive.google.com/uc?export=view&id=1IWpBXD_nuV7MboVhZA2sRB4FwzsHMUfX)

Con esto nostros podemos ver visualmente si nuestras transiciones están bien hechas pero el programa todavia no cuenta con esa información, entonces el siguiente paso es poder tener esta información en algún lugar para que nuestro programa pueda saber a que nodo puede moverse dependiendo de en que nodo se encuentra.

Para esto nos basamos en la funcion de mostrar pero ahora en luegar de generar una salida por consola generamos una lista con los valores numericos de cada nodo y para prepararme para los futuros pasos a cada transición le agregaré un valor **1** que para comenzar todos comenzarán con el mismo valor, este representa la probalilidad de que el programa transite hacia ese nodo, lo retomaremos más adelante pero de momento lo dejaremos así.

![Función inicializar transiciones válidas](https://drive.google.com/uc?export=view&id=1whJGvAY3KFCUbdGtg1S06uQt4yO2nudv)

Entonces la función nos generaría una lista como la siguiente, la cual es una lista con un diccionario en cada uno de sus elementos.

transitionProbabilities = [ 
    **{ "1" : 1, "2" : 1, "4" : 1},  → posición 0**
    { 'otros valores' }...           → posición 1
]

Ahora explicaré el porque de esta estructura, si nos enfocamos en la primera lista podemos observar que cada indice de la lista podemos relacionarlo con los nodos gracias a nustro diccionario de **states** en el cual vemos que el valor **0** corresponde al **nodo A**, entonces si lo vemos ignorando los diccionarios interiores podemos ver que la relación queda algo así.

transitionProbabilities = [ 
    **{diccionario 0},  → posición 0  → nodo A**
    **{diccionario 1},  → posición 1  → nodo B**
    **{diccionario 2},  → posición 2  → nodo C**
    **{diccionario 3},  → posición 3  → nodo D**
    **{diccionario 4},  → posición 4  → nodo E**
    ...
]

Ahora veamos más cerca los diccionarios, tomemos de ejemplo el diccionario **0** que le corresponde al **nodo A**.

{
    "1" : 1, **→ "valor del nodo a transitar" : probalilidad de transitar a este nodo**
    "2" : 1, 
    "4" : 1
}

Como podemos ver en el diccionario queda establecida la llave o valor del nodo a transitar entonces para el **nodo A** queda algo así.

- **"1" : 1** → 1 de probabilidad de transitar a **A → B → ("1")**
- **"2" : 1** → 1 de probabilidad de transitar a **A → C → ("2")**
- **"4" : 1** → 1 de probabilidad de transitar a **A → E → ("4")**

Ahora un ejemplo práctico, para consultar las transiciones posbiles del **nodo A** debemos buscar en la lista **transitionProbabilities** el elemento con el indice **1** y este nos regresa un diccionario con los nodos validos para transitar y sus posibilidades de transitar a el **{ ("1" : 1), ("2" : 1), ("4" : 1)}** (los parentesís solo los puse para ayudar a identficar cada elemento del diccionario, pero en el programa no los tiene, ni influyen en nada).

Ya que tenemos los nodos a los que podemos transitar ahora toca generar una ruta, para lo que se creó la siguiente función.

![Función para crear rutas](https://drive.google.com/uc?export=view&id=1GqaqTtosbYWbJSyGbcSGCJnwKkkylBSe)

Esta funcio recibe el nodo en el que inicia, la lista con las posibles transiciones, en nodo objetivo y el diccionario de los estados.

Al comenzar podemos ver que se inicializan las variables.

- **actualNode** → esta variable inicia siendo igaul a es punto inicial a cada transicion se debe actualizar al nuevo punto actual.
- **transitionCounter** → variable de control para saber cuantas trasiciones se hicieron.
- **routePoints** → esta variable nos servirá para asignar una puntuación a la ruta generada.
- **route** → variable de texto a la que se le irá agregando el nombre de cada transicion que se haga para mostrarla como resultado.

Ahora entramos en un ciclo **While** mientras **actualNode** sea diferente de **goalNode**

>Tener precaución aqui ya que si no se peude llegar al **goalNode** desde **actualNode** se crea un ciclo infinito, en proximos avances le daremos una solución a esto estableciendo un limite maximo de transiciones.

al comenzar el ciclo consultamos las trasiciones de **actualNode** con la siguiente línea de código y las guardamos en la variable **posibleTransitions**. 

**posibleTransitions** = transitionProbabilities[**actualNode**]

Ahora elegimos aleatoriamente un nodo para hacer la transición con la siguiente línea de código y la guardamos en la variable 

**transitionChoise** = random.choices(list(**posibleTransitions.keys()**), **weights**=list(**posibleTransitions.values()**), k=1)[0]

- **La lista de opciones a elegir**: **list(posibleTransitions.keys())**. Aquí se convierten las claves del diccionario opciones en una lista de Python, que servirá como lista de opciones para la función **choices()**.

- **Los pesos de cada opción**: **list(posibleTransitions.values())**. Aquí se convierten los valores del diccionario opciones en una lista de Python, que especifica las probabilidades de cada opción en la lista anterior. Estas probabilidades se utilizan para determinar la probabilidad de elegir cada opción. En este caso, se están utilizando los valores del diccionario opciones directamente como pesos, lo que significa que las opciones con valores más altos tendrán una probabilidad mayor de ser elegidas.

- **El número de elementos a elegir**: **k=1**. Aquí se especifica que solo se quiere elegir un elemento de la lista de opciones.

Después de elegir la transición actualizamos **actualNode** con el valor del nuevo nodo con la siguiente línea.

- **actualNode** = int(**transitionChoise**)

Actualizamos nuestros contadores con:

- **transitionCounter** += 1 → le sumamos uno porque se hizo una transición.
- **routePoints** -= 1 → aquí le restamos un punto el cual será el costo por hacer una transición, de momento todas tendrán puntos negativos.

> El plan aquí es que después le demos puntos por llegar a determinado nodo o cumplir ciertos objetivos, por ejemplo darle 100 puntos al pasar por un Nodo con la prioridad más alta, así entre menos transiciones haga menos puntos perderá por lo tanto al llegar a ese punto tendrá una mayor cantidad de puntos.

> También se espera que al final de craer la ruta compare esta con una ruta anterior y si esta resulta tener más puntos subir la prioridad de las transiciones que hizo en esa ruta y bajar las demas para que cada que logre mejorar la ruta a la proxima generación tenga una mayor posiblilidad de generar una ruta más óptima.

Por último agregamos el nombre del nodo a nuestro string con las trnsiciones textuales para tener un resultado más visual e imprimimos nuestros resultados.

- route += ' --> ' + get_key_by_value(states, int(transitionChoise))
  
imprimir resultados.

- print('Transiciones realizadas: {}'.format(transitionCounter))
- print('Puntuacion: {}'.format(routePoints))

- print('Ruta: {}'.format(route))

### Funciones no relevantes.
Una funcion que no es esencial es **get_key_by_value**.

![Función para crear rutas](https://drive.google.com/uc?export=view&id=1jqnu6v8PAnIMGBFKwjZju62Pc_un_dNQ)

La cual recibe como parametros el diccionario **states** y el valor que se busca, esto para devolver el nombre del nodo.

### Resultados planteamiento(1)

Al ejetutar nustro código nos genera nuestra primera ruta aleatoria para llegar de un punto a otro, dando en consola un mesaje parecido a este.

![Función para crear rutas](https://drive.google.com/uc?export=view&id=1VJbJbyRnrXa7t1UxK8dpFoYkxepp2QgM)

En la imagen vemos que se realizaron 7 transiciones, gastando un punto por cada una y sin recibir ningún tipo de recompensa, la ruta generada para ir del **nodo A** al **nodo O** fue la siguiente.

- A → C → E → C → G → H → K → O