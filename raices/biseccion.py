from util import (imprimir_tabla,START,ROOT_FOUND,ROOT_NOT_FOUND_YET) 
import math


# a y b son delimitadores del intervalo [a,b]; f es la funcion a buscar su raiz en dicho intervalo.
#def biseccion(f, a, b, tolerancia, n_recursion = 1): #BISECCION CON CRITERIO DE PARO: |f(p_n)| < tolerancia
#    
#    #en caso de que a o b sean cercanas a la raiz p
#    #if abs(f(a)) < tolerancia :
#    #    print(f"\n [Aprox con tolerancia adecuada]  Raiz encontrada: p == {a} ; En iteracion nro: {n_recursion} ")
#    #    a
#    #elif  abs(f(b)) < tolerancia :
#    #    print(f"\n [Aprox con tolerancia adecuada]  Raiz encontrada: p == {b} ; En iteracion nro: {n_recursion} ")
#    #    b
#    
#    p_n = (a+b)/2
#    err = abs(f(p_n))
#    if  err < tolerancia :
#        print(f"\n [Aprox con tolerancia adecuada]  Raiz encontrada: p == {p_n} ; En iteracion nro: {n_recursion} \n")
#        p_n
#    else:
#        print(f"\n [Tolerancia no alcanzada aun]  Valor actual de p_n: {p_n} ; En iteracion nro: {n_recursion} ")
#
#        if f(p_n)*f(a) < 0:
#            biseccion(f, a, p_n, tolerancia, n_recursion+1)
#        else:
#            biseccion(f, p_n, b, tolerancia, n_recursion+1)





# a y b son delimitadores del intervalo [a,b]; f es la funcion a buscar su raiz en dicho intervalo. prev_p_n es p_n-1 para el criterio de paro
def biseccion(f, a, b, tolerancia, n_recursion = 1, prev_p_n = 0): #BISECCION CON CRITERIO DE PARO: |p_n - p_n-1| <= tolerancia EXCEPTUANDO PRIMERA ITERACION (Porque alli no existe p_n-1)
  
    p_n = (a+b)/2
    
    if n_recursion == 1:
        imprimir_tabla(START)
        err = abs(f(p_n)) #PREV_P_N NO PUEDE USARSE CON VALOR CERO!!!!
    else:
        err = abs(p_n - prev_p_n)

    if err <= tolerancia :
        imprimir_tabla(ROOT_FOUND, p_n, n_recursion, err)
        p_n
    else:
        imprimir_tabla(ROOT_NOT_FOUND_YET, p_n, n_recursion, err)
        if f(p_n)*f(a) < 0:
            biseccion(f, a, p_n, tolerancia, n_recursion+1, p_n)
        else:
            biseccion(f, p_n, b, tolerancia, n_recursion+1, p_n)



    
#ejercicio 1 guia 2:
raiz = biseccion(lambda x: math.e**x * (math.sin(x) + math.cos(x) - 2*x - 2), -2.5, -0.5, 0.00001)

