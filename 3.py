import json

with open('dados.json', 'r', encoding='utf8') as arquivo:
    dados = json.load(arquivo)
    
    maior = {'dia': 0, 'valor': 0}
    menor = dados[1]
    
    contador = 0
    media = 0
    
    for dado in dados:
        
        if maior['valor'] < dado['valor']:
            maior = dado
        if menor['valor'] > dado['valor'] and dado['valor'] != 0:
            menor = dado
        
        contador = contador+1
        media = media + dado['valor']
    
    media = media / contador
    
    dias = []
    
    for dado in dados:
        if dado['valor'] > media:
            dias.append(dado['dia'])

print(f'O maior valor é do dia {maior["dia"]}, que foi {maior["valor"]}')
print(f'O menor valor é do dia {menor["dia"]}, que foi {menor["valor"]}')
print(f'A média foi de {media}')
print(f'Os dias que faturaram acima da média foram: {dias}')
