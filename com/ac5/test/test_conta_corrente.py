from com.ac5.conta_corrente import Conta_Corrente

def test_dep():
    conta = Conta_Corrente(10, 'Erick')
    conta.deposito(10)
    assert conta.saldo == 10

def test_saque():
    conta = Conta_Corrente(20, 'Thiago', 5)
    conta.saque(5)
    assert conta.saldo == 0

