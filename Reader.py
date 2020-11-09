import csv

class MatrixReader:
    def __init__(self, path):
        self.path = path
        self.m = []
        self.leerMat()
    
    
    def leerMat(self):
        data_array = []
        with open(self.path, newline='') as myFile:
            reader = csv.reader(myFile)
            for row in reader:
                result = row[0].split(";")
                data = result[0]
                data_array.append(data)
        data_array = data_array[0:]

        #Converts data to int
        for row in data_array:
            self.m.append(int(row))

    def getMatrix(self):
        return self.m
