import rsa

def encode(mensagem):
        
        letrasASCII = []
        c = []

        rsa.StringToASCII(mensagem, letrasASCII)

        p = 17 # Chave Privada P
        q = 23 # Chave Privada Q

        n = p * q # Chave Pública N

        e = 3 # Chave Pública E

        rsa.Encode(letrasASCII, c, e, n)
        
        return c