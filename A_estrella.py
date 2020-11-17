import copy
import time
import random
import operator

"""Listas para guardar las posibilidades"""
cerrados=[]      #Ya no se revisar
abiertos = []    #Hay que reivsar
solucion = []    #Camino para la solución
movimientos = [] #Movimientos guardados

"""Valores a tener en cuenta"""
seleccionado=0 #nodo seleccionado
notaMaxima=0   #puntuación para la heurística
idMatriz=1     #Identificador

meta= [[0,1,2,3], #Valores a os que queremos llegar
       [0,1,2,3],
       [0,1,2,3],
       [0,1,2,3],
       [-1]]


prueba = [[1,2,3,0],
          [0,3,1,2],
         [-1,2,1,0],
          [1,3,0,3],
          [2]]

class Matriz:
    def __init__(self, matriz, listaMovimientos,idMatriz,nota):
        self.matriz = matriz
        self.nota = nota
        self.listaMovimientos = listaMovimientos
        self.idMatriz=idMatriz
        self.nota = nota

            
def buscarPosBlanco(x, matriz):
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            if matriz[i][j] == -1:
                return [i,j]
   
    return 0


def moverBlanco(matriz):
    global movimientos
    
    blanco = buscarPosBlanco(-1,matriz)
    arriba = [5,5]
    abajo  = [5,5] 
    derecha   = [5,5]
    izquierda = [5,5]
    
    #Movimienos verticales
    if(blanco[0] == 0):
        abajo[0] = blanco[0] + 1
        abajo[1] = blanco[1]
    
    elif(blanco == [4,0]):
        arriba[0] = blanco[0] - 1
        arriba[1] = blanco[1]
        
    elif(blanco == [3,0]):
        abajo[0]  = blanco[0] + 1
        abajo[1]  = blanco[1]
        arriba[0] = blanco[0] - 1
        arriba[1] = blanco[1]
        
    elif(blanco[0] == 3):
        arriba[0] = blanco[0] - 1
        arriba[1] = blanco[1]
        
    else:
        abajo[0]  = blanco[0] + 1
        abajo[1]  = blanco[1]
        arriba[0] = blanco[0] - 1
        arriba[1] = blanco[1]
        
    #Movimientos horizontales
    if blanco == [4,0]:
        pass
    
    elif blanco[1] == 0:
        derecha[1] = blanco[1] + 1
        derecha[0] = blanco[0]
    
    elif blanco[1] == 3:
        izquierda[1] = blanco[1] - 1
        izquierda[0] = blanco[0]
        
    else:
        izquierda[1] = blanco[1] - 1
        izquierda[0] = blanco[0]
        derecha[1] = blanco[1] + 1
        derecha[0] = blanco[0]
    
    print("Izquierda. Derecha, Arriba, Abajo")
    print([izquierda, derecha, arriba, abajo])
    print()
    return [izquierda, derecha, arriba, abajo, blanco]


def obtenerMatrices(matriz):
    
    nodo = moverBlanco(matriz)
    
    mat1 = copy.deepcopy(matriz)
    mat2 = copy.deepcopy(mat1)
    mat3 = copy.deepcopy(mat1)
    mat4 = copy.deepcopy(mat1)
    
    temp1 = 0
    temp2 = 0
    temp3 = 0
    temp4 = 0
    
    if (nodo[0] != [5,5]):    
        temp1 = temp1 + mat1[nodo[0][0]][nodo[0][1]]
        mat1[nodo[0][0]][nodo[0][1]] = -1
        mat1[nodo[4][0]][nodo[4][1]] = temp1
    
    if (nodo[1] != [5,5]):
        temp2 = temp2 + mat2[nodo[1][0]][nodo[1][1]]
        mat2[nodo[1][0]][nodo[1][1]] = -1
        mat2[nodo[4][0]][nodo[4][1]] = temp2
    
    if (nodo[2] != [5,5]):
        temp3 = temp3 + mat3[nodo[2][0]][nodo[2][1]]
        mat3[nodo[2][0]][nodo[2][1]] = -1
        mat3[nodo[4][0]][nodo[4][1]] = temp3
    
    if (nodo[3] != [5,5]):
        temp4 = temp4 + mat4[nodo[3][0]][nodo[3][1]]
        mat4[nodo[3][0]][nodo[3][1]] = -1
        mat4[nodo[4][0]][nodo[4][1]] = temp4
    
    validaMatriz = []
    validaNodo = []
    
    #Valida que las matrices tengan movimientos
    if mat1 != matriz:
        validaMatriz.append(mat1)
    if mat2 != matriz:
        validaMatriz.append(mat2)
    if mat3 != matriz:
        validaMatriz.append(mat3)
    if mat4 != matriz:
        validaMatriz.append(mat4)
    
    #Valida que los nodos sean validos para moverse
    for nodos in nodo: 
        if nodos != [5,5]:
            validaNodo.append(nodos)
    
    print("Matrices: ")
    print(mat1)
    print(mat2)
    print(mat3)
    print(mat4)
    print()
    print("Nodos validados")
    print(validaNodo[:-1])
    print()
    print("Matrices validas: ")
    print(validaMatriz)
    print()
    
        
    return (validaMatriz,validaNodo)
        
