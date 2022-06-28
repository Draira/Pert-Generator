
#from __future__ import print_function

import numpy as np
import random
import math

from critical_methods import Node


def probability(x, p):
    x = np.array(x)
    p = np.array(p)
    y = np.random.rand()

    cdf = np.cumsum(p)
    total = len(x)

    pos = 0

    for n in range(total - 1):
        pos = pos + (y >= cdf.item(n))

    return x.item(pos)

def noditos(total_nodes, pro_edges):   
    lista = []
    
    for i in range(1,total_nodes+1):
        for j in range(i+1,total_nodes+1):
            if j == i:
                continue
        
                
            p = 1 - pro_edges
            has_edge = probability([0, 1], [p, pro_edges])
            
            lista.append([i,j,has_edge])
        
        suma = 0
        
        for k in lista:
            if k[0] == i:
                suma = suma + k[2]
            if k[1] == i:
                suma = suma + k[2]
        
        if suma == 0:
            
            lista[-1][2]=1

    """
    Se añade esto
    """

    suma2 = 0
    lista_vacia = []
    for z in lista:
        suma2 = suma2 + z[2]
        if z[2]==0:
            lista_vacia.append(z)
                 
    if suma2 < total_nodes-1:
       print(suma2,total_nodes-1)
            
       for i in range(total_nodes-1-suma2):
           random.shuffle(lista_vacia)
          
           nuva_conexion = lista_vacia[0]
           indice = lista.index(nuva_conexion)
           lista[indice][2]=1
           lista_vacia.pop(0)
       
    return lista
            
        
    return lista

def camino_critico(copidi):
    """
    Ahora simplemente retornaremos el camino crítico
    """
    lista_aux = []
    for i in range(len(copidi)):
        lista_aux.append(copidi[i][0])
   
    cam_crit = []
    for j in copidi:
        if j[0] ==  max(lista_aux):
            cam_crit.append(j[1])

    return cam_crit, max(lista_aux)


def tiempos_tardios_tempranos(copidi, lista_nodo):
    """
    Esta funcion lo que hace es sacar todas las sumas de cada uno de los 
    """
    lista_tiempos = []
        
    for i in range(len(copidi)):
        suma = 0
        for j in range(len(copidi[i][1])):
            
            for k in range(len(lista_nodo)):
                if str(copidi[i][1][j]) == lista_nodo[k][0]:
                    
                    lista_tiempos.append([lista_nodo[k][0],[suma, suma + lista_nodo[k][1]]])
                    suma = suma + lista_nodo[k][1]
                    break

    """
    Lo que hace este algoritmo es que entrega los tiempos tempranos.
    Es el tiempo de la primera pasada
    """
    tiempos_tempranos = []                   
    for w in range(len(lista_nodo)):
        mayor = 0
        for z in range(len(lista_tiempos)):
            if lista_nodo[w][0] == lista_tiempos[z][0]:
                if mayor == 0:
                    mayor = lista_tiempos[z][1]
                    
                elif lista_tiempos[z][1][1]> mayor[1]:
                    mayor = lista_tiempos[z][1]
        
                else:
                    mayor = mayor
        
        tiempos_tempranos.append([lista_nodo[w][0],mayor])

    """
    Esta funcion lo que hace es sacar todas las sumas de cada uno de los 
    """
    _, maximus = camino_critico(copidi)
    lista_tiempos2 = []

    #Avanzo por cada una de las rutas
    for i in range(len(copidi)):
        suma = maximus
   
        #Tomo los valores de los nodos conectados
        for j in range(len(copidi[i][1])-1,-1,-1):
            
            #Paso por cada uno de los nodos sin repetir
            for k in range(len(lista_nodo)):
                
                if str(copidi[i][1][j]) == lista_nodo[k][0]:
                 
                    lista_tiempos2.append([lista_nodo[k][0],[suma, suma - lista_nodo[k][1]]])
                 
                    suma = suma - lista_nodo[k][1]
               
                    break
    """
    Lo que hace este algoritmo es que entrega los tiempos tempranos.
    Es el tiempo de la primera pasada
    """
    tiempos_tardios = []                   
    for w in range(len(lista_nodo)):
        menor = 0
        for z in range(len(lista_tiempos2)):
            if lista_nodo[w][0] == lista_tiempos2[z][0]:
                if menor == 0:
                    menor = lista_tiempos2[z][1]
                    
                elif lista_tiempos2[z][1][1] < menor[1]:
                    menor = lista_tiempos2[z][1]
        
                else:
                    menor = menor

        menor.reverse()
        tiempos_tardios.append([lista_nodo[w][0], menor])

    """
    Finalmente unimos ambas filas en una, y calculamos la holgura. Al final entrega:
    Nodo | Tiempo más temprano | Tiempo más tardio | Holgura
    """
    lista_finalle = []
    for x in lista_nodo:
        for y in range(len(lista_nodo)):
            if x[0] == tiempos_tempranos[y][0] == tiempos_tardios[y][0]:
                 lista_finalle.append([x[0],tiempos_tempranos[y][1],tiempos_tardios[y][1], tiempos_tardios[y][1][0]-tiempos_tempranos[y][1][0]])
    
    return lista_finalle


def Calculate_pert(x):

    p = Node('project')

    nodos_totales = int(x)

    lista_nodos = []
    lista_nodo2 = []
    lista_nodo = []
    for i in range(1,nodos_totales+1):
        actividad = str(i)

        
        lista_dias = np.arange(1,26)
        random.shuffle(lista_dias)
        cs=sorted(lista_dias[:3])
        Esperanza = (cs[0]+4*cs[1]+cs[2])/6
        duracion = int(round(Esperanza))
        
        
        nodo = p.add(Node(str(actividad), duration=duracion, lag=0))
        lista_nodos.append(nodo)
        lista_nodo2.append([str(i), cs])
        lista_nodo.append([str(i), duracion])



    lita_conexiones = []
    lita_conexiones2 = []
    conexiones = noditos(nodos_totales, .50)

    for lista_conec in conexiones:
        if lista_conec[2] == 1:
            lita_conexiones2.append([lista_conec[0],lista_conec[1]])
            lita_conexiones.append(p.link(str(lista_conec[0]),str(lista_conec[1])))


    p.update_all()

    camino_cto = p.get_critical_path()
    

    #Entrega el nodo| tiempo temprano| tiempo tardio| holgura
    tiempos_tt = tiempos_tardios_tempranos(camino_cto, lista_nodo)

    #Entrega los caminos críticos + la duración final del proyecto
    soluciones_caminos = camino_critico(camino_cto)

    return lista_nodo2, lita_conexiones2, soluciones_caminos, tiempos_tt
