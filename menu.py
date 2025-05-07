import encode
import decode

# Menu de escolha
print('===================')
print('1 - Codificar')
print('2 - Decodificar')
print('===================')
op = int(input('Opção: '))

if op == 1: # 1 - Codificar
    mensagem = input('Digite a mensagem para ser codificada: ')

    # Chamo a função para fazer o encode da mensagem
    # Essa função retorna uma string de inteiros separados por espaços
    palavraCodificada = encode.encode(mensagem)
    print('mensagem codificada: ' + palavraCodificada)

if op == 2: # 2 - Decodificar
    palavraCodificada = input('Digite a mensagem para ser decodificada: ')

    # Chamo a função para fazer o encode da mensagem
    # Essa função retorna uma lista de inteiros
    mensagem = decode.decode(palavraCodificada)
    print('mensagem decodificada: ' + mensagem)
