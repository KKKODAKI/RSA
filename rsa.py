def MinMultiploInverso(r1, r2, t1, t2, totienteDeN):

    q = int(r1 / r2) 

    r = r1 - q * r2

    t = t1 - q * t2

    if r == 1:
        if t < 0:
            t = totienteDeN + t
        return t
    
    return MinMultiploInverso(r2, r, t2, t, totienteDeN)

def StringToASCII(mensagem, letrasASCII):

    for i in range(len(mensagem)):
        letrasASCII.append(ord(mensagem[i]))

def Encode(letrasASCII, c, e, n):

    for i  in range(len(letrasASCII)):
        c.append((letrasASCII[i] ** e) % n)

def Decode(c, d, n):
    palavra = ''
    for i  in range(len(c)):
        palavra = palavra + (chr(int((c[i] ** d) % n)))

    return palavra

# mensagem = 'morte ao miojo'
# letrasASCII = []
# novasletrasASCII = []
# c = []

# StringToASCII(mensagem, letrasASCII)

# for i in range(len(letrasASCII)):
#         print('ASCII ', i, ' - ',letrasASCII[i])

# p = 17 # Chave Privada P
# q = 23 # Chave Privada Q
# n = p * q # Chave Pública N

# totienteDeN = (p - 1) * (q - 1)

# e = 3 # Chave Pública E

# d = MinMultiploInverso(totienteDeN, e, 0, 1, totienteDeN) # Chave Privada D
# print(d)

# print('d: ',d)

# Encode(letrasASCII, c, e, n)

# for i in range(len(c)):
#         print('ASCII ', i, ' - ',c[i])

# decoded = Decode(c, d, n)

# print(decoded)
