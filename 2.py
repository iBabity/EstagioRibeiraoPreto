def count_a_in_string(s):
    count = s.lower().count('a')  # Conta 'a' minúsculo
    return count

# Defina a string aqui ou descomente a parte de entrada
text = input("Digite uma string: ")  # Entrada do usuário

count = count_a_in_string(text)

if count > 0:
    print(f"A letra 'a' ocorre {count} vez(es) na string.")
else:
    print("A letra 'a' não ocorre na string.")
