texto = "Teste de inversão de string."
texto_invertido = ""
index = 0
while texto[index:]:
    texto_invertido = texto[index] + texto_invertido
    index += 1
print("String invertida:", texto_invertido)
