"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta
é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
area = int(input('Quantos metros quadrados serão pintados?'))
litros = (area/3)
capacidade = 18.0
valor = 80.00
latas = litros/capacidade
preço_total = latas* valor
print('serão utilizadas', latas)
print('O Valor total da compra é: R$', preço_total)


