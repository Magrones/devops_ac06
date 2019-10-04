'''Este arquivo tem funções de conta corrente"
class conta_corrente:

    def __init__(self, numero, nome_correntista, saldo=0.0):
        '''
        Esta funçao define a conta
        '''
        self.numero = numero
        self.alterar_nome(nome_correntista)
        self.saldo = saldo

    def alterar_nome(self, nome_correntista):
        '''Esta funçao define o nome'''
        self.nome_correntista = nome_correntista

    def deposito(self, valor):
        '''Esta funçao define o deposito'''
        self.saldo += valor

    def saque(self, valor):
        '''Esta funçao define o saque'''
        self.saldo -= valor
