class Nodo:

    def __init__(self, head, color):
        self.head = head
        self.color = color #[rojo, azul, verde, amarillo] ; -1 = No hay color
        self.up = None
        self.down = None
        self.left = None
        self.right = None

    # def headGet(self):
    #     return self.head
    # def headSet(self,new):
    #     self.head = new
    #     return

    # def colorGet(self):
    #     return self.color
    # def colorSet(self,new):
    #     self.color = new
    #     return

    # def upGet(self):
    #     return self.up
    # def upSet(self,new):
    #     self.up = new
    #     return

    # def downGet(self):
    #     return self.down
    # def downSet(self,new):
    #     self.down = new
    #     return

    # def leftGet(self):
    #     return self.left
    # def leftSet(self,new):
    #     self.left = new
    #     return

    # def rightGet(self):
    #     return self.right
    # def rightSet(self,new):
    #     self.up = right
    #     return