def main():
    #escribe tu código abajo de esta línea
    print("Dame el saldo del mes anterior")
anterior=float(input())
print("Dame los ingresos")
ingresos=float(input())
print("Dame los egresos")
egresos=float(input())
print("Dame la cantidad de cheques expedidos")
cheques=float(input())*13

saldo1=anterior+ingresos-(egresos+cheques)
saldo2=saldo1*.075
saldo3=saldo1-saldo2

print("El saldo final de la cuenta es de: "+str(saldo3))

    pass

if __name__ == '__main__':
    main()
