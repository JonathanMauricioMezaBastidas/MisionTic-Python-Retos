# Descripción Reto 1

Se quiere priorizar la vacunación de la ciudadanía  y se estructuraron una serie de fases de vacunación (Fase 1, Fase 2, Fase 3, Fase 4). La asignación de las personas a cada una de las fases está basada en una serie de factores de riesgo, los cuales al ser calculados permitirían dar la fase de vacunación en la cual estará.

Los valores de cada factor de riesgo serán obtenidos de la siguiente manera:

-        El primer factor de riesgo (FR-1) está asociado a un Índice de Vulnerabilidad propuesto por el instituto de planeación ADNE. Este índice es construido de acuerdo con parámetros como: comorbilidad, hacinamiento, densidad poblacional, entre otros. Este Índice de Vulnerabilidad es transformado a factor de riesgo utilizando la función de parte entera int, la cual toma un número real (Índice de Vulnerabilidad) y devuelven el número entero más próximo (FR-1).

-        El segundo factor de riesgo (FR-2) es construido usando la siguiente relación: el doble del valor del primer factor de riesgo (FR-1) es igual al valor del segundo factor de riesgo (FR-2) menos cuatro.

-        El tercer factor de riesgo (FR-3) es tomado como relación de FR-1 y FR-2 como sigue: cinco veces el valor del tercer factor de riesgo (FR-3) es igual a la suma de los valores obtenidos en el primer y segundo factor de riesgo, FR-1 y FR-2 respectivamente.

La fase de vacunación de la persona estará dada por el valor obtenido del tercer factor de riego FR-3. Si el valor de FR-3 está entre 0 y 20, la persona estará priorizado para la fase 1. Si el valor se encuentra entre 21 y 30, la persona estará priorizado para la fase 2. En caso de que el valor de FR-3 este entre 31 y 50, su priorización será la fase 3. Finalmente, si el valor de FR-3 es mayor a 51, la persona será priorizada para la fase 4.

Elabora un programa que permita, dado el Índice de Vulnerabilidad de la persona, conocer los valores obtenidos en los diferentes factores de riesgo (FR-1, FR-2, FR-3), así como la fase de vacunación en la que se encuentra cada persona.

Nota: Los factores de riesgo son números enteros, en caso de necesitarlo se puede usar la función de parte entera int.

**Entrada**

La entrada es un número que representa el Índice de Vulnerabilidad de la persona.

**Salida**

Tres enteros separados por espacio que representan las valores para cada uno de los factores de riesgo FB-1, FB-2 y FB-3. En la siguiente línea en letras la fase de vacunación en la cual se encuentra la persona.

| ENTRADA      | SALIDA |
| --------- | -----:|
| 178  | 178 360 107 |
|      |   cuatro |
| 29      |    29 62 18 |
|       |    dos |
