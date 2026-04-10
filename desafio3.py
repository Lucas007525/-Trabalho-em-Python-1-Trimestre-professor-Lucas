#TERCEIRO DESAFIO:

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Escolha uma opção:")
print("1 - Soma")
print("2 - Diferença (maior pelo menor)")
print("3 - Produto")
print("4 - Divisão")

opcao = input("Digite a opção: ")

if opcao == "1":
    print("Resultado:", num1 + num2)

elif opcao == "2":
    if num1 > num2:
        print("Resultado:", num1 - num2)
    else:
        print("Resultado:", num2 - num1)

elif opcao == "3":
    print("Resultado:", num1 * num2)

elif opcao == "4":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Erro: divisão por zero não é permitida.")

else:
    print("Opção inválida!")

#Uso input para receber dados do usuário em forma de texto.  
#float para converter esse valor em número decimal.
#E uma variável para armazenar o valor que será usado nas operações.
# Mostro as opções de cálculo para o usuário com print.
# Depois uso input() para que ele digite a opção desejada.
# Verifico qual opção o usuário escolheu usando if e elif.

# Para cada opção, realizo uma operação diferente com os números informados.

# Se a opção for 1, faço a soma dos dois números.

# Se a opção for 2, verifico qual número é maior e faço a subtração do maior pelo menor.

# Se a opção for 3, faço a multiplicação dos dois números.

# Se a opção for 4, verifico se o segundo número é diferente de zero antes de fazer a divisão,
# para evitar erro.

# Caso o usuário digite uma opção inválida, exibo uma mensagem de erro.

