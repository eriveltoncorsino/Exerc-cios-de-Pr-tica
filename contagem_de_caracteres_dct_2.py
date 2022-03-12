def contar_caracteres(s):
    """Função que conta as caracteres de uma string

    Ex:

    >>> contar_caracteres('lorenzo')
    {'e': 1, 'l': 1, 'n': 1, 'o': 2, 'r': 1, 'z': 1} # deve ser colocados entre chaves, cada elemento entre aspas e separados por vírgula
    >>> contar_caracteres('banana')
    {'a': 3, 'b': 1, 'n': 2}

    :param s: string a ser contada

    """

    resultado={} # foi colocado o resultado dentro de um dicionário vazio

    for caracter in s:
        contagem = resultado.get(caracter, 0)
        contagem += 1
        resultado [caracter] = contagem
        
    return resultado # está retornando o resultado

if __name__ == '__main__': # para conferir criamos o if __name__. digitando main e enter, é preenchido automaticamente.
    print (contar_caracteres('lorenzo')) # imprime a contagem
    print() #foi acrescentado um print vazio para pular a linha entre a contagem das palavras
    print (contar_caracteres('banana'))