"""Isso faz algo legal"""
def valor_pagamento(valor, dias_atraso):
    """Qualquer coisa"""
    if valor < 0:
        return None
    if dias_atraso > 0:
        multa = valor * 0.03
        adicional_atraso = valor * dias_atraso * 0.01
        return valor + multa + adicional_atraso
    return valor
