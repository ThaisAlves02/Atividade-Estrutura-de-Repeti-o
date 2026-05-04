# Questão 7 - Informar o maior número.
# Enunciado: Faça um programa que leia 5 números e informe o maior número.

maior = None

for i in range(5):
    num = int(input("Digite um número: "))

    if maior == None:
        maior = num
    
    if num > maior:
        maior = num


print("O maior número é: ",maior)       