faturamentos = [
    {'estado': 'sp', 'valor': 67836.43},
    {'estado': 'rj', 'valor': 36678.66},
    {'estado': 'mg', 'valor': 29229.88},
    {'estado': 'es', 'valor': 27165.48},
    {'estado': 'outros', 'valor': 19846.53},
]

total = 0

for faturamento in faturamentos:
    print(faturamento)
    total = total+ faturamento['valor']
    
print(total)

for faturamento in faturamentos:
    percentual = 100 * faturamento['valor'] / total
    print(f'O percentual de {faturamento["estado"]} é de {round(percentual, 2)}%')
    
