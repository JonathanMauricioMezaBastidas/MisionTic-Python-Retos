# Descripción Reto 3

El gobernante de la ciudad de Nuncalandia quiere implementar un sistema de vigilancia epidemiológico en cada establecimiento, con el fin de poder rastrear a todas las personas que ingresan al mismo. Para ello, ubica una cámara inteligente que registra cuantas veces ingresa una persona al establecimiento. Al final del día, la cámara tiene registro de todas las personas que ingresaron al establecimiento.

Elaborar un programa que permita, dado el registro de personas que ingresaron al establecimiento, conocer la cantidad de veces que una persona ingresó al establecimiento antes de que el sistema registrara el ingreso de otra persona.

**Entrada:**

Una cadena de caracteres separada por espacios que representa las personas que ingresaron al establecimiento.

**Salida:**

Dos cadenas de caracteres. La primera cadena que representa las personas que van ingresando al establecimiento y la segunda representa la cantidad de veces que ingresaron a este, antes de que el sistema registrara a otra persona.

**Ejemplo:**

| Entrada      | Salida |
|:---------:|:-----:|
| D D D D T T T D A A T T T A A A U Y U U U  | D T D A T A U Y U |
|      |   4 3 1 2 3 3 1 1 3 |

| Entrada      | Salida |
|:---------:|:-----:|
| U U U U U D D B D D T T T I B T T T T U U U U  | U D B D T I B T U |
|      |   5 2 1 2 3 1 1 4 4 |

