from impresion import *
import math


def punto_fijo(g, tolerancia, semilla, n_recursion = 1, prev_p_n = 0):  #PUNTO FIJO CON CRITERIO DE PARO: |p_n - p_n-1| <= tolerancia

    if n_recursion == 1:
        imprimir_tabla(START)
        prev_p_n = semilla  #PREV_P_N NO PUEDE USARSE CON VALOR CERO!!!!
    
    p_n = g(prev_p_n)
    err = abs(p_n - prev_p_n)

    if err <= tolerancia :
        imprimir_tabla(ROOT_FOUND, p_n, n_recursion, err)
        p_n
    else:
        imprimir_tabla(ROOT_NOT_FOUND_YET, p_n, n_recursion, err)
        punto_fijo(g, tolerancia, semilla, n_recursion+1, p_n)

    


 
#ejemplo del cuaderno (notas de clase):
raiz = punto_fijo(lambda x: (x**2 - 1)/3 , 0.001, 0)


