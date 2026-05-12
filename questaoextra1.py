# Questão - 19

maior = None
menor = None

soma = 0

while True:
    num = int(input("Digite um número (-2 para sair): "))
    
    if num == -2:
        break
    
    if num >= 0 and num <= 1000:
        soma += num
    else:
        print("Escreva um número entre zero e mil!")
        continue
        
    if maior == None:
        maior = num
    
    if num > maior:
        maior = num
    
    if menor == None:
        menor = num
    
    if num < menor:
        menor = num


print(f"""
        Maior: {maior}
        Menor: {menor}
        Soma: {soma}
    """)