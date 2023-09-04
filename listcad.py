listas = [[]]

while True:
    print("1-Cadastrar Carros")
    print("2-Lista Cadastros")
    print("3-Procurar Carro Especifico")
    op = int(input())
    if op == 1:
        nova = [] 
        id = input("Marca")
        model = input("Modelo")
        version = input("Versão")
        nova.append(id)
        nova.append(model)
        nova.append(version)
        listas.append(nova)
    elif op == 2:
        for mostrar in listas:
            for mostrar2 in mostrar:
                print(mostrar2)

    elif op == 3:
        print(listas)