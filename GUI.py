from tkinter import Tk, Label, Button
from Estructura import Estructura

docDir = 'matriz.csv'

class GUI:
    def __init__(self,master):
        self.master = master
        master.title("Proyecto 2")
        master.geometry("1000x600")

        #Tamaño de los LABELS
        self.width = 14
        self.height = 6

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

        #Botones de Movimientos IZQ y DER
        self.leftLayer1 = Button(master, text= "<", width=self.width, command = lambda: self.movLateral(0,1))
        self.rightLayer1 = Button(master, text= ">", width=self.width, command = lambda: self.movLateral(1,1))

        self.leftLayer2 = Button(master, text= "<", width=self.width, command = lambda: self.movLateral(0,2))
        self.rightLayer2 = Button(master, text= ">", width=self.width, command = lambda: self.movLateral(1,2))

        self.leftLayer3 = Button(master, text= "<", width=self.width, command = lambda: self.movLateral(0,3))
        self.rightLayer3 = Button(master, text= ">", width=self.width, command = lambda: self.movLateral(1,3))

        self.leftLayer4 = Button(master, text= "<", width=self.width, command = lambda: self.movLateral(0,4))
        self.rightLayer4 = Button(master, text= ">", width=self.width, command = lambda: self.movLateral(1,4))

        #Botones de Movimiento UP y DOWN
        self.up1 = Button(master, text= "^", width=self.width, command = lambda: self.movVertical(0,1))
        self.down1 = Button(master, text= "v", width=self.width, command = lambda: self.movVertical(1,1))

        self.up2 = Button(master, text= "^", width=self.width, command = lambda: self.movVertical(0,2))
        self.down2 = Button(master, text= "v", width=self.width, command = lambda: self.movVertical(1,2))

        self.up3 = Button(master, text= "^", width=self.width, command = lambda: self.movVertical(0,3))
        self.down3 = Button(master, text= "v", width=self.width, command = lambda: self.movVertical(1,3))

        self.up4 = Button(master, text= "^", width=self.width, command = lambda: self.movVertical(0,4))
        self.down4 = Button(master, text= "v", width=self.width, command = lambda: self.movVertical(1,4))


        #Botones Auxiliares
        self.resetButton = Button(master, text="RESET", width=self.width, command = lambda: self.reset())


        #Acutaliza los colores de los LABELS acorde al OJBETO Estructura
        self.fijarColoresLayer0()
        self.fijarColoresLayer1()
        self.fijarColoresLayer2()
        self.fijarColoresLayer3()
        self.fijarColoresLayer4()

        #Desplegar LABELS
        self.layer0pos0.grid(row = 6, column = 1)

        self.layer1pos0.grid(row = 5, column = 1)
        self.layer1pos1.grid(row = 5, column = 2)
        self.layer1pos2.grid(row = 5, column = 3)
        self.layer1pos3.grid(row = 5, column = 4)

        self.layer2pos0.grid(row = 4, column = 1)
        self.layer2pos1.grid(row = 4, column = 2)
        self.layer2pos2.grid(row = 4, column = 3)
        self.layer2pos3.grid(row = 4, column = 4)

        self.layer3pos0.grid(row = 3, column = 1)
        self.layer3pos1.grid(row = 3, column = 2)
        self.layer3pos2.grid(row = 3, column = 3)
        self.layer3pos3.grid(row = 3, column = 4)

        self.layer4pos0.grid(row = 2, column = 1)
        self.layer4pos1.grid(row = 2, column = 2)
        self.layer4pos2.grid(row = 2, column = 3)
        self.layer4pos3.grid(row = 2, column = 4)

        #Desplegar Botones IZQ y DER
        self.leftLayer1.grid(row = 5, column = 0)
        self.rightLayer1.grid(row = 5, column = 5)

        self.leftLayer2.grid(row = 4, column = 0)
        self.rightLayer2.grid(row = 4, column = 5)

        self.leftLayer3.grid(row = 3, column = 0)
        self.rightLayer3.grid(row = 3, column = 5)

        self.leftLayer4.grid(row = 2, column = 0)
        self.rightLayer4.grid(row = 2, column = 5)

        #Desplegar Botones UP y DOWN
        self.up1.grid(row=0, column = 1)
        self.down1.grid(row=7, column = 1)

        self.up2.grid(row=0, column = 2)
        self.down2.grid(row=7, column = 2)

        self.up3.grid(row=0, column = 3)
        self.down3.grid(row=7, column = 3)

        self.up4.grid(row=0, column = 4)
        self.down4.grid(row=7, column = 4)

        #Desplegar Botones Auxiliares
        self.resetButton.grid(row = 0, column = 6)


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

    def reset(self):
        self.estructura.resetZero()
        self.estructura.layer0[0].color = self.estructura.layer0[0].inicial
        
        for i in range(len(self.estructura.layer1)):
            self.estructura.layer1[i].color = self.estructura.layer1[i].inicial
            self.estructura.layer2[i].color = self.estructura.layer2[i].inicial
            self.estructura.layer3[i].color = self.estructura.layer3[i].inicial
            self.estructura.layer4[i].color = self.estructura.layer4[i].inicial

        self.actualizarColores()


    def movLateral(self, direccion, layer):
        if (direccion == 0):
            if layer == 1:
                self.estructura.movLeft(self.estructura.layer1)
                self.fijarColoresLayer1()
                return
            elif layer == 2:
                self.estructura.movLeft(self.estructura.layer2)
                self.fijarColoresLayer2()
                return
            elif layer == 3:
                self.estructura.movLeft(self.estructura.layer3)
                self.fijarColoresLayer3()
                return
            elif layer == 4:
                self.estructura.movLeft(self.estructura.layer4)
                self.fijarColoresLayer4()
                return
        elif (direccion == 1):
            if layer == 1:
                self.estructura.movRight(self.estructura.layer1)
                self.fijarColoresLayer1()
                return
            elif layer == 2:
                self.estructura.movRight(self.estructura.layer2)
                self.fijarColoresLayer2()
                return
            elif layer == 3:
                self.estructura.movRight(self.estructura.layer3)
                self.fijarColoresLayer3()
                return
            elif layer == 4:
                self.estructura.movRight(self.estructura.layer4)
                self.fijarColoresLayer4()
                return

    def movVertical(self, direccion, colum):
        if (direccion == 0):
            if colum == 1:
                if self.estructura.layer0[0].color == -1:
                    self.estructura.movUpVoid(self.estructura.layer0, self.estructura.layer1, colum)
                    self.fijarColoresLayer0()
                    self.fijarColoresLayer1()
                elif self.estructura.layer1[0].color == -1:
                    self.estructura.movUpVoid(self.estructura.layer1, self.estructura.layer2, colum)
                    self.fijarColoresLayer1()
                    self.fijarColoresLayer2()
                elif self.estructura.layer2[0].color == -1:
                    self.estructura.movUpVoid(self.estructura.layer2, self.estructura.layer3, colum)
                    self.fijarColoresLayer2()
                    self.fijarColoresLayer3()
                elif self.estructura.layer3[0].color == -1:
                    self.estructura.movUpVoid(self.estructura.layer3, self.estructura.layer4, colum)
                    self.fijarColoresLayer3()
                    self.fijarColoresLayer4()
                return
            elif colum == 2:
                if self.estructura.layer1[1].color == -1:
                    self.estructura.movUpVoid(self.estructura.layer1, self.estructura.layer2, colum)
                    self.fijarColoresLayer1()
                    self.fijarColoresLayer2()
                elif self.estructura.layer2[1].color == -1:
                    self.estructura.movUpVoid(self.estructura.layer2, self.estructura.layer3, colum)
                    self.fijarColoresLayer2()
                    self.fijarColoresLayer3()
                elif self.estructura.layer3[1].color == -1:
                    self.estructura.movUpVoid(self.estructura.layer3, self.estructura.layer4, colum)
                    self.fijarColoresLayer3()
                    self.fijarColoresLayer4()
                return
            elif colum == 3:
                if self.estructura.layer1[2].color == -1:
                    self.estructura.movUpVoid(self.estructura.layer1, self.estructura.layer2, colum)
                    self.fijarColoresLayer1()
                    self.fijarColoresLayer2()
                elif self.estructura.layer2[2].color == -1:
                    self.estructura.movUpVoid(self.estructura.layer2, self.estructura.layer3, colum)
                    self.fijarColoresLayer2()
                    self.fijarColoresLayer3()
                elif self.estructura.layer3[2].color == -1:
                    self.estructura.movUpVoid(self.estructura.layer3, self.estructura.layer4, colum)
                    self.fijarColoresLayer3()
                    self.fijarColoresLayer4()
                return
            elif colum == 4:
                if self.estructura.layer1[3].color == -1:
                    self.estructura.movUpVoid(self.estructura.layer1, self.estructura.layer2, colum)
                    self.fijarColoresLayer1()
                    self.fijarColoresLayer2()
                elif self.estructura.layer2[3].color == -1:
                    self.estructura.movUpVoid(self.estructura.layer2, self.estructura.layer3, colum)
                    self.fijarColoresLayer2()
                    self.fijarColoresLayer3()
                elif self.estructura.layer3[3].color == -1:
                    self.estructura.movUpVoid(self.estructura.layer3, self.estructura.layer4, colum)
                    self.fijarColoresLayer3()
                    self.fijarColoresLayer4()
                return

        elif (direccion == 1):
            if colum == 1:
                if self.estructura.layer1[0].color == -1:
                    self.estructura.movUpVoid(self.estructura.layer1, self.estructura.layer0, colum)
                    self.fijarColoresLayer1()
                    self.fijarColoresLayer0()
                elif self.estructura.layer2[0].color == -1:
                    self.estructura.movUpVoid(self.estructura.layer2, self.estructura.layer1, colum)
                    self.fijarColoresLayer2()
                    self.fijarColoresLayer1()
                elif self.estructura.layer3[0].color == -1:
                    self.estructura.movUpVoid(self.estructura.layer3, self.estructura.layer2, colum)
                    self.fijarColoresLayer3()
                    self.fijarColoresLayer2()
                elif self.estructura.layer4[0].color == -1:
                    self.estructura.movUpVoid(self.estructura.layer4, self.estructura.layer3, colum)
                    self.fijarColoresLayer4()
                    self.fijarColoresLayer3()
                return
            elif colum == 2:
                if self.estructura.layer2[1].color == -1:
                    self.estructura.movUpVoid(self.estructura.layer2, self.estructura.layer1, colum)
                    self.fijarColoresLayer2()
                    self.fijarColoresLayer1()
                elif self.estructura.layer3[1].color == -1:
                    self.estructura.movUpVoid(self.estructura.layer3, self.estructura.layer2, colum)
                    self.fijarColoresLayer3()
                    self.fijarColoresLayer2()
                elif self.estructura.layer4[1].color == -1:
                    self.estructura.movUpVoid(self.estructura.layer4, self.estructura.layer3, colum)
                    self.fijarColoresLayer4()
                    self.fijarColoresLayer3()
                return
            elif colum == 3:
                if self.estructura.layer2[2].color == -1:
                    self.estructura.movUpVoid(self.estructura.layer2, self.estructura.layer1, colum)
                    self.fijarColoresLayer2()
                    self.fijarColoresLayer1()
                elif self.estructura.layer3[2].color == -1:
                    self.estructura.movUpVoid(self.estructura.layer3, self.estructura.layer2, colum)
                    self.fijarColoresLayer3()
                    self.fijarColoresLayer2()
                elif self.estructura.layer4[2].color == -1:
                    self.estructura.movUpVoid(self.estructura.layer4, self.estructura.layer3, colum)
                    self.fijarColoresLayer4()
                    self.fijarColoresLayer3()
                return
            elif colum == 4:
                if self.estructura.layer2[3].color == -1:
                    self.estructura.movUpVoid(self.estructura.layer2, self.estructura.layer1, colum)
                    self.fijarColoresLayer2()
                    self.fijarColoresLayer1()
                elif self.estructura.layer3[3].color == -1:
                    self.estructura.movUpVoid(self.estructura.layer3, self.estructura.layer2, colum)
                    self.fijarColoresLayer3()
                    self.fijarColoresLayer2()
                elif self.estructura.layer4[3].color == -1:
                    self.estructura.movUpVoid(self.estructura.layer4, self.estructura.layer3, colum)
                    self.fijarColoresLayer4()
                    self.fijarColoresLayer3()
                return        