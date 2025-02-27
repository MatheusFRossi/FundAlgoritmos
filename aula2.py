# a = int(input("Digite o primeiro número: "))
# b = int(input("Digite o segundo número: "))

# if a > b:
#     print("O menor número é o: ", b)
# if a < b:
#     print("O menor número é o: ", a)





# c = int(input("Digite um número: "))

# if c > 0:
#     print("O número digitado é positivo")
# else:
#     print("O número digitado é negativo")





# d = int(input("Digite um número para um dia da semana correspondente: "))

# if d == 1:
#     print("Domingo")
# if d == 2:
#     print("Segunda")
# if d == 3:
#     print("Terça")
# if d == 4:
#     print("Quarta")
# if d == 5:
#     print("Quinta")
# if d == 6:
#     print("Sexta")
# if d == 7:
#     print("Sábado")





# salario = float(input("Digite o seu salário: "))

# if salario > 1250:
#     novosalario = salario * 1.10
# else:
#     novosalario = salario * 1.15

# print(f"Seu novo salário é {novosalario:.2f}")





# anoAtual = int(input("Digite o ano atual: "))
# anoNasc = int(input("Digite o seu ano de nascimento: "))
# Idade = int( anoAtual - anoNasc)

# if (Idade >= 18):
#     print("Você pode retirar sua CNH")
# else:
#     print("Você ainda é muito novo para tirar sua CNH")





# AnoCarro = int(input("Digite o ano de um carro: "))
# AnoAtual = int(input("Digite o ano atual: "))
# CalcAnoCarro = int( AnoAtual - AnoCarro)

# if (CalcAnoCarro >= 3):
#     print("O carro em questão é um carro velho!")
# else:
#     print("O carro em questão é um carro novo")





# DistViagem= int(input("Digite a distância de uma viagem: "))

# if DistViagem <= 200:
#     ValorTotal = DistViagem * 0.50
#     print("Valor da viagem: ", ValorTotal)
# else:
#     ValorTotal = 0.50 * 200 + (DistViagem - (200 * 0.45))
#     print("O valor da sua viagem será: ", ValorTotal)





from math import ceil

# recupera o raio e a altura do cilindro
PI = 3.1415
Altura = float(input("Digite a altura do cilindro: "))
RaioCilindro = float(input("Digite o raio do Cilindro: "))
# calcular a área da base 
AreaBase = float( PI * RaioCilindro * RaioCilindro)
AreaLateral = float( Altura * 2 * PI * RaioCilindro)
AreaCilindro = float( AreaBase + AreaLateral)

print(f"Area a ser pintada: {AreaCilindro:.2f} m²")

# Calcular o volume de tinta
VolumeTinta = AreaCilindro / 3
print(f"Qtde de liros necessários: {VolumeTinta:.2f}")

# Calcular a qtd de latas de tint
latas_tinta = ceil(VolumeTinta / 5)
print(f"Qtde de latas de tinta: {latas_tinta}")

#Econtrar o preço unitário com base no número de latas
if latas_tinta == 1:
    preco_unitario = 50
elif latas_tinta == 2:
    preco_unitario = 48
elif latas_tinta == 3:
    preco_unitario = 46
elif latas_tinta > 3:
    preco_unitario = 45

print(f"Preço Unitário: {preco_unitario:.2f}")
print(f"Custo total: {latas_tinta * preco_unitario:.2f}")