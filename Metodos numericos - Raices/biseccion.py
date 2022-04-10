import math

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class tablecodes:
    START = 0
    ROOT_NOT_FOUND_YET = 1
    ROOT_FOUND = 2


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
#    
#    if  abs(f(p_n)) < tolerancia :
#        print(f"\n [Aprox con tolerancia adecuada]  Raiz encontrada: p == {p_n} ; En iteracion nro: {n_recursion} \n")
#        p_n
#    else:
#        print(f"\n [Tolerancia no alcanzada aun]  Valor actual de p_n: {p_n} ; En iteracion nro: {n_recursion} ")
#
#        if f(p_n)*f(a) < 0:
#            biseccion(f, a, p_n, tolerancia, n_recursion+1)
#        else:
#            biseccion(f, p_n, b, tolerancia, n_recursion+1)

def imprimir_tabla(table_code, p_n = 0, n_recursion = 0) :

    if table_code == tablecodes.START :
        print(f"\n {bcolors.OKBLUE}          [BISECCION] {bcolors.ENDC}")
        print(f" {bcolors.OKBLUE}N° iteracion{bcolors.ENDC}  |  {bcolors.OKBLUE}Valor actual de p_n{bcolors.ENDC}")
    elif table_code == tablecodes.ROOT_NOT_FOUND_YET:
        print(f"     {n_recursion}              {p_n} ")
    elif table_code == tablecodes.ROOT_FOUND:
        print(f"     {bcolors.OKGREEN}{n_recursion}{bcolors.ENDC}              {bcolors.OKGREEN}{p_n}{bcolors.ENDC} \n")



# a y b son delimitadores del intervalo [a,b]; f es la funcion a buscar su raiz en dicho intervalo. prev_p_n es p_n-1 para el criterio de paro
def biseccion(f, a, b, tolerancia, n_recursion = 1, prev_p_n = 0): #BISECCION CON CRITERIO DE PARO: |p_n - p_n-1| < tolerancia
    
    if n_recursion == 1 :
        imprimir_tabla(tablecodes.START)

    p_n = (a+b)/2
    
    if abs(p_n - prev_p_n) < tolerancia :
        imprimir_tabla(tablecodes.ROOT_FOUND, p_n, n_recursion)
        p_n
    else:
        imprimir_tabla(tablecodes.ROOT_NOT_FOUND_YET, p_n, n_recursion)
        if f(p_n)*f(a) < 0:
            biseccion(f, a, p_n, tolerancia, n_recursion+1, p_n)
        else:
            biseccion(f, p_n, b, tolerancia, n_recursion+1, p_n)



    
#ejercicio 1 guia 2:
raiz = biseccion(lambda x: math.e**x * (math.sin(x) + math.cos(x) - 2*x - 2), -2.5, -0.5, 0.00001)

