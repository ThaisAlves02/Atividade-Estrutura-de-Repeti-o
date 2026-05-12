#Questão - 24

somaNotas = 0
qtdNotas = 0

while True:
    nota = float(input("Digite a nota do aluno (0 para sair): "))
    
    if nota == 0:
        break
    
    somaNotas += nota
    qtdNotas += 1 
    media = somaNotas / qtdNotas 
    
print(f"Média: {media}")