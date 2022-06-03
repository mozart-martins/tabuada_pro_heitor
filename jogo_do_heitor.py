import random

quantidade = 0
quantidade = int(input("Quantas continhas você quer fazer? "))

for q in range(quantidade):
    print(str(random.randint(1,10)))
    numero1 = random.randint(1,10)
    numero2 = random.randint(1,10)
    resposta = int(input(f"{numero1} x {numero2} = "))
    if resposta == (numero1 * numero2):
        print(f"Você ACERTOU! A respostas é {resposta}!!")
    else:
        print(f"Você ERROU! A respostas é {(numero1 * numero2)}!!")
