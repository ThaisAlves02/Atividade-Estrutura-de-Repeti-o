# Questão 3 - Pedir e validar nome, idade, salario, sexo, estado civil.
# Enunciado: Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd'.

errostxt = ""
errosnum = ""

while True:
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))
    salario = float(input("Digite o seu salário: "))
    sexo = input("Digite o seu sexo (f/m): ")
    estado_civil = input("Digite o seu estado civil (s/c/v/d): ")

    if len(nome) > 3:
            errostxt += "Nome inválido! Deve ter até 3 caracteres.\n"

    if idade < 0 or idade > 150:
            errosnum += "Idade inválida! Deve estar entre 0 e 150.\n"
        
    if salario <= 0:
            errosnum += "Salário inválido! Deve ser maior que zero.\n"

    if sexo != "f" and sexo != "m":
            errostxt += "Sexo inválido! Deve ser f ou m.\n"

    if estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d":
            errostxt += "Estado Civil inválido! Deve as seguintes opções: (s, c, v, d)."
    
    if errostxt or errosnum:
        print("As informações fornecidas são inválidas! Digite novamente.")
        if errostxt:
            print(f"Erros de texto:\n{errostxt}")
        if errosnum:
            print(f"Erros numéricos:\n{errosnum}")
            continue
        else:
            print(f"""
                        Nome: {nome}
                        Idade: {idade}
                        Salário: {salario:.2f}
                        Sexo: {sexo}
                        Estado Civil: {estado_civil}
                """)
            break