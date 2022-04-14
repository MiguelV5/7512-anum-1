from util import iteracion_funcional
import math



#Notar que se requiere la g, NO la f a la que se le quiere calcular la raiz. Por lo tanto se debe asegurar que la g ES FUNCIÓN ADMISIBLE:
# 1) Debe existir el punto fijo para g
# 2) El mismo debe ser único
def punto_fijo(g, tolerancia, semilla, n_recursion = 1, prev_p_n = 0):  #PUNTO FIJO CON CRITERIO DE PARO: |p_n - p_n-1| <= tolerancia

    iteracion_funcional(g,tolerancia, semilla)

    


 
#ejemplo del cuaderno (notas de clase):
raiz = punto_fijo(lambda x: (x**2 - 1)/3 , 0.001, 0)


