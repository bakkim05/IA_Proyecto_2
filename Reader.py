

class MatrixReader:
    def __init__(self, path):
        self.path = path
        self.m = []
        self.leerMat()

    def leerMat(self):
        read = open(self.path,"r")
        lines = read.readlines()
        for line in lines:
            self.m.append(int(line.strip("\n")))

    def getMatrix(self):
        return self.m


    def saveMatrix(self, arrayMatrix):
        write = open(self.path, "w")
        for i in range(len(arrayMatrix)):
            arrayMatrix[i] = str(arrayMatrix[i])+"\n"
        write.writelines(arrayMatrix)

