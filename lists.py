listas = [[]]

while True:
    print("1-inserir os dados")
    print("2-mostrar dados")
    print("3-consultar dados especificos")
    op = int(input())
    if op == 1:
        nova = []
        nome = input("nome")
        cpf = input("cpf")
        tel = input("tel")
        nova.append(nome)
        nova.append(cpf)
        nova.append(tel)
        listas.append(nova)
    elif op == 2:
        for mostrar in listas:
            for mostrar2 in mostrar:
                print(mostrar2)

    elif op == 3:
        print(listas)
