import pytest
from cajerotest import Cajero

@pytest.fixture
def cajero():
    return Cajero()

def test_consultar_saldo(cajero):
    assert cajero.consultar_saldo() == 85200

def test_depositar_dinero(cajero):
    cajero.depositar_dinero(1000)
    assert cajero.consultar_saldo() == 86200

def test_extraer_dinero(cajero):
    cajero.extraer_dinero(5000)
    assert cajero.consultar_saldo() == 80200

def test_extraer_dinero_excede_disponible(cajero):
    with pytest.raises(ValueError):
        cajero.extraer_dinero(16000)

def test_transferir_dinero(cajero):
    cajero.transferir_dinero(1000)
    assert cajero.consultar_saldo() == 84200

def test_transferir_dinero_excede_saldo(cajero):
    with pytest.raises(ValueError):
        cajero.transferir_dinero(86000)

def test_comprar_dolares_correcto(cajero):
    saldo, saldo_dolar = cajero.comprar_dolares(100)
    assert saldo == pytest.approx(84830, rel=1e-2)  # Utiliza aproximación con una tolerancia pequeña
    assert saldo_dolar == 100

def test_vender_dolares(cajero):
    cajero.saldoDolar = 100
    saldo, saldo_dolar = cajero.vender_dolares(50)
    assert saldo == 85385
    assert saldo_dolar == 50

def test_vender_dolares_excede_saldo_dolar(cajero):
    cajero.saldoDolar = 50  # Ajusta el saldo de dólares para que sea exactamente 50
    with pytest.raises(ValueError):
        cajero.vender_dolares(100)  # Intenta vender más de lo que tienes, debería levantar ValueError

def test_crear_plazo_fijo(cajero):
    saldo, interes_ganado = cajero.crear_plazo_fijo(10000, 30)
    assert saldo == 75200
    assert interes_ganado > 0

def test_crear_plazo_fijo_excede_saldo(cajero):
    with pytest.raises(ValueError):
        cajero.crear_plazo_fijo(90000, 30)
