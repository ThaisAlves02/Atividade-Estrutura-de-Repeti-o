# Questão 8 - Informar a soma e a média dos números.
#Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
for i in range(5):
    num = int(input(f"Digite um número {i+1}: "))
    soma += num
    
media = soma/5

print("O resultado da soma é: ",soma)
print("A média é: ",media)