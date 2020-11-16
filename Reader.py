

class MatrixReader:
    def __init__(self, path):
        self.path = path
        self.m = []
        self.leerMat()

    def leerMat(self):
        read = open(self.path,"r")
        lines = read.readlines()
        for line in lines:
            inputLine = line.strip("\n")
            try:
                inputLine = int(inputLine)
            except:
                print ("Una de las entradas no es un numero")
            
            self.m.append(inputLine)
        return

    def getMatrix(self):
        self.validator()
        return self.m


    def saveMatrix(self, arrayMatrix):
        write = open(self.path, "w")
        for i in range(len(arrayMatrix)):
            arrayMatrix[i] = str(arrayMatrix[i])+"\n"
        write.writelines(arrayMatrix)
        return

    def resetMatrix(self):
        self.m = [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,-1]
        return
    
    def validator(self):
        valn1 = 0
        val0 = 0
        val1 = 0
        val2 = 0
        val3 = 0
        valError = 0

        for i in range(len(self.m)):
            if (self.m[i] == -1):
                valn1 += 1
            elif (self.m[i] == 0):
                val0 += 1
            elif (self.m[i] == 1):
                val1 += 1
            elif (self.m[i] == 2):
                val2 += 1
            elif (self.m[i] == 3):
                val3 += 1
            else:
                valError += 1

        if valError > 0:
            print ("Los valores de la matriz deben estar entre [-1,3]")
            return
        if valn1 != 1:
            print ("revisar la cantidad de espacios blancos en la matriz (debe ser 1)")
            return
        if val0 != 4:
            print ("revisar la cantidad de espacios rojos en la matriz (debe ser 4)")
            return
        if val1 != 4:
            print ("revisar la cantidad de espacios azul en la matriz (debe ser 4)")
            return
        if val2 != 4:
            print ("revisar la cantidad de espacios verde en la matriz (debe ser 4)")
            return
        if val3 != 4:
            print ("revisar la cantidad de espacios amarillo en la matriz (debe ser 4)")
            return

        
            
        
