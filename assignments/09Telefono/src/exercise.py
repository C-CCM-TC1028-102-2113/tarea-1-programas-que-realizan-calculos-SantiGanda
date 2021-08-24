def main():
    #escribe tu código abajo de esta línea
    #Leer los datos
    print("Dame el número de mensajes")
mnsj=int(input())
print("Dame el número de megas")
megas=float(input())
print("Dame el número de minutos")
minutos=int(input())
cost=(mnsj*.80)+(megas*.80)+(minutos*.80)
print("El costo mensual es de: "+str(cost))

    pass


if __name__ == '__main__':
    main()
