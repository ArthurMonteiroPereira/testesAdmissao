def contaAs(s):
    count = 0
    for char in s:
        if char.lower() == 'a':
            count += 1
    return count

# Entrada da string
s = input("Informe uma string: ")

# Conta e exibe o número de ocorrências de 'a'
count = contaAs(s)
print(f"A letra 'a' ocorre {count} vez(es) na string.")
