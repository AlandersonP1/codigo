def contar_letra_a(s):
    return s.lower().count('a')


texto = input("Digite uma string: ")
quantidade = contar_letra_a(texto)
print(f"A letra 'a' aparece {quantidade} vezes na string.")
