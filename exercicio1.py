#Altura das pessoas do genero masculino e feminino, 15 pessoas. 
# A maior aultura do grupo; A média de altura das pessoas do gênero masculino; O número de pessoas do gênero feminino.

dados = []

for i in range(15):
    while True:
        try:
            altura = float(input(f"Digite a altura da {i+1}ª pessoa (em cm): "))
            if altura <= 0:
                print("Por favor, insira uma altura válida (maior que zero).")
                continue
            break
        except ValueError:
            print("Por favor, insira um número válido para a altura.")
    
    while True:
        genero = input(f"Digite o gênero da {i+1}ª pessoa (Masculino ou Feminino): ").strip().lower()
        if genero in ['masculino', 'feminino']:
            break
        else:
            print("Por favor, insira 'Masculino' ou 'Feminino'.")

    dados.append((altura, genero.capitalize()))

alturas = [altura for altura, genero in dados]
maior_altura = max(alturas)
menor_altura = min(alturas)

alturas_masculinas = [altura for altura, genero in dados if genero == 'Masculino']
media_altura_masculina = sum(alturas_masculinas) / len(alturas_masculinas)

numero_feminino = len([genero for altura, genero in dados if genero == 'Feminino'])

print(f'\nResultados:')
print(f'Maior altura: {maior_altura} cm')
print(f'Menor altura: {menor_altura} cm')
print(f'Média de altura dos homens: {media_altura_masculina:.2f} cm')
print(f'Número de mulheres: {numero_feminino}')
