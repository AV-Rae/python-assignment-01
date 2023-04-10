#RM:99011 NOME:Aksel Viktor Caminha Rae
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a = 0
loop = 0
print("bem vindo a vinheria de *inserir nome depois*")
nome = input("insira o seu nome: ")
idade = int(input("insira a sua idade: "))
enderecoCliente = input("insira o seu endereço: ")
enderecoEntrega = input("insira o endereço de entrega: ")

print("AVISO: é preciso ter idade maior de 18 anos para comprar álcool")

if idade >= 18:
    print("APROVADO!")
    catalogo = ["vinho tinto", "vinho branco", "vinho rose", "espumante", "vinho licoroso"]
    carrinho = []
    valor = 0
    menu = 0
    while menu < 4:
        print("digite o mumero de acordo com o menu")
        print(" 1. comprar\n 2. carrinho\n 3. checkout\n 4. sair")
        menu = int(input("escolha uma opção do menu: "))
        if menu > 3:
            print("Adeus!")
        else:
            if menu == 1:
                print("os vinhos disponiveis são " + str(catalogo) + "o valor de cada vinho em ordem é: 60, 40, 100, 100, 50")
                inp = str(input("digite o vinho a comprar comprar, caso nenhum deixe em branco. "))
                if inp == "vinho tinto":
                    valor = valor + 60
                    carrinho.append("vinho tinto")
                elif inp == "vinho branco":
                    valor = valor + 40
                    carrinho.append("vinho branco")
                elif inp == "vinho rose":
                    valor = valor + 100
                    carrinho.append("vinho rose")
                elif inp == "espumante":
                    valor = valor + 100
                    carrinho.append("espumante")
                elif inp == "vinho licoroso":
                    valor = valor + 50
                    carrinho.append("vinho licoroso")
            elif menu == 2:
                print(carrinho)
                print(valor)
            elif menu == 3:
                print("o valor total de " + str(carrinho) + " é " + str(valor))
                if valor < 100:
                    print("a compra não pode prosseguir pois ela não alcança o valor mínimo")
                elif valor < 200:
                    print("um frete de 10 reais será adicionado")
                    valor + 10
                    print("seu carrinho contêm estes items: " + str(carrinho) + " resultando um valor total de " + str(valor))
                    final = int(input("para finalizar a compra aperte 1, para voltar ao menu, digite 2 "))
                    if final == 1:
                        print("você comprou " + str(len(carrinho)) + " items, por um total de " + str(valor) + " a ser entregado em " + str(enderecoEntrega))
                        menu = 4
                    elif final == 2:
                        print("retornando ao menu...")
                        valor - 10
                else:
                    print("já que a compra excede 200R$, frete não será adicionado")
                    print("seu carrinho contêm estes items: " + str(carrinho) + " resultando em um valor total de " + str(valor))
                    final2 = int(input("para finalizar a compra digite 1, para voltar ao menu, digite 2 "))
                    if final2 == 1:
                        print("você comprou " + str(len(carrinho)) + " items, por um total de " + str(valor) + " a ser entregado em " + str(enderecoEntrega))
                        menu = 4
                    elif final2 == 2:
                        print("retornando ao menu...")
else:
    print("acesso negado")