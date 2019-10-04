from com.ac5.calcula_parcela import valor_pagamento
"""Calcula"""
def test_valorcerto():
    assert valor_pagamento(8, 5) == 8.64, "Deveria ser 8.64"
    """Calcula"""


def test_valormenor():
    assert valor_pagamento(-2, 5) == , "Deveria ser None"
    """Calcula"""


def test_diazero():
    assert valor_pagamento(10, 0) == 10, "Deveria ser 5"
    """Calcula"""
