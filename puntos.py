import random
premios = ["1000", "Viaje a Cartagena", "Bicicleta", "1 Dolar", "Otra Oportunidad"]
num = random.randint(0,4)
if num == 0:
    print(f"Su premio es igual: {premios[num]}")
