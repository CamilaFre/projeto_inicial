nome = input("Digite seu nome")
salario = float(input("Digite seu salario"))
bonus = float(input("Digite seu bonus"))
KPI = 1000+salario*bonus
print(f"Olá, {nome}, o seu bônus foi de {KPI}")