#DESAFIO 5:

massa = float(input("Digite a massa inicial em gramas: "))
massa_inicial = massa
tempo = 0

while massa >= 0.5:
    massa = massa / 2
    tempo += 50

horas = tempo // 3600
resto = tempo % 3600
minutos = resto // 60
segundos = resto % 60

print("Massa inicial:", massa_inicial)
print("Massa final:", massa)
print("Tempo:", horas, "h", minutos, "min", segundos, "s")


# Recebo a massa inicial informada pelo usuário e armazeno em uma variável.
# Também guardo esse valor inicial em outra variável para exibir depois.

# Crio uma variável de tempo começando em 0, que será usada para somar os segundos
# a cada repetição do processo.

# Uso um while como estrutura de repetição. Ele executa o bloco de código enquanto
# a condição (massa >= 0.5) for verdadeira.

# Dentro do while, a cada repetição:
# - Divido a massa por 2, simulando a perda de metade da massa.
# - Somo 50 segundos ao tempo total, representando o tempo que passou.

# O loop continua executando até que a massa se torne menor que 0.5,
# momento em que a condição se torna falsa e o while é encerrado automaticamente.

# Após sair do loop, o tempo total está em segundos.
# Então faço a conversão para horas, minutos e segundos:

# Uso divisão inteira (//) para descobrir quantas horas cabem no tempo total.
# Uso o operador de resto (%) para pegar o que sobra e continuar o cálculo.

# Primeiro calculo as horas, depois uso o resto para calcular os minutos,
# e por fim o restante são os segundos.

# Por último, exibo:
# - a massa inicial (valor informado pelo usuário)
# - a massa final (valor após o loop)
# - o tempo total convertido em horas, minutos e segundos.
