import random

def gera_numeros():

    # numero que representa a soma que queremos
    numero_alvo = random.randint(10, 100)

    # par de numeros que somados são iguais ao número alvo
    num1 = random.randint(1, numero_alvo // 2)
    num2 = numero_alvo - num1
    
    # sorteia número intruso
    while True:
        intruso = random.randint(1, numero_alvo)
        if intruso != num1 and intruso != num2 and intruso != numero_alvo:
            break
    
    # embaralha os números
    numeros = [num1, num2, intruso]
    random.shuffle(numeros)
    
    return numero_alvo, numeros
