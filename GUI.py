from tkinter import Tk, Label
from Estructura import Estructura

class GUI:
    def __init__(self,master):
        self.master = master
        master.title("Proyecto 2")
        master.geometry("800x600")

        #Tamaño de los LABELS
        self.width = 14
        self.height = 7

        #Inicialización de la estructura del juego (OBJETO Estructura)
        self.estructura = Estructura()
        
        #Inicializar los LABELS para la visualización de las posiciones del juego
        self.layer0pos0 = Label(master, borderwidth = 2, relief="ridge", background = "white", width=self.width, height=self.height)

        self.layer1pos0 = Label(master, borderwidth = 2, relief="ridge", background = "white", width=self.width, height=self.height)
        self.layer1pos1 = Label(master, borderwidth = 2, relief="ridge", background = "white", width=self.width, height=self.height)
        self.layer1pos2 = Label(master, borderwidth = 2, relief="ridge", background = "white", width=self.width, height=self.height)
        self.layer1pos3 = Label(master, borderwidth = 2, relief="ridge", background = "white", width=self.width, height=self.height)

        self.layer2pos0 = Label(master, borderwidth = 2, relief="ridge", background = "white", width=self.width, height=self.height)
        self.layer2pos1 = Label(master, borderwidth = 2, relief="ridge", background = "white", width=self.width, height=self.height)
        self.layer2pos2 = Label(master, borderwidth = 2, relief="ridge", background = "white", width=self.width, height=self.height)
        self.layer2pos3 = Label(master, borderwidth = 2, relief="ridge", background = "white", width=self.width, height=self.height)

        self.layer3pos0 = Label(master, borderwidth = 2, relief="ridge", background = "white", width=self.width, height=self.height)
        self.layer3pos1 = Label(master, borderwidth = 2, relief="ridge", background = "white", width=self.width, height=self.height)
        self.layer3pos2 = Label(master, borderwidth = 2, relief="ridge", background = "white", width=self.width, height=self.height)
        self.layer3pos3 = Label(master, borderwidth = 2, relief="ridge", background = "white", width=self.width, height=self.height)

        self.layer4pos0 = Label(master, borderwidth = 2, relief="ridge", background = "white", width=self.width, height=self.height)
        self.layer4pos1 = Label(master, borderwidth = 2, relief="ridge", background = "white", width=self.width, height=self.height)
        self.layer4pos2 = Label(master, borderwidth = 2, relief="ridge", background = "white", width=self.width, height=self.height)
        self.layer4pos3 = Label(master, borderwidth = 2, relief="ridge", background = "white", width=self.width, height=self.height)

        #Acutaliza los colores de los LABELS acorde al OJBETO Estructura
        self.fijarColoresLayer0()
        self.fijarColoresLayer1()
        self.fijarColoresLayer2()
        self.fijarColoresLayer3()
        self.fijarColoresLayer4()

        #Desplegar LABELS
        self.layer0pos0.grid(row = 5, column = 0)

        self.layer1pos0.grid(row = 4, column = 0)
        self.layer1pos1.grid(row = 4, column = 1)
        self.layer1pos2.grid(row = 4, column = 2)
        self.layer1pos3.grid(row = 4, column = 3)

        self.layer2pos0.grid(row = 3, column = 0)
        self.layer2pos1.grid(row = 3, column = 1)
        self.layer2pos2.grid(row = 3, column = 2)
        self.layer2pos3.grid(row = 3, column = 3)

        self.layer3pos0.grid(row = 2, column = 0)
        self.layer3pos1.grid(row = 2, column = 1)
        self.layer3pos2.grid(row = 2, column = 2)
        self.layer3pos3.grid(row = 2, column = 3)

        self.layer4pos0.grid(row = 1, column = 0)
        self.layer4pos1.grid(row = 1, column = 1)
        self.layer4pos2.grid(row = 1, column = 2)
        self.layer4pos3.grid(row = 1, column = 3)


    def fijarColoresLayer0(self):
        self.layer0pos0["background"] = self.definirColor(self.estructura.layer0[0])
    
    def fijarColoresLayer1(self):
        self.layer1pos0["background"] = self.definirColor(self.estructura.layer1[0])
        self.layer1pos1["background"] = self.definirColor(self.estructura.layer1[1])
        self.layer1pos2["background"] = self.definirColor(self.estructura.layer1[2])
        self.layer1pos3["background"] = self.definirColor(self.estructura.layer1[3])

    def fijarColoresLayer2(self):
        self.layer2pos0["background"] = self.definirColor(self.estructura.layer2[0])
        self.layer2pos1["background"] = self.definirColor(self.estructura.layer2[1])
        self.layer2pos2["background"] = self.definirColor(self.estructura.layer2[2])
        self.layer2pos3["background"] = self.definirColor(self.estructura.layer2[3])

    def fijarColoresLayer3(self):
        self.layer3pos0["background"] = self.definirColor(self.estructura.layer3[0])
        self.layer3pos1["background"] = self.definirColor(self.estructura.layer3[1])
        self.layer3pos2["background"] = self.definirColor(self.estructura.layer3[2])
        self.layer3pos3["background"] = self.definirColor(self.estructura.layer3[3])

    def fijarColoresLayer4(self):
        self.layer4pos0["background"] = self.definirColor(self.estructura.layer4[0])
        self.layer4pos1["background"] = self.definirColor(self.estructura.layer4[1])
        self.layer4pos2["background"] = self.definirColor(self.estructura.layer4[2])
        self.layer4pos3["background"] = self.definirColor(self.estructura.layer4[3])

    def definirColor(self, nodo):

        if (nodo.color == 0):
            return "red3"
        elif (nodo.color == 1):
            return "blue2"
        elif (nodo.color == 2):
            return "green3"
        elif (nodo.color == 3):
            return "gold2"
        elif (nodo.color == -1):
            return "white"
        return

    def actualizarColores(self):
        self.fijarColoresLayer0()
        self.fijarColoresLayer1()
        self.fijarColoresLayer2()
        self.fijarColoresLayer3()
        self.fijarColoresLayer4()
        return