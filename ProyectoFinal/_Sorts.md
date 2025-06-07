# Algoritmos de Ordenamiento

Este documento contiene una explicación general, complejidad y comportamiento de los algoritmos de ordenamiento implementados que son:

- Insertion                 (Interativo)                        in-place
- Shell                     (Interativo)                        in-place
- Merge                     (Recursivo)                         no-in-place
- Tim                       (Hibrido interativo, recursivo)     no-in-place
- Selection                 (Interativo)                        in-place
- Quick                     (Recursivo)                         in-place
- Heap                      (Interativo)                        in-place
- Intro #no se desarrollo   (Hibrido interativo, recursivo)     in-place
- Cycle                     (Interativo)                        in-place
- Counting                  (Interativo)                        no-in-place
- Radix                     (Interativo)                        no-in-place

En todos los algoritmos immplementados puse la opción de reverse inicializada como False, en los algoritmos de comparación usamos
el metodo comparar(a,b) el cual regresaba a < b si reverse era verdadero si no a > b, en algunos codigos la comparación estaba invertida
o se le cambiaban por => y =<.

# Explicación de los algoritmos de ordenamiento asumiendo que (reverse = False)
## Insertion
**Descripción:**
Este algoritmo toma elemento por elemento y lo compara con los elementos que esten a la izquierda de su posisión inicial y los va
recorriendo hasta que encuentra el lugar donde a la izquierda no hay un elemento mayor que este.

**Complejidad:**
- Mejor caso: O(n)
- Promedio: O(n²)
- peor caso: O(n²)
- Espacio: O(1)

## Shell
**Descripción:**
Este algoritmo extiende Insertion sort solo que en vez de recorrer toda la lista, recorre secciones de la lista y va haciendo esas secciónes
más chicas.

**Complejidad:**
- Mejor caso: O(n log n)
- Promedio: O(n log² n)
- Peor caso: O(n²)
- Espacio: O(1)

## Merge
**Descripción:**
Este algoritmo se basa en divide y venceras, en donde en vez de recorrrer la lista, la sub dibide en dos arreglos uno de la parte izquierdfa
y otro de la parte derecha y cada uno de estos arreglos los vuelve a enviar a si mismo para que sub divida y así hasta tener arreglos de 1
solo elemento que convina en orden y pasa ese arreglo unido a las diviciones anteriores para que los unan, hasta optener el arreglo completo
ordenado por las diviciones y convinaciones.

**Complejidad:**
- Mejor: O(n log n)
- Promedio: O(n log n)
- Peor caso: O(n log n)
- Espacio: O(n)

## Tim
**Descripción:**
tim sort es una convinación entre insertion sort y merge sort en donde se mandan rangos de la lista de finidos por min_runs, sulen ser de 32 a 64
elementos, que se ordenan con insertionSort dentro de la misma lista y luego se conbinan esos rangos de la lista con merge sort convinando los
primeros 32/64 elementos con los segundos y así hasta llegar al final de la lista, luego min_runs es duplicado, 64/128 y convina los primeros
64/128 con los segundos 64/128 y terceros con cuartyos y segue hacendo las convinaciónes hasta que min_runs sea mayor que el tamaño del arreglo.

**Complejidad:**
- Mejor caso: O(n)
- Promedio: O(n log n)
- Peor caso: O(n log n)
- Espacio: O(n)

## Selection
**Descripción:**
Este algoritmo mediante iteraciones encuentra el elemento menor y lo intercambia por el que esta en la primera posición luego repite el proceso
con la demás lista y pone el segundo elemento más chico en la segunda posición y así consecutivamente hasta encontrar el ultimo elemento más
chico que ya seria el más grande en la lista en general.

**Complejidad:**
- Mejor caso: O(n²)
- Promedio: O(n²)
- peor caso: O(n²)
- Espacio: O(1)

## Quick
**Descripción:**
Este elige un pivote que general mente es el ultimo elemento y manda todos los elementos mayores a el a la derecha luego se manda a si mismo
a ordenar la parte anterior a el pivote y la parte posterior al mismo, el pivote ya se encuentra en su posición final ya que a la izquierda no
tiene ni un elemento mayor y a la derecha no tiene ninugn elemento menor que el.

**Complejidad:**
- Mejor: O(n log n)
- Pomedio: O(n log n)
- Peor caso: O(n²)
- Espacio: O(log n)

## Heap
**Descripción:**
Este algoritmo primero crea una arbol binario por monticulos en donde el primer elemento es el mayor y tiene dos hijos y los hijos pueden tener
hijos, para localizar los hijos debes saber que el priimer hijo se encuentra en la posision del padre por dos y el segundo hijo es el siguiente
elemento en la lista, luego que ya se tiene hecha el arbol se intercambia el primer elemento por el ultimo y el primer elemento ahora va
intercambiandose por siu hijo mayor hasta recuperar la condición del heap que ningun hijo puede ser mayor a el padre, y se repite este proceso
para obtener una lista ordenada.

**Complejidad:**
- Mejor: O(n log n)
- Promedio: O(n log n)
- Peor caso: O(n log n)
- Espacio: O(1)

## Intro
**Descripción:**


**Complejidad:**
- Mejor: O(n log n)
- Promedio: O(n log n)
- Peor caso: O(n log n)
- Espacio: O(n log n)

## Cycle
**Descripción:**
El algoritmo toma el primer elemento y lo compara con los demás elementos y va sumando 1 a la posición que se le asignara, luego cuando
recorre toda la lista y tiene la posición final del elemento compara el elemento con el que se encuentra en la posición que se le asignara
si es igual a la posición se le suma uno hasta encontrar una posición que no tenga un elemento igual en donde se pone ese elemento y ahora
se trabaja con el elemento que estaba en esa posición buscando su posición esto se repite hasta que la posición que se le asigne a el
elemento sea igual a la primera posición y ahi empieza el proceso de nuevo pero desde la segunda posición y así consecutivamente.

**Complejidad:**
- Mejor caso: O(n²)
- Promedio: O(n²)
- peor caso: O(n²)
- Espacio: O(1)
- Ideal para minimizar escrituras (útil en EEPROM)


## Counting
**Descripción:**
Este ordenamiento se da haciendo un arreglo de 0 representando cada 0 un numero desde el más pequeño de la lista hasta el más grande y luego se recorre la lista contando cuantos elementos aparecen de cada valor, sumandolo en el elemento de la matriz de ceros despues se cada elemento suma a el elemento anterior para obtener hasta que lugar de la lista resultante ocupara ese valor, por ejemplo [3,5,5,5,6,7] en donde el valor más pequeño es 7 y el más grande es 12, seria [7,7,7,8,8,11,12].

**Complejidad:**
- Mejor caso: O(n + k)
- Promedio: O(n + k)
- peor caso: O(n + k)
- Espacio: O(k)
*(k = valor máximo)*

## Radix
**Descripción:**
Este usa couting para ordenar sus valores, pero aqui va ordenando por el valor posicional, osea primero ordena por las unidades de los numeros luego por las decenas y así continua hasta donde sea necesario, ejemplo: [12,543,2,4,123,72,49,3] -> [12,2,72,543,123,3,4,49] -> [2,3,4,12,123,543,49,72] -> [2,3,4,12,49,72,123,543]

**Complejidad:**
- Mejor caso: O(n * k)
- Promedio: O(n * k)
- peor caso: O(n * k)
- Espacio: O(k)
*(k = valor máximo)*
