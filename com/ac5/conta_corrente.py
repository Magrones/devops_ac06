'''Este arquivo tem funções de conta corrente'''
class conta_corrente:

    def __init__(self, numero, nome_correntista, saldo=0.0):
        '''Conta corrente'''
        self.numero = numero
        self.alterar_nome(nome_correntista)
        self.saldo = saldo

    def alterar_nome(self, nome_correntista):
        '''correntista'''
        self.nome_correntista = nome_correntista

    def deposito(self, valor):
        '''deposito'''
        self.saldo += valor

    def saque(self, valor):
        '''saque'''
        self.saldo -= valor
