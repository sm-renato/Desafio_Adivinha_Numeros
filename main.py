from random import randrange                                                    #Importa a função 'randrange' da biblioteca random.


def generate_number():                                                          #Define uma função para gerar números aleatórios. A cada loop, gera um número e armazena na lista 'number', até formar um número com a quantidade de dígitos informada pelo usuário.
    digit_count = int(input('Digite a quantidade de algarismos desejada: '))    #Converte para inteiro e tribui à variável 'digit_count' o valor de algarismos informados pelo usuário.
    number = []                                                                 #Cria uma lista vazia.
    for _ in range(digit_count):                                                #Laço de repetição. Repete até atingir o valor informado em 'digit_count'.
        while True:                                                             #Enquanto for verdadeiro:
            random = randrange(0, 10)                                           #Gera um número aleatório entre 0 e 9 e armazena em 'random'.
            if not any(item in number for item in number if item == random):    #Verifica se não existe um item na lista number que é igual ao random gerado.
                number.append(random)                                           #Adiciona o número gerado à lista "number".
                break                                                           #Sai do while.
    return number                                                               #Retorna a lista de valores de 'number'.


def get_response():                                                             #Define uma função para armazenar o palpite do usuário.
    users_value = str(input('Digite sua resposta: '))                           #Converte para string e tribui à variável 'users_value' o valor digitado.
    r_list = []                                                                 #Cria uma lista vazia para armazenar os dígitos informados.
    for i in range(len(users_value)):                                           #Laço de repetição. A função 'len' verifica o número de caracteres digitados, definindo a condição de parada após percorrer todos os valores de 'users_value'.
        r_list.append(int(users_value[i]))                                      #A cada loop, adiciona um dígito informado à lista 'r_list', atualizando o índice, baseado em 'i'.
    return r_list                                                               #Retorna a lista "r_list" contendo o palpite informado pelo usuário.


def validate_response(correct_value, users_value):                              #Define uma função para receber o valor aleatório gerado na função 'generate_number' e o valor do palpite do usuário da função 'get_response'.
    if correct_value == users_value:                                            #Verifica se o valor gerado aleatóriamente é igual ao valor do palpite do usuário.
        print('Parabéns, você acertou!')                                        #Se os valores forem iguais, imprime 'Parabéns, você acertou!'.
        return 1                                                                #Retorna 1.
    elif len(correct_value) > len(users_value):                                 #Verifica se o valor gerado possui mais dígitos que o palpite do usuário.
        print('O número informado possui uma quantidade de algarismos'
              ' menor do que o esperado.')                                      #Em caso positivo, imprime 'O número informado possui uma quantidade de algarismos menor do que o esperado'.
    elif len(correct_value) < len(users_value):                                 #Verifica se o valor gerado possui menos dígitos que o palpite do usuário.
        print('O número informado possui uma quantidade de algarismos'
              ' maior do que o esperado.')                                      #Em caso positivo, imprime 'O número informado possui uma quantidade de algarismos maior do que o esperado'.
    else:                                                                       #Se nenhuma das condições se aplicam:
        digits_found = len(set(correct_value) & set(users_value))               #Armazena na variável contadora, 'digits_found', o número de digitos corretos no número gerado e na resposta do usuário.
        correct_place = 0                                                       #Inicializa a variável 'correct_place' em 0.
        for i in range(len(correct_value)):                                     #Laço de repetição até atingir a quantidade de dígitos do valor gerado.
            if correct_value[i] == users_value[i]:                              #Verifica se o valor gerado na posição 'i' é igual ao valor informado pelo usuário na posição 'i'.
                correct_place += 1                                              #Se o valor está na posição correta, incrementa-se a variável 'correct_place' em 1.
        if correct_place > 0:                                                   #Verifica se pelo menos 1 dos algarismos está correto na posição certa.
            print('O número informado possui ' + str(digits_found) +
                  ' algarismos corretos, sendo ' + str(correct_place) +
                  ' deles no lugar certo.')                                     #Em caso positivo, imprime a quantidade de algarismos e a quantidade que está na posição correta.
        elif digits_found > 0:                                                  #Verifica se pelo menos 1 dos algarismos está correto.
            print('O número informado possui ' + str(digits_found) +
                  ' algarismos corretos, em lugares errados.')                  #Em caso positivo, imprime a quantidade de algarismos corretos.
        else:                                                                   #Se nenhuma das condições se aplicam:
            print('O número informado está totalmente incorreto.')              #Imprime a mensagem de que todos os algarismos estão incorretos.
    return 0                                                                    #Retorna 0.


if __name__ == '__main__':
    print('------- Adivinha números -------')                                   #Exibe a mensagem 'Adivinha números'.
    number = generate_number()                                                  #Armazena na variável 'number' os algarismos gerados na função 'generate_number'.
    while True:                                                                 #Enquanto for verdadeiro:
        response = get_response()                                               #Armazena a lista de valores do palpite do usuário na variável 'response'.
        is_it_finished = validate_response(number, response)                    #Variável 'is_it_finished' recebe o resultado da função 'validate_response', tendo como retorno 0 ou 1.
        if is_it_finished == 1:                                                 #Caso receba '1', o usuário acertou o número e o jogo termina.
            break                                                               #Sai do while.
