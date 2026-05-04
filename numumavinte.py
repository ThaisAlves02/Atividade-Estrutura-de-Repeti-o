# Questão 6 - Imprimir os números de 1 á 20.
# Enunciado: Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
# Depois modifique o programa para que ele mostre os números um ao lado do outro.

contador = 0
for i in range(1,21):
    contador += 1
    print(i, end=" ")

#OBS: usei o end = "" para imprimir os números um do lado do outro. 