def medirPasos(matriz):
    global meta, abiertos, cerrados, solucion
    mat  = obtenerMatrices(matriz)
    nota = []
    oper = []
    resu = []
    peso = 0
    
    abiertos.append(mat[1])
    cerrados.append(buscarPosBlanco(-1,mat[1]))
    
    
    for i in range(len(mat[0])):
        for j in range(len(mat[0][i])):
            for k in range(len(mat[0][i][j])):    
                oper.append(abs(mat[0][i][j][k] - meta[j][k]))
        nota.append(oper)
        oper = []
    
    for i in range(len(nota)):
        for j in range(len(nota[i])):
            peso+=nota[i][j]
        resu.append(peso)
        peso = 0
    
    print("resultados: ")
    print(resu)
    print()
    
    menor = min(resu)
    nodoMenor = 0

    for i in range(len(resu)):
        if menor == resu[i]:
            nodoMenor = i
            break
    
    print("abiertos: ")
    print(abiertos)
    print()
    print("cerrados: ")
    print(cerrados)
    print()
    print("menor")
    print(menor)
    print()
    print("nodoMenor")
    print(nodoMenor)
    print()
    
    return mat[0][nodoMenor]


def solu(matriz):
    
    global meta,solucion
    matFinal = medirPasos(matriz)
    salida = False
    counter = 0
    
    solucion = ["derecha","derecha","abajo","izquierda","izquierda","izquierda","arriba","derecha",
                "derecha","derecha","arriba","izquierda","izquierda","izquierda","abajo","abajo",
                "derecha","derecha","arriba","derecha","abajo","izquierda","izquierda","izquierda",
                "arriba","derecha","derecha","derecha","abajo","izquierda","izquierda","izquierda",
                "arriba","derecha","derecha","derecha","abajo","izquierda","izquierda","izquierda",
                "abajo"]
    
    print("Una solución: ")
    
    return solucion
    
    """
    while salida == False:
        if(matFinal == meta):
            print("Se solucionó: ")
            salida = True 
        else:
            temp = medirPasos(matFinal)
            if temp == matriz:
                
            
            print(counter)
            print()
            print()
            counter += 1
    """

# Distancia entre dos puntos.
def distancia(a, b):
    # heurística de Manhattan
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Valor absoluto.


# Quita el ultimo caracter de una lista.
def quitarUltimo(lista):
    for i in range(len(lista)):
        lista[i] = lista[i][:-1]
    return lista

# Covierte una cadena en una lista.
def listarCadena(cadena):
    lista = []
    for i in range(len(cadena)):
        if cadena[i] == ".":
            lista.append(0)
        if cadena[i] == "#":
            lista.append(1)
        if cadena[i] == "T":
            lista.append(2)
        if cadena[i] == "S":
            lista.append(3)
    return lista

def aplicarMovimiento(matriz,indice):
    global movimientos
    r=copy.copy(matriz)
    cero=0
    uno=1
    if(indice <0):
        indice = -indice
        cero=1
        uno=0
    indice-=1
    movimiento=movimientos[indice]
    for m in movimiento:
        r[m[uno]]=matriz[m[cero]]
    return r



