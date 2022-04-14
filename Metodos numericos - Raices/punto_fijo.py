from impresion import *
import math

START = 0
ROOT_NOT_FOUND_YET = 1
ROOT_FOUND = 2



def punto_fijo(g, tolerancia, semilla, n_recursion = 1, prev_p_n = 0): 


    if n_recursion == 1:
        imprimir_tabla(START)
        p_n = g(semilla)
        err = abs(g(p_n)) #PREV_P_N NO PUEDE USARSE CON VALOR CERO!!!!
    else:
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





