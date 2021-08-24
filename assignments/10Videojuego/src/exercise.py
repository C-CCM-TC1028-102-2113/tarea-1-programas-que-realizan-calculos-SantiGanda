def main():
    #escribe tu código abajo de esta línea
    print("Dame la cantidad de juegos nuevos")
nuevos=int(input())
print("Dame la cantidad de juegos usados")
usados=int(input())
total=(nuevos*1000)+(usados*350)
print("El total de la compra es de: "+str(total))

   pass



if __name__ == '__main__':
    main()
