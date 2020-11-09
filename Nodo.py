class Nodo:

    def __init__(self,color):
        self.color = color #[rojo, azul, verde, amarillo] ; -1 = No hay color
        self.inicial = color
        self.temp = -1
        self.up = None
        self.down = None
        self.left = None
        self.right = None