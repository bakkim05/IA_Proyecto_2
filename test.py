from Reader import MatrixReader

if __name__ == "__main__":
    reader = MatrixReader("matriz.csv")
    a = reader.getMatrix()
    print(a)