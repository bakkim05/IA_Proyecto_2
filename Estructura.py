from Nodo import Nodo
from Reader import MatrixReader
import numpy as np

class Estructura:
    def __init__(self):
        self.reader = MatrixReader("matrix.txt")
        self.mr = self.reader.getMatrix()

        #inicializar 
        self.layer0 = [Nodo(self.mr[16])]
        self.layer1 = [Nodo(self.mr[12]),Nodo(self.mr[13]),Nodo(self.mr[14]),Nodo(self.mr[15])]
        self.layer2 = [Nodo(self.mr[8]),Nodo(self.mr[9]),Nodo(self.mr[10]),Nodo(self.mr[11])]
        self.layer3 = [Nodo(self.mr[4]),Nodo(self.mr[5]),Nodo(self.mr[6]),Nodo(self.mr[7])]
        self.layer4 = [Nodo(self.mr[0]),Nodo(self.mr[1]),Nodo(self.mr[2]),Nodo(self.mr[3])]

        self.connect()


    def connect(self):
        #Conexiones Layer 0
        self.layer0[0].up = self.layer1[0]

        #Conexiones Layer 1
        self.layer1[0].down = self.layer0[0]
        self.layer1[0].up = self.layer2[0]
        self.layer1[0].left = self.layer1[3]
        self.layer1[0].right = self.layer1[1]

        self.layer1[1].up = self.layer2[1]
        self.layer1[1].left = self.layer1[0]
        self.layer1[1].right = self.layer1[2]

        self.layer1[2].up = self.layer2[2]
        self.layer1[2].left = self.layer1[1]
        self.layer1[2].right = self.layer1[3]

        self.layer1[3].up = self.layer2[3]
        self.layer1[3].left = self.layer1[2]
        self.layer1[3].right = self.layer1[0]

        #Conexiones Layer 2
        self.layer2[0].down = self.layer1[0]
        self.layer2[0].up = self.layer3[0]
        self.layer2[0].left = self.layer2[3]
        self.layer2[0].right = self.layer2[1]

        self.layer2[1].down = self.layer1[1]
        self.layer2[1].up = self.layer3[1]
        self.layer2[1].left = self.layer2[0]
        self.layer2[1].right = self.layer2[2]

        self.layer2[2].down = self.layer1[2]
        self.layer2[2].up = self.layer3[2]
        self.layer2[2].left = self.layer2[1]
        self.layer2[2].right = self.layer2[3]

        self.layer2[3].down = self.layer1[3]
        self.layer2[3].up = self.layer3[3]
        self.layer2[3].left = self.layer2[2]
        self.layer2[3].right = self.layer2[0]

        #Conexiones Layer 3
        self.layer3[0].down = self.layer2[0]
        self.layer3[0].up = self.layer4[0]
        self.layer3[0].left = self.layer3[3]
        self.layer3[0].right = self.layer3[1]

        self.layer3[1].down = self.layer2[1]
        self.layer3[1].up = self.layer4[1]
        self.layer3[1].left = self.layer3[0]
        self.layer3[1].right = self.layer3[2]

        self.layer3[2].down = self.layer2[2]
        self.layer3[2].up = self.layer4[2]
        self.layer3[2].left = self.layer3[1]
        self.layer3[2].right = self.layer3[3]

        self.layer3[3].down = self.layer2[3]
        self.layer3[3].up = self.layer4[3]
        self.layer3[3].left = self.layer3[2]
        self.layer3[3].right = self.layer3[0]

        #Conexiones Layer 4
        self.layer4[0].down = self.layer3[0]
        self.layer4[0].left = self.layer4[3]
        self.layer4[0].right = self.layer4[1]

        self.layer4[1].down = self.layer3[1]
        self.layer4[1].left = self.layer4[0]
        self.layer4[1].right = self.layer4[2]

        self.layer4[2].down = self.layer3[2]
        self.layer4[2].left = self.layer4[1]
        self.layer4[2].right = self.layer4[3]

        self.layer4[3].down = self.layer3[3]
        self.layer4[3].left = self.layer4[2]
        self.layer4[3].right = self.layer4[0]

    #sirve para los layers diferentes al 0
    def movLeft(self, layer):
        layer[0].temp = layer[1].color
        layer[1].temp = layer[2].color
        layer[2].temp = layer[3].color
        layer[3].temp = layer[0].color

        for i in range(len(layer)):
            layer[i].color = layer[i].temp
            layer[i].temp = -1

        return 

    #sirve para los layers diferentes al 0
    def movRight(self, layer):
        layer[0].temp = layer[3].color
        layer[1].temp = layer[0].color
        layer[2].temp = layer[1].color
        layer[3].temp = layer[2].color

        for i in range(len(layer)):
            layer[i].color = layer[i].temp
            layer[i].temp = -1

        return 
    
    def movUpVoid(self, layerDown, layerUp, colum):
        layerDown[colum-1].temp = layerUp[colum-1].color
        layerUp[colum-1].temp = layerDown[colum-1].color

        layerDown[colum-1].color = layerDown[colum-1].temp
        layerUp[colum-1].color = layerUp[colum-1].temp
        return

    def movDownVoid(self, layerDown, layerUp, colum):
        layerDown[colum-1].temp = layerDown[colum-1].color
        layerUp[colum-1].temp = layerUp[colum-1].color

        layerDown[colum-1].color = layerUp[colum-1].temp
        layerUp[colum-1].color = layerDown[colum-1].temp
        return

    def movLeftVoid(self, node):
        node.left.temp = node.color
        node.temp = node.left.color

        node.left.color = node.left.temp
        node.color = node.temp
        return

    def movRightVoid(self, node):
        node.right.temp = node.color
        node.temp = node.right.color

        node.right.color = node.right.temp
        node.color = node.temp
        return

    def resetZero(self):
        self.reader.resetMatrix()
        self.mr = self.reader.getMatrix()
        self.layer0 = [Nodo(self.mr[16])]
        self.layer1 = [Nodo(self.mr[12]),Nodo(self.mr[13]),Nodo(self.mr[14]),Nodo(self.mr[15])]
        self.layer2 = [Nodo(self.mr[8]),Nodo(self.mr[9]),Nodo(self.mr[10]),Nodo(self.mr[11])]
        self.layer3 = [Nodo(self.mr[4]),Nodo(self.mr[5]),Nodo(self.mr[6]),Nodo(self.mr[7])]
        self.layer4 = [Nodo(self.mr[0]),Nodo(self.mr[1]),Nodo(self.mr[2]),Nodo(self.mr[3])]

        return

    def saveMatrix(self):
        arrayMatrix = []
        arrayMatrix.append(self.getMatrixRow(self.layer4))
        arrayMatrix.append(self.getMatrixRow(self.layer3))
        arrayMatrix.append(self.getMatrixRow(self.layer2))
        arrayMatrix.append(self.getMatrixRow(self.layer1))
        arrayMatrix = np.array(arrayMatrix)
        arrayMatrix = arrayMatrix.reshape(1,16)[0]
        arrayMatrix = np.ndarray.tolist(arrayMatrix)
        arrayMatrix.append(self.layer0[0].color)
        self.reader.saveMatrix(arrayMatrix)
        
    def getMatrixRow(self, layer):
        arrayLayer = []
        for i in range(len(layer)):
            arrayLayer.append(layer[i].color)
        return arrayLayer
