"""Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de internet (em Mbps),calcule e informe o tempo
aproximado de download do arquivo usando este link (em minutos).
"""
download = int(input('Qual o tamanho do arquivo para download em MB:'))
velocidade = int(input(' Qual a velocidade de um link de internet em MBPS'))
tempo = download/velocidade
print(download)
print(velocidade)
print(tempo)
