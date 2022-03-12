def contar_caracteres(s):
    """Função que conta as caracteres de uma string

    Ex:

    >>> contar_caracteres('lorenzo')
    e: 1
    l: 1
    n: 1
    o: 2
    r: 1
    z: 1
    >>> contar_caracteres('banana')
    a: 3
    b: 1
    n: 2

    :param s: string a ser contada

    """
    caracteres_ordenados = sorted(s)# sort = ordena qualquer iterável. O resultado sempre será uma lista com os elementos ordenados

    caracter_anterior = caracteres_ordenados[0] # manter uma referência para o caracter anterior da string e enquanto o anterior for igual ao caracter corrente somamos o numero de vezes que este caracter aparece. Quando mudar de caracter, significa que eu posso imprimir a contagem deste caracter e zerar a contagem
    contagem = 1

    for caracter in caracteres_ordenados[1:]: # iterar a string, vamos pegar os caracteres ordenados e fazer o slice, eliminando o 1º elemento
        if caracter == caracter_anterior: # compara o caracter anterior com o atual
            contagem+= 1 #incrementar a contagem. Caso contário significa que terminei a contagem dos caracteres.
        else:
            print(f'{caracter_anterior}:{contagem}') # imprime o que eu vou querer
            caracter_anterior = caracter # caracter anterior passa a referenciar o caracter atual
            contagem = 1 # reseta a contagem

    print(f'{caracter_anterior}:{contagem}') # quando finalizar o "for" deve informar que tem mais 1 caracter a ser apresentado. Devo imprimir novamente o caracter.


if __name__ == '__main__': # para conferir criamos o if __name__. digitando main e enter, é preenchido automaticamente.
    contar_caracteres('lorenzo') # executar a contagem
    print() #foi acrescentado um print vazio para pular a linha entre a contagem das palavras
    contar_caracteres('banana')