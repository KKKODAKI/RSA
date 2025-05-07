import rsa

# encoded = '37 304 45 24 16 315 79 304 315 37 265 304 30 304'

def decode(encoded):
        c = encoded.split()

        for i in range(len(c)):
                c[i] = int(c[i])
        
        p = 17 # Chave Privada P
        q = 23 # Chave Privada Q
        n = p * q # Chave Pública N

        totienteDeN = (p - 1) * (q - 1)

        e = 3 # Chave Pública E

        d = rsa.MinMultiploInverso(totienteDeN, e, 0, 1, totienteDeN) # Chave Privada D

        decoded = rsa.Decode(c, d, n)

        return decoded

# decode(encoded)