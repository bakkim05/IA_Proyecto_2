from Nodo import Nodo

class Estructura:
    def __init__(self):
        #inicializar 
        self.layer0 = [Nodo(-1)]
        self.layer1 = [Nodo(0),Nodo(1),Nodo(2),Nodo(3)]
        self.layer2 = [Nodo(0),Nodo(1),Nodo(2),Nodo(3)]
        self.layer3 = [Nodo(0),Nodo(1),Nodo(2),Nodo(3)]
        self.layer4 = [Nodo(0),Nodo(1),Nodo(2),Nodo(3)]

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
    def movLeft(self,layer):
        layer[0].temp = layer[1].color
        layer[1].temp = layer[2].color
        layer[2].temp = layer[3].color
        layer[3].temp = layer[0].color

        for i in range(len(layer)):
            layer[i].color = layer[i].temp
            layer[i].temp = -1

        return 

    #sirve para los layers diferentes al 0
    def movRight(self,layer):
        layer[0].temp = layer[3].color
        layer[1].temp = layer[0].color
        layer[2].temp = layer[1].color
        layer[3].temp = layer[2].color

        for i in range(len(layer)):
            layer[i].color = layer[i].temp
            layer[i].temp = -1

        return 
    
    def movUp(self,layer0,layer1,layer2,layer3,layer4):
        return

    def movDown(self,layer0,layer1,layer2,layer3,layer4):
        return