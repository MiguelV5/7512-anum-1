from util import iteracion_funcional
#import math

# Notar que se requiere la g, NO la f a la que se le quiere calcular la raiz. Por lo tanto se debe asegurar que la g ES FUNCIÓN ADMISIBLE: 
# >> La f original es C^2[a,b].
# >> La f original debe tener derivada no nula en todo el entorno de p.
#Además de esto la semilla debe ser relativamente cercana a la raíz p.
# 
# NR CON CRITERIO DE PARO: |p_n - p_n-1| <= tolerancia
def newton_raphson(g, tolerancia, semilla) :  
    
    iteracion_funcional(g, tolerancia, semilla)




#ejercicio 2 de clase teorica 3 - NR
#raiz = newton_raphson(lambda x: x - (x**10 - 1)/(10*x**9), 0.01, 0.8)



# NOTA:
# Para NR para raíces multiples 
# >> La f original debe tener derivada de orden m no nula en todo el entorno de p, siendo nulas todas las derivadas de orden menor que m en la raiz p.
# Como la g tambien debe ser calculada a mano, simplemente usar la misma funcion newton_raphson(), pero asegurandose de cumplir lo anterior adicionalmente.
