


idade = 1


try:
    while idade <= 1:
        nome = str(input("Qual seu nome?"))
        email = str(input("Digite seu email:"))
        idade = int(input("Digite sua idade:"))
        if idade >= 18:
            print("Situação: Maior de idade.")
        elif idade <= 0:
            print("Por favor insira uma idade valida.")
        else:
            print("Situação: Menor de idade.")
except:
    print("Por favor, insira uma idade valida.")

with open("Cadastros.txt", "a") as cadastros:
    cadastros.write(" ### Dados Cadastrados ### \n" f"Nome: {nome} \n" f"Idade: {idade} \n" f"Email: {email} \n")
    if idade >= 18:
        cadastros.write("Situação: Maior de idade." f"\n ================================================")
    else:
        cadastros.write("Situação: Menor de idade." f"\n ================================================")
cadastros.close()
    