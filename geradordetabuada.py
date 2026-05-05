# Questão 12 - Gerar uma tabuada com um número dado pelo usuário.
# Enunciado: Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

#Tabuada de 5:
#5 X 1 = 5
#5 X 2 = 10
#5 X 10 = 50

tabuada = ""
num = int(input("Digite qual é o número da tabuada desejada: "))

for i in range(1,11):
    
    if num < 0 or num > 10:
        print("ERRO! Digite um número entre 0 e 10.")
        break

    
    if num <= 10:
        print(f"Tabuada de {num}")
        calc = (num * i)
        tabuada = f"""{num} X {i} = {calc}"""
        print(tabuada)



