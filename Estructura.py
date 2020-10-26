from Nodo import Nodo

class Estructura:
    def __init__(self):
        #inicializar 
        self.layer0 = [Nodo(True,-1)]
        self.layer1 = [Nodo(False,0),Nodo(False,1),Nodo(False,2),Nodo(False,3)]
        self.layer2 = [Nodo(False,0),Nodo(False,1),Nodo(False,2),Nodo(False,3)]
        self.layer3 = [Nodo(False,0),Nodo(False,1),Nodo(False,2),Nodo(False,3)]
        self.layer4 = [Nodo(False,0),Nodo(False,1),Nodo(False,2),Nodo(False,3)]

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