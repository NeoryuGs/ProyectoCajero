###########################################################################
# Simular cajero
###########################################################################

def cajero():
    print("Hola Bienvenido al cajero de codo a codo")
    print("ingresa tu clave para acceder a tu cuenta \n la clave es 1234 ")
    clave = int(input("ingresa tu clave: "))
    nombre = str(input("ingresa tu nombre: "))
    saldo = float(85200)  # Saldo en soles
    disponible = float(15000)  # Saldo disponible para extracción
    saldoDolar = float(0)  # Saldo en dólares
    tasaCambio = 3.70  # Tasa de cambio actual en soles

    if clave == 1234:
        print("#########################################")
        print("Bienvenido a tu cuenta", nombre, "!!")
        print("#########################################")
        print("selecciona una opcion y presiona lo siguiente: ")
        print("#########################################")
        print("     #1  consultar saldo")
        print("     #2  depositar dinero")
        print("     #3  extraer dinero")
        print("     #4  transferir dinero")
        print("     #5  comprar dolares")
        print("     #6  vender dolares")
        print("     #7  crear plazo fijo")
        print("     #8  ver ultimos movimientos")
        print("     #9  salir de la cuenta")
        print("#########################################")
        opcion = int(input("ingresa tu opcion: "))
        
        # 1consultar saldo
        if opcion == 1:
            print("tu saldo actual en soles es de: S/.", saldo)
        
        # 2depositar dinero
        elif opcion == 2:
            print("#########################################")
            ingreso = int(input("digite por teclado el monto de su dinero a ingresar y luego inserte su dinero: "))
            print("#########################################")
            saldoActual = saldo + ingreso
            print("--Gracias por ingresar su dinero, su saldo actual es de: S/.", saldoActual, "--")
        
        # 3extraer dinero
        elif opcion == 3:
            extraccion = int(input("ingresa el monto a extraer: "))
            saldoActual = saldo - extraccion
            print("gracias por extraer, tu saldo restante es: S/.", saldoActual)
        
        # 4transferir dinero
        elif opcion == 4:
            tranferir = int(input("ingrese el cbu de la cuenta a la cual deseas tranferir: "))
            monto = int(input("ingresa el monto a tranferir: "))
            print("#########################################################")
            print("Estas por realizar una transferencia al numero de cuenta ", tranferir, "con el siguiente monto: S/.", monto, "estas seguro que deseas realizar esta accion ?")
            print("#########################################################")
            saldoActual = saldo - monto
            confirmar = str(input("ingresa: \n     # si para confirmar la transferencia. \n     # no para cancelar: \n "))
            if confirmar == "si":
                print("gracias tu tranferencia ha sido realizada!, tu saldo actual es de: S/.", saldoActual)
            elif confirmar == "no":
                print("has cancelado tu transferencia")
            else:
                print("has ingresado un valor invalido")
        
        # 5comprar dolares
        elif opcion == 5:
            print("#####################################")
            print("    el precio del dolar es de S/.", tasaCambio)
            print("    tu saldo es el siguiente: S/.", saldo)
            print("#####################################")
            compraDolar = float(input("ingresa el monto de dolares a comprar: "))
            print("#####################################")
            print("estas seguro de comprar : US$", compraDolar, " dolares ?")
            confirma = str(input("ingresa \n     #si para confirmar. \n     #no para cancelar "))
            print("#####################################")
            if confirma == "si":
                conversion = compraDolar * tasaCambio
                saldoActual = saldo - conversion
                saldoDolar = saldoDolar + compraDolar
                print("#####################################################")
                print("tu saldo en tu cuenta soles es de: S/.", saldoActual)
                print("tu saldo en tu cuenta dolares es de: US$", saldoDolar)
                print("#####################################################")
            elif confirma == "no":
                print("has cancelado tu compra")
        
        # 6vender dolares
        elif opcion == 6:
            print("#####################################")
            print("    el precio del dolar es de S/.", tasaCambio)
            print("    tu saldo es el siguiente: S/.", saldo)
            print("#####################################")
            venderDolar = float(input("ingresa el monto de dolares a vender: "))
            print("#####################################")
            print("estas seguro de vender : US$", venderDolar, " dolares ?")
            confirma = str(input("ingresa \n     #si para confirmar. \n     #no para cancelar "))
            print("#####################################")
            if confirma == "si":
                conversion = venderDolar * tasaCambio
                saldoActual = saldo + conversion
                saldoDolar = saldoDolar - venderDolar
                print("#####################################################")
                print("tu saldo en tu cuenta soles es de: S/.", saldoActual)
                print("tu saldo en tu cuenta dolares es de: US$", saldoDolar)
                print("#####################################################")
            elif confirma == "no":
                print("has cancelado tu venta")

        # 7crear plazo fijo
        elif opcion == 7:
            print("#####################################")
            print("    Tasa Nominal Anual (TNA) es de 75,00%")
            print("    la Tasa Efectiva Anual (TEA) es de 107,05%")
            print("    tu saldo es el siguiente: S/.", saldo)
            print("#####################################")
            plazoFijoMonto = float(input("ingresa el capital a invertir: "))
            print("#####################################")
            plazoFijoDias = float(input("ingresa el plazo en dias: "))
            print("#####################################")
            print("quiere que simulemos su plazo fijo en soles por", plazoFijoMonto, " soles a ?", plazoFijoDias, " dias?")
            confirma = str(input("ingresa \n     #si para confirmar. \n     #no para cancelar "))
            print("#####################################")
            if confirma == "si":
                tasaInt = (75/100)
                nDias = plazoFijoDias/365
                simulador = plazoFijoMonto * (1+(tasaInt*nDias))
                saldoActual = saldo - plazoFijoMonto
                intGanados = (plazoFijoMonto - simulador) * -1
                print("#####################################################")
                print("tu saldo en tu cuenta soles es de: S/.", saldoActual)
                print("tu capital invertido es de: S/.", plazoFijoMonto)
                print("tu interes ganado va a ser de : S/.", intGanados)
                print("tu saldo en tu cuenta dolares es de: US$", saldoDolar)
                print("#####################################################")
            elif confirma == "no":
                print("has cancelado tu inversion")
        
        # 8ver ultimos movimientos
        elif opcion == 8:
            from os import system
            system("cls")
            listaMovimientos = ['Saldo actual: 85,200 Soles ', 'Disponible para extraccion: 15,000 Soles', 'Saldo de dolares: 0,00', 'No tiene movimientos registrados']
            contenido = open("D:\Documentos\VisualCode\Python\operacionescajero.txt", "w")
            for movimiento in listaMovimientos:
                contenido.write(movimiento + "\n")
            contenido.close()
            print('Ahora lo abrimos!')
            contenido = open("D:\Documentos\VisualCode\Python\operacionescajero.txt", "r")
            contador = 1
            for linea in contenido:
                print("Linea", contador, ":", linea)
                contador = contador + 1
        
        # 9salir de la cuenta
        elif opcion == 9:
            print("#####################################")
            print("    Has cancelado la transacción...")
            print("    Muchas gracias por usar nuestro cajero")
            print("    Que tenga un buen dia!!!")
            print("#####################################")

    else:
        print("clave incorrecta")

cajero()
