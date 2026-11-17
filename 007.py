#GERANDO LISTAS DE NUMEROS
import random # numeros aleatorios
numeros = [10, 67, 7, 4, 3, 2, 1, 5, 6, 8, 9]
random.shuffle(numeros)
sorteado = numeros [0]
numeros.remove(sorteado)

print(f'Número sorteado: {sorteado}')
print(f'Lista atualizada: {numeros}')


print('----------------------------------------------')

import random
numeros = []
while len (numeros) < 10:
    numero = random.randint(1, 100)
    if numero not in numeros:
        numeros.append(numero)
print(f'Numero sorteado: {sorteado}')