# Questão 14 - 
# Enunciado: Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

contadorpar = 0
contadorimpar = 0

for i in range(10):
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        contadorpar += 1
    else:
        contadorimpar += 1
        
print(f"Números pares: {contadorpar}")
print(f"Números ímpares: {contadorimpar}")