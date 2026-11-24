with open('banco-temperaturas-julho.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

total_linhas = len(linhas)
registros = []

for linha in linhas:
    partes = linha.strip().split()
    if partes:
        data_hora = f"{partes[0]} {partes[1]}"
        temperatura = float(partes[2])
        registros.append((data_hora, temperatura))

temperaturas = [reg[1] for reg in registros]
media_temp = sum(temperaturas) / len(temperaturas)
temp_min = min(temperaturas)
temp_max = max(temperaturas)

primeiro_registro_min = ""
for data_hora, temp in registros:
    if temp == temp_min:
        primeiro_registro_min = data_hora
        break

print(f"1. Total de linhas: {total_linhas}")
print(f"2. Média das temperaturas: {media_temp:.2f}°C")
print(f"3. Temperatura mínima: {temp_min}°C | Temperatura máxima: {temp_max}°C")
print(f"4. Primeiro registro da temperatura mínima: {primeiro_registro_min}")