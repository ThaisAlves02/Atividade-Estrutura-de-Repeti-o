# Questão 2 - Pedir um nome de usuário e senha.
# Enunciado: Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if senha == usuario:
        print("Senha inválida! Digite novamente.")
        continue
    else:
        print("Acesso concedido.")
        break