altura= float(input("Digite sua altura: "))
peso_ideal= (75.7 * altura) - 58
print("seu peso ideal é: ", peso_ideal)

dias= int(input("Digite a quantidade de dias que o carro será utilizado: "))
CustoDiario= int(dias * 60)
quilometros= int(input("digite a quantidade de quilometros que serao percorridos: "))
CustoQuilometros= int( quilometros * 0.15 )
print("isso é o custo total de custo diário do carro com a quantidade de quilometros rodados: ", CustoDiario + CustoQuilometros)

Dias= int(input("Digite a quantidade de dias: "))
Horas= int(input("Digite a quantidade de horas: "))
Minutos= int(input("Digite a quantidade de minutos: "))
Segundos= int(input("Digite a quantidade de segundos: "))
Total= int(Segundos + (Minutos * 60) + (Horas * 3600) + (Dias * 86400))
print("Total: ", Total)

SalarioLiquido= int(input("Digite seu salário líquido: "))
SalarioBruto= int(SalarioLiquido - (SalarioLiquido * 0.11) - (SalarioLiquido * 0.08) - (SalarioLiquido * 0.05))
print("Seu salario bruto é: ", SalarioLiquido)