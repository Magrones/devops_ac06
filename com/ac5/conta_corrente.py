class Conta_Corrente:

    def __init__(self, numero, nome_Correntista, saldo=0.0):
        self.numero = numero
        self.alterar_Nome(nome_Correntista)
        self.saldo = saldo

    def alterarNome(self, nome_Correntista):
        self.nome_Correntista = nome_Correntista

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor
