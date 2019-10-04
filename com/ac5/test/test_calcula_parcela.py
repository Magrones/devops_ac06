from com.ac5.calcula_parcela import valor_pagamento

def test_valorcerto():
    assert valor_pagamento(8,5) == 8.64, "Deveria ser 8.64"


def test_valormenor():
    assert valor_pagamento(-2,5) == None, "Deveria ser None"


def test_diazero():
    assert valor_pagamento(10,0) == 10, "Deveria ser 5"
