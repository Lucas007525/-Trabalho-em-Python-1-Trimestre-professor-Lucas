# Recebo a quantidade de termos que o usuário quer na sequência.
n = int(input("Digite a quantidade de termos: "))

# Inicializo os dois primeiros números da sequência.
a = 1
b = 1

# Exibo os dois primeiros valores.
print(a)
print(b)

# Repito o processo para gerar os próximos números.
for i in range(n - 2):

    # Calculo o próximo número somando os dois anteriores.
    novo = a + b

    # Mostro o novo número.
    print(novo)

    # Atualizo os valores para continuar a sequência.
    a = b
    b = novo

# Começa com 1 e 1
# Soma os dois → gera o próximo
# Anda pra frente
# Repete até chegar no N
# Eu começo com 1 e 1, depois sempre somo os dois últimos números 
# para gerar o próximo e repito isso até atingir a quantidade que o usuário pediu.