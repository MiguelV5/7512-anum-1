
# funciones de biblioteca permitidas
import numpy as np
from math import isclose

def crear_lista_de_incrementos_hi(tabla_de_datos_sobre_nodos: list):
    h_list = []
    for i in range(len(tabla_de_datos_sobre_nodos)-1):
        h_i = tabla_de_datos_sobre_nodos[i+1][0] - tabla_de_datos_sobre_nodos[i][0]
        h_list.append(h_i)
    return h_list

def crear_lista_de_coeficientes_independientes_ai(tabla_de_datos_sobre_nodos: list):
    a_list = []
    for i in range(len(tabla_de_datos_sobre_nodos)):
        a_i = tabla_de_datos_sobre_nodos[i][1] 
        a_list.append(a_i)
    return a_list


def matriz_A(h_list: list):
    nro_sub_splines = len(h_list)

    A_matrix = [([0]*(nro_sub_splines+1)) for i in range(nro_sub_splines+1)]

    for i in range(nro_sub_splines+1):
        for j in range(nro_sub_splines+1):
            if i == j:
                if i == 0:
                    A_matrix[i][j] = 2 * h_list[i]
                    A_matrix[i][j+1] = h_list[i]
                elif i == nro_sub_splines:
                    A_matrix[i][j] = 2 * h_list[i-1]
                    A_matrix[i][j-1] = h_list[i-1]
                else:
                    A_matrix[i][j-1] = h_list[i-1]
                    A_matrix[i][j] = 2 * (h_list[i-1] + h_list[i])
                    A_matrix[i][j+1] = h_list[i]

    return A_matrix




def matriz_b(h_list: list, a_list: list, derivada_f_x0, derivada_f_xn):
    nro_sub_splines = len(h_list)
    b = []

    for i in range(nro_sub_splines+1):
        if i == 0:
            b.append((3/h_list[i] * (a_list[i+1] - a_list[i])) - (3 * derivada_f_x0))
        elif i == nro_sub_splines:
            b.append((3 * derivada_f_xn) - (3/h_list[i-1] * (a_list[i] - a_list[i-1])))
        else:
            b.append(((3/h_list[i]) * (a_list[i+1] - a_list[i])) - ((3/h_list[i-1]) * (a_list[i] - a_list[i-1])))
    
    return b



def crear_lista_de_coeficientes_lineales_bi(h_list: list, a_list: list, c_list: list):
    nro_sub_splines = len(h_list)
    lista_bi = []

    for i in range(nro_sub_splines):
        b_i = ((1/h_list[i]) * (a_list[i+1] - a_list[i])) - ((h_list[i]/3) * (2 * c_list[i] + c_list[i+1]))
        lista_bi.append(b_i)

    return lista_bi


def crear_lista_de_coeficientes_cubicos_di(h_list: list, c_list: list):
    nro_sub_splines = len(h_list)
    lista_di =[]

    for i in range(nro_sub_splines):
        d_i = (1/(3*h_list[i]))*(c_list[i+1]-c_list[i])
        lista_di.append(d_i)
    return lista_di