from util import (imprimir_tabla, START, ROOT_FOUND, ROOT_NOT_FOUND_YET)
#import math


#Al llamarse inicialmente p__n-1 debe ser la semilla_1; p__n-2 debe ser la semilla_0
def iteracion_funcional_de_dos_semillas(g, tolerancia, p__n_1, p__n_2, n_recursion = 1) :
    
    if n_recursion == 1:
        imprimir_tabla(START)
    
    p_n = g(p__n_1, p__n_2)
    err = abs(p_n - p__n_1)

    if err <= tolerancia :
        imprimir_tabla(ROOT_FOUND, p_n, n_recursion, err)
        p_n
    else:
        imprimir_tabla(ROOT_NOT_FOUND_YET, p_n, n_recursion, err)
        iteracion_funcional_de_dos_semillas(g, tolerancia, p_n, p__n_1, n_recursion+1)



#Notar que se requiere la f(x) a la que se le quiere calcular la raiz. Por lo tanto se debe asegurar: 
# >> La f original es C^2[a,b].
# >> La f original debe tener derivada no nula en todo el entorno de p.
#Además de esto se requieren DOS SEMILLAS en el intervalo.
def secante(f, tolerancia, semilla_1, semilla_0) :  #Secante CON CRITERIO DE PARO: |p_n - p_n-1| <= tolerancia
    
    # g == p_n ; x == p_n-1 ; y == p_n-2
    g = lambda x,y: x - (f(x)*(x-y))/(f(x) - f(y))

    iteracion_funcional_de_dos_semillas(g, tolerancia, semilla_1, semilla_0)



#ejercicio 2 de clase teorica 3 - NR
#raiz = secante(lambda x: x**10 - 1 , 0.01, 0.8, 0.2) #FALLA: ESTAS SEMILLAS SON MALAS 
# http://www.ohiouniversityfaculty.com/youngt/IntNumMeth/lecture6.pdf
# https://www.geogebra.org/calculator/xcetshx6

# Esta converge correctamente: 
#raiz = secante(lambda x: x**10 - 1 , 0.01, 1.3, 1.2)  #tuvo 6 iteraciones

# Aunque creía que por lo general convendria que las semillas estuviese "rodeando" una a cada lado de la raiz real, esto no siempre se cumple y en realidad depende muchisimo de como es la función y de las semillas que se den.
#  Comparar iteraciones con la anterior:
#raiz = secante(lambda x: x**10 - 1 , 0.01, 1.3, 0.8) #tuvo 8 iteraciones, por culpa de que la recta secante inicial.
