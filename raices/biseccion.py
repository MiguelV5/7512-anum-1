from util import (imprimir_tabla,START,ROOT_FOUND,ROOT_NOT_FOUND_YET) 
import math


# a y b son delimitadores del intervalo [a,b]; f es la funcion a buscar su raiz en dicho intervalo.
def biseccion(f, a, b, tolerancia, n_recursion = 1, p__n_1 = 0): #BISECCION CON CRITERIO DE PARO: |p_n - p_n-1| <= tolerancia EXCEPTUANDO PRIMERA ITERACION (Porque alli no existe p_n-1)
  
    p__n = (a+b)/2
    
    if n_recursion == 1:
        imprimir_tabla(START)
        err = abs(f(p__n)) # p__n-1 NO PUEDE USARSE CON VALOR CERO!!!!
    else:
        err = abs(p__n - p__n_1)

    if err <= tolerancia :
        imprimir_tabla(ROOT_FOUND, p__n, n_recursion, err)
        p__n
    else:
        imprimir_tabla(ROOT_NOT_FOUND_YET, p__n, n_recursion, err)
        if f(p__n)*f(a) < 0:
            biseccion(f, a, p__n, tolerancia, n_recursion+1, p__n)
        else:
            biseccion(f, p__n, b, tolerancia, n_recursion+1, p__n)



    
#ejercicio 1 guia 2:
raiz = biseccion(lambda x: math.e**x * (math.sin(x) + math.cos(x) - 2*x - 2), -2.5, -0.5, 0.00001)

