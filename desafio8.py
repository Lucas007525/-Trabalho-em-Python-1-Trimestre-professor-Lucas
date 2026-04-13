sequencia = input("Digite a sequência de DNA: ").upper()

dna = {
    "A": "Adenina",
    "G": "Guanina",
    "C": "Citosina",
    "T": "Timina"
}

posicao = 1

for letra in sequencia:

    if letra in dna:
        print(posicao, "-", letra + ":", dna[letra])
    else:
        print("Nucleotídeo inválido!")

    posicao += 1

# Recebo a sequência de DNA e converto para maiúsculo para evitar erros.
# Crio um dicionário com os nucleotídeos e seus respectivos nomes.
# Crio uma variável para contar em qual posição da sequência cada letra está.
# Percorro a sequência letra por letra usando um loop.

# Para cada letra, verifico se ela é válida:
# - se for, mostro a posição, a letra e o nome correspondente.
# - se não for, informo que é inválida.

# Depois avanço para a próxima posição.
