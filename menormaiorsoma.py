# Questão 18 - Determinar o maior e o menor número e depois somar. 
#Enunciado: Faça um programa que, dado um conjunto de N números,
# determine o menor valor, o maior valor e a soma dos valores.

maior = None
menor = None

soma = 0

while True:
    num = int(input("Digite um número (0 para sair): "))
    soma += num

    if maior == None:
        maior = num
        
    if num > maior:
        maior = num
        
    if menor == None:
        menor = num
        
    if num > menor:
        menor = num
        

    if num == 0:
        break

print(f"""
        Maior: {maior}
        Menor: {menor}
        Soma: {soma}
    """)


