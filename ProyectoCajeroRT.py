import requests
import time
from datetime import datetime

usuarios = {
    "usuario1": {"clave": "1234", "nombre": "Usuario 1", "saldo": 85200.0, "saldo_dolar": 0.0},
    "usuario2": {"clave": "5678", "nombre": "Usuario 2", "saldo": 100000.0, "saldo_dolar": 0.0}
}

sesion_activa = False
usuario_actual = None

def cerrar_sesion():
    global sesion_activa, usuario_actual
    sesion_activa = False
    usuario_actual = None
    print("Sesión cerrada. Regresando al inicio de sesión.")

def cambiar_clave():
    global usuario_actual
    if usuario_actual:
        clave_actual = input("Ingrese su clave actual: ")
        if clave_actual == usuarios[usuario_actual]["clave"]:
            nueva_clave = input("Ingrese su nueva clave: ")
            confirmar_clave = input("Confirme su nueva clave: ")
            if nueva_clave == confirmar_clave:
                usuarios[usuario_actual]["clave"] = nueva_clave
                print("Clave cambiada exitosamente.")
            else:
                print("Las claves no coinciden. Inténtelo de nuevo.")
        else:
            print("Clave incorrecta. No se puede cambiar la clave.")
    else:
        print("Debe iniciar sesión para cambiar la clave.")

def iniciar_sesion():
    global sesion_activa, usuario_actual
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario in usuarios and usuarios[usuario]["clave"] == clave:
        sesion_activa = True
        usuario_actual = usuario
        print(f"Bienvenido, {usuarios[usuario]['nombre']}!")

        while sesion_activa:
            opcion = int(input("""
    #########################################
    # Seleccione una opción:
    # 1. Consultar saldo
    # 2. Depositar dinero
    # 3. Extraer dinero
    # 4. Transferir dinero
    # 5. Comprar dólares
    # 6. Vender dólares
    # 7. Crear plazo fijo
    # 8. Ver últimos movimientos
    # 9. Cambiar clave
    # 10. Cerrar sesión
    #########################################
    Ingrese su opción: """))

            if opcion == 1:
                consultar_saldo()

            elif opcion == 2:
                depositar_dinero()

            elif opcion == 3:
                extraer_dinero()

            elif opcion == 4:
                transferir()

            elif opcion == 5:
                comprar_dolares()

            elif opcion == 6:
                vender_dolares()

            elif opcion == 7:
                crear_plazo_fijo()

            elif opcion == 8:
                ver_ultimos_movimientos()

            elif opcion == 9:
                cambiar_clave()

            elif opcion == 10:
                cerrar_sesion()

            else:
                print("Opción no válida. Inténtelo de nuevo.")

    else:
        print("Usuario o clave incorrectos. Inténtelo de nuevo.")

def tiempo_sesion():
    global sesion_activa
    tiempo_inicio = time.time()

    while sesion_activa:
        tiempo_transcurrido = time.time() - tiempo_inicio
        if tiempo_transcurrido > 20:
            print("Tiempo de sesión agotado. Cerrando sesión automáticamente.")
            cerrar_sesion()
        time.sleep(1)

def consultar_saldo():
    global usuario_actual
    if usuario_actual:
        print(f"Su saldo actual en soles es: S/. {usuarios[usuario_actual]['saldo']}")
        print(f"Su saldo actual en dólares es: US$ {usuarios[usuario_actual]['saldo_dolar']}")
        registrar_operacion(f"Consulta de saldo - Saldo actual en soles: S/. {usuarios[usuario_actual]['saldo']}")

def depositar_dinero():
    global usuario_actual
    if usuario_actual:
        monto = float(input("Ingrese el monto a depositar en soles: "))
        usuarios[usuario_actual]['saldo'] += monto
        print(f"Depósito exitoso. Su nuevo saldo en soles es: S/. {usuarios[usuario_actual]['saldo']}")
        registrar_operacion(f"Depósito de dinero - Monto: S/. {monto}")

def extraer_dinero():
    global usuario_actual
    if usuario_actual:
        monto = float(input("Ingrese el monto a extraer en soles: "))
        if monto <= usuarios[usuario_actual]['saldo']:
            usuarios[usuario_actual]['saldo'] -= monto
            print(f"Extracción exitosa. Su nuevo saldo en soles es: S/. {usuarios[usuario_actual]['saldo']}")
            registrar_operacion(f"Extracción de dinero - Monto: S/. {monto}")
        else:
            print("Fondos insuficientes.")

def transferir():
    global usuario_actual
    if usuario_actual:
        usuario_destino = input("Ingrese el usuario destino: ")
        if usuario_destino in usuarios:
            monto = float(input("Ingrese el monto a transferir en soles: "))
            if monto <= usuarios[usuario_actual]['saldo']:
                usuarios[usuario_actual]['saldo'] -= monto
                usuarios[usuario_destino]['saldo'] += monto
                print(f"Transferencia exitosa. Saldo actual en soles de {usuario_actual}: S/. {usuarios[usuario_actual]['saldo']}")
                registrar_operacion(f"Transferencia de dinero - Monto: S/. {monto} a usuario destino: {usuario_destino}")
            else:
                print("Fondos insuficientes para realizar la transferencia.")
        else:
            print(f"Usuario destino {usuario_destino} no encontrado.")
    else:
        print("Debe iniciar sesión para realizar transferencias.")

