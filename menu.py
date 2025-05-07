import encode
import decode

print('===================')
print('1 - Codificar')
print('2 - Decificar')
print('===================')
op = int(input('Opção: '))

if op == 1:
    palavraCodificada = []
    mensagem = input('Digite a mensagem para ser codificada: ')
    palavraCodificada = encode.encode(mensagem)
    print(palavraCodificada)

if op == 2:
    palavraCodificada = input('Digite a mensagem para ser decodificada: ')
    mensagem = decode.decode(palavraCodificada)
    print(mensagem)