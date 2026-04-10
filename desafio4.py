#QUARTO DESAFIO:

sexo = input("Digite o sexo (M/F): ").upper()
idade = int(input("Digite a idade: "))

if idade < 10 or idade > 65:
    print("Valor: R$ 0.50")

elif 10 <= idade <= 17:
    print("Valor: R$ 4.28")

elif 18 <= idade <= 65:
    if sexo == "F":
        print("Valor: R$ 5.50")
    elif sexo == "M":
        print("Valor: R$ 8.25")
    else:
        print("Sexo inválido!")

else:
    print("Idade inválida!")

# Recebo o sexo e a idade do usuário e padronizo o sexo para maiúsculo com .upper().

# Verifico primeiro a idade, pois algumas regras dependem apenas da idade.

# Se a idade for menor que 10 ou maior que 65, o valor é 0,50 (desconto).

# Se a idade estiver entre 10 e 17, o valor é 4,28 (valor padrão pela idade).

# Se a idade estiver entre 18 e 65, verifico o sexo:
# feminino paga 5,50 e masculino paga 8,25 (defino os preços com base nas regras).

# Caso o sexo seja inválido, exibo uma mensagem de erro.