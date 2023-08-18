#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui



def is_anagram(str1, str2):
    # Remove espaços, pontuações, converte para minúsculo e ordena as letras
    sorted_str1 = sorted(''.join(e.lower() for e in str1 if e.isalnum()))
    sorted_str2 = sorted(''.join(e.lower() for e in str2 if e.isalnum()))

    # Retorna True se as strings ordenadas forem iguais
    return sorted_str1 == sorted_str2


# Teste a sua função aqui (caso ache necessário)


print(is_anagram("banana", "banana"))  # Deve retornar True
print(is_anagram("locura", "doidera"))  # Deve retornar False








