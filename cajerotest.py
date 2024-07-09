class Cajero:
    def __init__(self, saldo=85200, disponible=15000, saldoDolar=0, tasaCambio=3.70):
        self.saldo = saldo
        self.disponible = disponible
        self.saldoDolar = saldoDolar
        self.tasaCambio = tasaCambio

    def consultar_saldo(self):
        return self.saldo

    def depositar_dinero(self, monto):
        self.saldo += monto
        return self.saldo

    def extraer_dinero(self, monto):
        if monto <= self.disponible:
            self.saldo -= monto
            self.disponible -= monto  # Actualizar disponible también
            return self.saldo
        else:
            raise ValueError("Monto excede el saldo disponible")

    def transferir_dinero(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            return self.saldo
        else:
            raise ValueError("Monto excede el saldo disponible")

    def comprar_dolares(self, monto_dolares):
        conversion = monto_dolares * self.tasaCambio
        if conversion <= self.saldo:
            self.saldo -= conversion
            self.saldoDolar += monto_dolares
            return self.saldo, self.saldoDolar
        else:
            raise ValueError("Monto excede el saldo disponible")

    def vender_dolares(self, monto_dolares):
        conversion = monto_dolares * self.tasaCambio
        if monto_dolares <= self.saldoDolar:
            self.saldo += conversion
            self.saldoDolar -= monto_dolares
            return self.saldo, self.saldoDolar
        else:
            raise ValueError("Monto excede el saldo de dólares disponible")

    def crear_plazo_fijo(self, monto, dias):
        tasaInt = 0.75
        nDias = dias / 365
        simulador = monto * (1 + (tasaInt * nDias))
        interes_ganado = simulador - monto
        if monto <= self.saldo:
            self.saldo -= monto
            return self.saldo, interes_ganado
        else:
            raise ValueError("Monto excede el saldo disponible")
