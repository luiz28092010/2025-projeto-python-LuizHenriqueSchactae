'''
Game - V.10
2025.06.23
Luiz Henrique Schactae Brandão
'''

# Objetivo: resolva todas as perguntas de matematica que serão atribuidas e tente acertar todas

import random # importa a função de sorteio

def gerar_pergunta(): # define 'gerar_pergunta' como uma função
    operadores = ['+', '-', '*', '/']
    operador = random.choice(operadores) # sorteia um sinal de conta da variavel operadores e o coloca nos lugares sinalizados na variavel operador

    if operador == '/': # define uma condição para se operador por 'divisão'
        b = random.randint(1, 10)     # Para nao ter nenhuma divisão por zero uzamos esse codigo para limitar para aparecer apenas números de 1 até 10

        a = b * random.randint(1, 10)  # garante que a pode se multiplicar por b para sempre ser uma divisão exata
    else:
        a = random.randint(1, 20) # sorteia um número aleatorio de 1 a 20 para variavel 'a'
        b = random.randint(1, 20) # sortei um número aleatorio de 1 a 20 para variavel 'b'

    pergunta = f"{a} {operador} {b}" # cria uma pergunta gerando dos valores 'a' e 'b', gera tambem um oprador como soma ou divisão
    resposta_certa = eval(pergunta)  # calcula a resposta

    if operador == '/': # cria uma condição para variavel operador
        resposta_certa = int(resposta_certa)  # resultado inteiro para divisão exata

    return pergunta, resposta_certa # retorna mostrando qual sera a resposta certa

def jogar(): # define jogar como variavel
    print("Bem-vindo ao Jogo de Matemática!") # mostrar a mensagem: Bem vindo ao jogo da matemática
    tentativas = 5 # esse sera o valor inicial da variavel tentativas e vai mudar conforme vai se jogando o jogo
    acertos = 0 # e esse sera o valor inicial da variavel acertos

    for i in range(tentativas): # esse código é para quantas vezes o codigo vai repetir, nesse caso ele vai repetir 5 vezes 
        pergunta, resposta_certa = gerar_pergunta() 
        while True: # cria um loop infinito
            try: # utilizado para testar um bloco de código em busca de erros ou exceções que possam ocorrer durante sua execução.
                resposta = float(input(f"\nPergunta {i + 1}: Quanto é {pergunta}? ")) # pede uma resposta
                break # usado para interromper um loop
            except ValueError: # comando executado caso você digite um número invalido
                print("Por favor, digite um número válido.") # imprime a mensagem pedindo um número valido

        if abs(resposta - resposta_certa) < 0.001:  # para evitar problemas com float
            print(" correto Você acertou!") # Mostra a mensagem que você acertou
            acertos += 1 # adiciona 1 ou deixa = 1 a variavel 'acertos'
        else: # esse é o comando que dara uma outra condição
            print(f" Boboca a resposta certa era {resposta_certa}") # caso erre a pergunta mostra qual que vai ser a resposta certa

    print(f"\n Acabou o jogo e você teve {acertos} acertos de {tentativas} perguntas.") # mostra a mensagem com número de acertos

if __name__ == "__main__":
    jogar()



