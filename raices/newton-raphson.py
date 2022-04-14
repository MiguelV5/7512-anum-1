from util import *
import math

#Notar que se requiere la g, NO la f a la que se le quiere calcular la raiz. Por lo tanto se debe asegurar que la g ES FUNCIÓN ADMISIBLE: 
# >> La f original debe tener derivada no nula en todo el entorno de p
#Además de esto la semilla debe ser relativamente cercana a la raíz p.
def newton_raphson(g, tolerancia, semilla, n_recursion = 1, prev_p_n = 0) :  #NR CON CRITERIO DE PARO: |p_n - p_n-1| <= tolerancia
    
    iteracion_funcional(g, tolerancia, semilla)


