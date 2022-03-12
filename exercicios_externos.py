"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto: R$
- IR (11%): R$
- INSS (8%): R$
- Sindicato (5%): R$
= Salário Liquido: R$
Obs.: Salário Bruto - Descontos = Salário Líquido."""

valor_hora = float(input('Quanto voc ganha por hora?:'))
hora_mes = float(input('Quantas horas você trabalha no mês?:'))
salario = (valor_hora * hora_mes)
ir = (11 / 100.0 * salario)

inss = (8 / 100.0 * salario)

sin = (5 / 100.0 * salario)

desc = (ir + inss + sin)

salario_l = (salario - desc)

print('Valor Salário Bruto: R$', salario)
print('Valor do imposto de renda: R$', ir)
print('Valor INSS: R$', inss)
print('Valor Sindicato: R$', sin)
