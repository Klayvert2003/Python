"""
Formas de fazer:

if km >= (LOCAL_1 - RADAR_RANGE) and km <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1:
    print('Foi multado no radar 1')
else:
    print('Não passou da velocidade!')

OU
"""


velocidade = 61
km = 99

RADAR_1 = 61
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_acima_radar = velocidade > RADAR_1

carro_multado = km >= (LOCAL_1 - RADAR_RANGE) and km <= (LOCAL_1 + RADAR_RANGE)

if carro_multado and velocidade_acima_radar:
    print('Foi multado no radar 1')
else:
    print('Não passou da velocidade!')