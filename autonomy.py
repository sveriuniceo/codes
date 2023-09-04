name = input("Nome: ")
time = float(input("{}, digite tempo de viagem (em horas):".format(name)))
speed = float(input("{}, digite velociade média de viagem:".format(name)))
consumption = speed/12
print("Foram consumidos", consumption, "litros de comubustível")