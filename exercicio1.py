#  Se achar necessario, faça import de outras bibliotecas




# Crie a função que será avaliada no exercício aqui

def conta_palavras_unicas(*palavras):
    # Remove pontuações e caracteres especiais e converte para minúsculo
    palavras = [''.join(e.lower() for e in palavra if e.isalnum()) for palavra in palavras]
    
    # Utiliza o conjunto (set) para identificar palavras únicas
    palavras_unicas = set(palavras)
    
    # Retorna a quantidade de palavras únicas
    return len(palavras_unicas)



# Teste a sua função aqui (caso ache necessário)


print(conta_palavras_unicas("Escreva", "uma", "função", "que", "uma", "frase", "função"))



