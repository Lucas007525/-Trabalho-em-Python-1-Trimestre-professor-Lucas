maior = None
menor = None

while True:
    num = int(input("Digite um número (0 para parar): "))

    if num == 0:
        break

    if num < 0:
        print("Número negativo não será considerado.")
        continue

    if maior is None or num > maior:
        maior = num

    if menor is None or num < menor:
        menor = num

print("Maior valor:", maior)
print("Menor valor:", menor)

# Eu começo com as variáveis maior e menor como none pois ainda não há valores.
# Uso um loop while pra receber valores até o usuário digitar zero.
# Se o número for zero eu encerro o loop com break.
# Se o número for negativo eu informo meu usuário e ignoro seguindo com continue.

# Para os números positivos, verifico:
# - se é o maior valor já digitado
# - se é o menor valor já digitado
# Como se o programa perguntasse, esse número é maior ou menor do que eu ja vi ?

# Ao final, exibo o maior e o menor valor informados.
