def main():
    #escribe tu código abajo de esta línea
    print("Dame un número de cuatro dígitos")
num=(input())

if int(num[0])%2 == 0:
    par1=int(1)
else:
    par1=int(0)
if int(num[1])%2 == 0:
    par2=int(1)
else:
    par2=int(0)
if int(num[2])%2 == 0:
    par3=int(1)
else:
    par3=int(0)
if int(num[3])%2 == 0:
    par4=int(1)
else:
    par4=int(0)

pares=par1+par2+par3+par4

print("La cantidad de dígitos pares es: "+str(pares))

    pass


if __name__ == '__main__':
    main()
