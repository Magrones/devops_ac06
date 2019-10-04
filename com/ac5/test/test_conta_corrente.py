from com.ac5.conta_corrente import conta_corrente

def test_dep():
    '''Esta função faz deposito'''
    conta = conta_corrente(10, 'Erick')
    conta.deposito(10)
    assert conta.saldo == 10

def test_saque():
    '''Esta função faz saque'''
    conta = conta_corrente(20, 'Thiago', 5)
    conta.saque(5)
    assert conta.saldo == 0
