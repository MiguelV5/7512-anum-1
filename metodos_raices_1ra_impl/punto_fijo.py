from util import iteracion_funcional
#import math



# Notar que se requiere la g(x), NO la f(x) a la que se le quiere calcular la raiz. Por lo tanto se debe asegurar que la g ES FUNCIÓN ADMISIBLE:
# 1) Debe existir el punto fijo para g
# 2) El mismo debe ser único
# 
# PUNTO FIJO CON CRITERIO DE PARO: |p_n - p_n-1| <= tolerancia
def punto_fijo(g, tolerancia, semilla):  

    iteracion_funcional(g,tolerancia, semilla)

    


 
#ejemplo del cuaderno (notas de clase):
#raiz = punto_fijo(lambda x: (x**2 - 1)/3 , 0.001, 0)


