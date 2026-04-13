alunos = []

for i in range(4):
    nota = float(input("Digite a nota do aluno:"))
    alunos.append(nota)

Media = sum(alunos)/len(alunos)

if Media < 6.0: 
    print("Reprovado")
else:
    print ("Aprovado")

# Crio uma lista vazia para armazenar as notas do aluno.(Alunos = [])

# Uso um laço for para repetir 4 vezes, pois o exercício pede 4 notas.

# Em cada repetição, recebo a nota digitada pelo usuário com input()
# e converto para número decimal com float.

# Uso append() para adicionar cada nota na lista.

# Após coletar todas as notas, calculo a média somando os valores com sum()
# e dividindo pela quantidade de notas com len().

# Exibo o valor da média.

# Uso uma estrutura condicional para verificar se o aluno foi aprovado ou não:
# se a média for menor que 6.0, o aluno está reprovado, caso contrário está aprovado.

#Por que eu usei o Len ?
# Uso len(alunos) para garantir que a s
# média seja calculada corretamente com base na quantidade de notas digitadas.