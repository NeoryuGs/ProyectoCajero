import pytest
from cajerotest import Cajero

@pytest.fixture
def cajero():
    return Cajero()

@pytest.mark.parametrize("expected_saldo", [85200])
def test_consultar_saldo(cajero, expected_saldo):
    assert cajero.consultar_saldo() == expected_saldo

@pytest.mark.parametrize("deposit, expected_saldo", [
    (1000, 86200), (2000, 87200), (500, 85700), (1500, 86700), (2500, 87700),
    (3000, 88200), (3500, 88700), (4000, 89200), (4500, 89700), (5000, 90200),
    (6000, 91200), (7000, 92200), (8000, 93200), (9000, 94200), (10000, 95200),
])
def test_depositar_dinero(cajero, deposit, expected_saldo):
    cajero.depositar_dinero(deposit)
    assert cajero.consultar_saldo() == expected_saldo

@pytest.mark.parametrize("withdraw, expected_saldo", [
    (5000, 80200), (1000, 84200), (200, 85000), (3000, 82200), (4000, 81200),
    (1500, 83700), (2500, 82700), (3500, 81700), (4500, 80700), (500, 84700),
    (6000, 79200), (7000, 78200), (8000, 77200), (9000, 76200), (10000, 75200),
])
def test_extraer_dinero(cajero, withdraw, expected_saldo):
    cajero.extraer_dinero(withdraw)
    assert cajero.consultar_saldo() == expected_saldo

@pytest.mark.parametrize("withdraw", [
    16000, 20000, 17000, 18000, 19000, 21000, 22000, 23000, 24000, 25000,
    26000, 27000, 28000, 29000, 30000,
])
def test_extraer_dinero_excede_disponible(cajero, withdraw):
    with pytest.raises(ValueError):
        cajero.extraer_dinero(withdraw)

@pytest.mark.parametrize("transfer, expected_saldo", [
    (1000, 84200), (2000, 83200), (500, 84700), (1500, 83700), (2500, 82700),
    (3000, 82200), (3500, 81700), (4000, 81200), (4500, 80700), (5000, 80200),
    (6000, 79200), (7000, 78200), (8000, 77200), (9000, 76200), (10000, 75200),
])
def test_transferir_dinero(cajero, transfer, expected_saldo):
    cajero.transferir_dinero(transfer)
    assert cajero.consultar_saldo() == expected_saldo

@pytest.mark.parametrize("transfer", [
    86000, 90000, 87000, 88000, 89000, 91000, 92000, 93000, 94000, 95000,
    96000, 97000, 98000, 99000, 100000,
])
def test_transferir_dinero_excede_saldo(cajero, transfer):
    with pytest.raises(ValueError):
        cajero.transferir_dinero(transfer)

@pytest.mark.parametrize("monto_dolares, expected_saldo, expected_saldo_dolar", [
    (100, 84830, 100), (200, 84460, 200), (300, 84090, 300), (400, 83720, 400), (500, 83350, 500),
    (600, 82980, 600), (700, 82610, 700), (800, 82240, 800), (900, 81870, 900), (1000, 81500, 1000),
    (1100, 81130, 1100), (1200, 80760, 1200), (1300, 80390, 1300), (1400, 80020, 1400), (1500, 79650, 1500),
])
def test_comprar_dolares(cajero, monto_dolares, expected_saldo, expected_saldo_dolar):
    saldo, saldo_dolar = cajero.comprar_dolares(monto_dolares)
    assert saldo == expected_saldo
    assert saldo_dolar == expected_saldo_dolar

@pytest.mark.parametrize("monto_dolares", [
    30000, 40000, 31000, 32000, 33000, 34000, 35000, 36000, 37000, 38000,
    39000, 41000, 42000, 43000, 44000,
])
def test_comprar_dolares_excede_saldo(cajero, monto_dolares):
    with pytest.raises(ValueError):
        cajero.comprar_dolares(monto_dolares)

@pytest.mark.parametrize("monto_dolares, initial_saldo_dolar, expected_saldo, expected_saldo_dolar", [
    (50, 100, 85385, 50), (20, 50, 85274, 30), (30, 40, 85311, 10), (10, 20, 85237, 10), (5, 15, 85218.5, 10),
    (60, 120, 85422, 60), (70, 140, 85459, 70), (80, 160, 85496, 80), (90, 180, 85533, 90), (100, 200, 85570, 100),
    (110, 220, 85607, 110), (120, 240, 85644, 120), (130, 260, 85681, 130), (140, 280, 85718, 140), (150, 300, 85755, 150),
])
def test_vender_dolares(cajero, monto_dolares, initial_saldo_dolar, expected_saldo, expected_saldo_dolar):
    cajero.saldoDolar = initial_saldo_dolar
    saldo, saldo_dolar = cajero.vender_dolares(monto_dolares)
    assert saldo == expected_saldo
    assert saldo_dolar == expected_saldo_dolar

@pytest.mark.parametrize("monto_dolares, initial_saldo_dolar", [
    (50, 30), (100, 80), (110, 90), (120, 100), (130, 110),
    (140, 120), (150, 130), (160, 140), (170, 150), (180, 160),
    (190, 170), (200, 180), (210, 190), (220, 200), (230, 210),
])
def test_vender_dolares_excede_saldo_dolar(cajero, monto_dolares, initial_saldo_dolar):
    cajero.saldoDolar = initial_saldo_dolar
    with pytest.raises(ValueError):
        cajero.vender_dolares(monto_dolares)


@pytest.mark.parametrize("monto, dias, expected_saldo, expected_interes", [
    (10000, 30, 75200, 616.4383561643836), (20000, 60, 65200, 2465.753424657534), (5000, 15, 80200, 154.10958904109611),
    (15000, 45, 70200, 1386.9863013698632), (25000, 75, 60200, 3852.7397260273974), (30000, 90, 55200, 5547.945205479453),
    (35000, 120, 50200, 8630.136986301375), (40000, 150, 45200,12328.767123287675), (45000, 180, 40200, 16643.83561643835),
    (50000, 210, 35200, 21575.34246575342), (55000, 240, 30200,27123.287671232873), (60000, 270, 25200, 33287.67123287672),
    (65000, 300, 20200, 40068.49315068494), (70000, 330, 15200, 47465.75342465752), (75000, 360, 10200, 55479.452054794514),
])
def test_crear_plazo_fijo(cajero, monto, dias, expected_saldo, expected_interes):
    initial_saldo = cajero.consultar_saldo()
    saldo, interes_ganado = cajero.crear_plazo_fijo(monto, dias)
    assert saldo == expected_saldo
    assert pytest.approx(interes_ganado, 0.01) == expected_interes
    cajero.saldo=initial_saldo

@pytest.mark.parametrize("monto, dias", [
    (90000, 30), (100000, 60), (110000, 90), (120000, 120), (130000, 150),
    (140000, 180), (150000, 210), (160000, 240), (170000, 270), (180000, 300),
    (190000, 330), (200000, 360), (210000, 390), (220000, 420), (230000, 450),
])
def test_crear_plazo_fijo_excede_saldo(cajero, monto, dias):
    with pytest.raises(ValueError):
        cajero.crear_plazo_fijo(monto, dias)
