# Descripción Reto 4

El chef de la pizzeria “Mominos” sale todas las mañanas a la plaza de mercado a comprar los ingredientes para sus pizzas. Como él tiene una lista con los ingredientes que le hacen falta, quieren saber los ingredientes que puede comprar y el precio a pagar por dicha compra, dada la disponibilidad de productos en la plaza.

Elaborar un programa que permita, dada la disponibilidad de productos que tiene la plaza de mercado y la lista de ingredientes que le faltan al chef, conocer los ingredientes que compró y el precio total que pagó por su compra.

**Entrada:**

Dos cadenas de caracteres. La primer cadena representa un diccionario (en formato JSON) que tiene las parejas ingrediente:precio de todos los ingredientes disponibles en la plaza de mercado, y la segunda representa la lista de ingredientes (separados por espacio) que necesita el chef para preparar sus pizzas.

**Salida:**

Dos cadenas de caracteres, que representan el precio total de los ingredientes y los ingredientes (separados por espacio) que pudo comprar.

**Ejemplo:**

| Entrada      | Salida |
|:--------- | -----:|
| {"t": 66, "u": 72, "d": 90, "r": 84, "j": 36, "g": 50, "s": 94, "q": 62, "f": 35}  | 290 |
| d p h u i e t q     |   d u t q |

| Entrada      | Salida |
|:--------- | -----:|
| {"k": 48, "j": 82, "r": 78, "q": 66, "f": 31, "w": 31, "s": 62, "u": 41}  | 179 |
| w q h o g j     |   w q j |