def comprar_dolares():
    global usuario_actual
    if usuario_actual:
        tasa_cambio = obtener_tipo_cambio()
        print(f"La tasa de cambio actual es: S/. {tasa_cambio}")
        monto_soles = float(input("Ingrese el monto en soles a convertir a dólares: "))
        if monto_soles <= usuarios[usuario_actual]['saldo']:
            usuarios[usuario_actual]['saldo'] -= monto_soles
            monto_dolares = monto_soles / tasa_cambio
            usuarios[usuario_actual]['saldo_dolar'] += monto_dolares
            print(f"Compra de dólares exitosa. Saldo actual en soles: S/. {usuarios[usuario_actual]['saldo']}, en dólares: US$ {usuarios[usuario_actual]['saldo_dolar']}")
            registrar_operacion(f"Compra de dólares - Monto en soles: S/. {monto_soles}")
        else:
            print("Fondos insuficientes para realizar la compra de dólares.")
    else:
        print("Debe iniciar sesión para comprar dólares.")

def vender_dolares():
    global usuario_actual
    if usuario_actual:
        tasa_cambio = obtener_tipo_cambio()
        print(f"La tasa de cambio actual es: S/. {tasa_cambio}")
        monto_dolares = float(input("Ingrese el monto en dólares a convertir a soles: "))
        if monto_dolares <= usuarios[usuario_actual]['saldo_dolar']:
            usuarios[usuario_actual]['saldo_dolar'] -= monto_dolares
            monto_soles = monto_dolares * tasa_cambio
            usuarios[usuario_actual]['saldo'] += monto_soles
            print(f"Venta de dólares exitosa. Saldo actual en soles: S/. {usuarios[usuario_actual]['saldo']}, en dólares: US$ {usuarios[usuario_actual]['saldo_dolar']}")
            registrar_operacion(f"Venta de dólares - Monto en dólares: US$ {monto_dolares}")
        else:
            print("Fondos insuficientes de dólares para realizar la venta.")
    else:
        print("Debe iniciar sesión para vender dólares.")

def obtener_tipo_cambio():
    url = "https://api.exchangeratesapi.io/latest?base=USD"
    try:
        response = requests.get(url)
        data = response.json()
        return data['rates']['PEN']  # Cambiar a 'PEN' si es la moneda local correcta
    except requests.exceptions.RequestException as e:
        print("Error al obtener el tipo de cambio:", e)
        return None

def crear_plazo_fijo():
    global usuario_actual
    if usuario_actual:
        print("#####################################")
        print("    Tasa Nominal Anual (TNA) es de 75,00%")
        print("    la Tasa Efectiva Anual (TEA) es de 107,05%")
        print(f"    Tu saldo actual es de: S/. {usuarios[usuario_actual]['saldo']}")
        print("#####################################")
        plazo_fijo_monto = float(input("Ingrese el capital a invertir en plazo fijo: "))
        plazo_fijo_dias = float(input("Ingrese el plazo en días para el plazo fijo: "))
        if plazo_fijo_monto <= usuarios[usuario_actual]['saldo']:
            tasa_interes = 0.75
            n_dias = plazo_fijo_dias / 365
            interes_ganado = plazo_fijo_monto * tasa_interes * n_dias
            usuarios[usuario_actual]['saldo'] -= plazo_fijo_monto
            print(f"Inversión en plazo fijo exitosa.")
            print(f"Interés ganado: S/. {interes_ganado}")
            print(f"Nuevo saldo en soles: S/. {usuarios[usuario_actual]['saldo']}")
            registrar_operacion(f"Inversión en plazo fijo - Monto: S/. {plazo_fijo_monto}, Plazo: {plazo_fijo_dias} días")
        else:
            print("Operación de plazo fijo cancelada.")
    else:
        print("Debe iniciar sesión para crear un plazo fijo.")

def ver_ultimos_movimientos():
    global usuario_actual
    if usuario_actual:
        try:
            with open(f"{usuario_actual}_movimientos.txt", "r") as archivo:
                movimientos = archivo.readlines()
                if movimientos:
                    print("Últimos movimientos:")
                    for idx, movimiento in enumerate(movimientos, start=1):
                        print(f"{idx}. {movimiento.strip()}")
                else:
                    print("No hay movimientos registrados.")
        except FileNotFoundError:
            print("No hay movimientos registrados.")
    else:
        print("Debe iniciar sesión para ver los últimos movimientos.")

def registrar_operacion(operacion):
    global usuario_actual
    if usuario_actual:
        with open(f"{usuario_actual}_movimientos.txt", "a") as archivo:
            fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            archivo.write(f"{fecha_hora} - {operacion}\n")
    else:
        print("Debe iniciar sesión para registrar operaciones.")

def menu_principal():
    print("Bienvenido al cajero automático.")

    while True:
        opcion = input("""
    #########################################
    # Seleccione una opción:
    # 1. Iniciar sesión
    # 2. Salir
    #########################################
    Ingrese su opción: """)
        
        if opcion == '1':
            iniciar_sesion()
        elif opcion == '2':
            print("Gracias por utilizar nuestro cajero automático. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

menu_principal()
