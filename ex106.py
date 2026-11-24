temperaturas_por_dia = {}

with open('banco-temperaturas-julho.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        if linha:
            partes = linha.split()
            data = partes[0]
            temperatura = float(partes[2])
            
            if data not in temperaturas_por_dia:
                temperaturas_por_dia[data] = []
            temperaturas_por_dia[data].append(temperatura)

data_consulta = input("Digite a data desejada (formato aaaa-mm-dd): ").strip()

if data_consulta in temperaturas_por_dia:
    lista_temps = temperaturas_por_dia[data_consulta]
    
    t_min = min(lista_temps)
    t_max = max(lista_temps)
    amplitude = t_max - t_min
    
    print(f"Dados para o dia {data_consulta}:")
    print(f"- Temperatura mínima: {t_min:.2f}°C")
    print(f"- Temperatura máxima: {t_max:.2f}°C")
    print(f"- Amplitude térmica: {amplitude:.2f}°C")
else:
    print(f"A data '{data_consulta}' não foi encontrada no arquivo.")