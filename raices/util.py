
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

START = 0
ROOT_NOT_FOUND_YET = 1
ROOT_FOUND = 2
ROOT_WITH_WARNING = 3
TOLERANCIA_MAXIMA = 1e-15
ITER_MAXIMAS = 500



err_with___pn__pn_1 = 0
err_with___pn__pn_1_over_pn = 1
err_with___f_of_pn = 2



def imprimir_tabla(table_code, p_n = 0, n_iteracion = 0, err = 9999) :

    if table_code == START :
        print(f"\n {bcolors.HEADER} [========================================//========================================] {bcolors.ENDC}\n")
        print(f" {bcolors.OKBLUE}N° iteracion{bcolors.ENDC}    |    {bcolors.OKBLUE}Valor actual de p_n{bcolors.ENDC}    |    {bcolors.OKBLUE}Valor actual de error estimado{bcolors.ENDC} ")

    elif table_code == ROOT_NOT_FOUND_YET:
        print(f"     {n_iteracion}                 {p_n}                 {err} ")
        
    elif table_code == ROOT_FOUND:
        print(f"     {bcolors.OKGREEN}{n_iteracion}{bcolors.ENDC}                 {bcolors.OKGREEN}{p_n}{bcolors.ENDC}                 {bcolors.OKGREEN}{err}{bcolors.ENDC} \n")
        print(f" {bcolors.HEADER} [========================================//========================================] {bcolors.ENDC}\n")

    elif table_code == ROOT_WITH_WARNING:
        print(f"     {bcolors.WARNING}{n_iteracion}{bcolors.ENDC}                 {bcolors.WARNING}{p_n}{bcolors.ENDC}                 {bcolors.WARNING}{err}{bcolors.ENDC} \n")
        print(f" {bcolors.WARNING} [WARNING] El algoritmo se detuvo aquí.\n            La busqueda realizó un valor muy alto de iteraciones; o la tolerancia dada fue demasiado precisa y se llegó al máximo representable. {bcolors.ENDC}\n")
        print(f" {bcolors.HEADER} [========================================//========================================] {bcolors.ENDC}\n")


# Iteración funcional p_n = g(p_n-1) para todo n>=1  con:  g(x) = x - @(x)*f(x) ;   y   |p_n - p_n-1| <= tolerancia.
# Notar que se requiere la g, NO la f a la que se le quiere calcular la raiz. Por lo tanto se debe asegurar que la g ES FUNCIÓN ADMISIBLE (SEGUN SEA QUE ESTA FUNCION SE USE CON PUNTO_FIJO O CON NR)
# Al llamarse por primera vez p__n-1 DEBE SER LA SEMILLA.
def iteracion_funcional(g, tolerancia, p__n_1, n_recursion = 1) :

    if n_recursion == 1:
        imprimir_tabla(START)
    
    p_n = g(p__n_1)
    err = abs(p_n - p__n_1)

    if err <= tolerancia :
        imprimir_tabla(ROOT_FOUND, p_n, n_recursion, err)
        p_n
    else:
        imprimir_tabla(ROOT_NOT_FOUND_YET, p_n, n_recursion, err)
        iteracion_funcional(g, tolerancia, p_n, n_recursion+1)
