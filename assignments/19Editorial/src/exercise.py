def main():
    #escribe tu código abajo de esta línea
    import math
print("Dame el número de palabras")
paginas=math.ceil(int(input())/475)
costo1=paginas*60
costo2=costo1*.10
costo3=costo1-costo2

print("El costo de la publicación es de: "+str(costo3))


    pass


if __name__ == '__main__':
    main()
