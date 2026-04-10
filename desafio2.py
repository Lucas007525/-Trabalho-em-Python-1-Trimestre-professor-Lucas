# SEGUNDO DESAFIO: 2.

nucleotideo = input("Digite um nucleotídeo (A, T, C, G): ").upper()

complementos = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

if nucleotideo in complementos:
    print("Complementar:", complementos[nucleotideo])
else:
    print("Nucleotídeo inválido!")

# Usei um dicionário para organizar os nucleotídeos e seus complementares,
# como se fosse uma tabela de troca.

# Usei input() para permitir que o usuário digite no terminal
# e utilizei .upper() para garantir que as letras fiquem maiúsculas,
# evitando erro caso o usuário digite em minúsculo.

# O if verifica se o valor digitado está dentro dos nucleotídeos válidos.
# Se estiver, ele retorna o complementar correspondente.

# Caso não esteja, o else retorna a mensagem "Nucleotídeo inválido!".
# Escolhi usar dicionário porque deixa o código mais organizado
# e evita várias verificações com if.
