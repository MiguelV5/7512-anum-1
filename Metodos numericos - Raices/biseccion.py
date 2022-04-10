import math

# a y b son delimitadores del intervalo [a,b]; f es la funcion a buscar su raiz en dicho intervalo.
def biseccion(f, a, b, tolerancia, n_recursion = 0):
    
    #en caso de que a o b sean cercanas a la raiz p
    if abs(f(a)) <= tolerancia :
        print(f"\n [Aprox con tolerancia adecuada]  Raiz encontrada: p == {a} ; En iteracion nro: {n_recursion} ")
        a
    elif  abs(f(b)) <= tolerancia :
        print(f"\n [Aprox con tolerancia adecuada]  Raiz encontrada: p == {b} ; En iteracion nro: {n_recursion} ")
        b
    
    p_n = (a+b)/2
    
    if  abs(f(p_n)) <= tolerancia :
        print(f"\n [Aprox con tolerancia adecuada]  Raiz encontrada: p == {p_n} ; En iteracion nro: {n_recursion} ")
        p_n
    else:
        print(f"\n [Tolerancia no alcanzada aun]  Valor actual de p_n: {p_n} ; En iteracion nro: {n_recursion} ")

        if f(p_n)*f(a) < 0:
            biseccion(f, a, p_n, tolerancia, n_recursion+1)
        else:
            biseccion(f, p_n, b, tolerancia, n_recursion+1)

    
#ejercicio 1 guia 2:
raiz = biseccion(lambda x: math.e**x * (math.sin(x) + math.cos(x) - 2*x - 2), -2.5, -0.5, 0.00001)

