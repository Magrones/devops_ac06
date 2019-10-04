def cvhora(hora, minuto):
    if (hora > 23) or (hora < 0) or (minuto < 0) or (minuto > 59):
        return "Nenhum"
    if (hora < 12):
        if (hora == 0):
            hora = 12
        return ' % 02d : % 02d AM ' % (hora, minuto)
    if (hora > 12):
        hora -= 12
        return ' % 02d : % 02d PM ' % (hora, minuto)
