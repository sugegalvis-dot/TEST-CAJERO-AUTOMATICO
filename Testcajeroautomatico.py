
saldo = 1000



def mostrar_menu():
    print ("\n=== CAJERO AUTOMATICO===\n")
    print ("===MENÚ===")
    print ("1. Consultar saldo")
    print ("2. Depositar dinero")
    print ("3. Retirar dinero")
    print ("0. Salir")

def consultar_saldo():
    print ("Su saldo actual es: ", "$", saldo)

def deposita_r (monto):
    global saldo 
    if monto > 0:
        saldo = saldo + monto
        print ("Deposito aceptado. El nuevo saldo es: ", "$", saldo)
    else: 
        print ("Error: el monto a depositar debe ser mayor que 0")

def retirar (monto):
    global saldo 
    if monto <= 0:
        print ("Error: El monto a retirar debe ser mayor que cero")
    elif monto > saldo:
        print ("Error: Monto no permitido. Fondos insuficientes")
    else: 
        saldo = (saldo - monto)
        print ("Retiro exitoso. El nuevo saldo es: ", "$", saldo)

opcion = -1
while opcion != 0:
    mostrar_menu()
    opcion = int(input("Elija una opción (digite numero): "))
    if opcion == 1:
        consultar_saldo()
    elif opcion == 2:
        monto = float(input("Monto a depositar: $"))
        deposita_r(monto)
    elif opcion == 3:
        monto = float(input("Monto a retirar: $")) 
        retirar(monto)
    elif opcion == 0:
        print ("Sesión finalizada. Gracias por usar el cajero")
    else:
        print ("Opción invalida. Intente de nuevo.")




    