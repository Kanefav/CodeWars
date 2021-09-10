def cakes(recipe, available):
    cont = 0
    maxbolos = 0
    receita = list(recipe)
    while True:
        for itens  in range(0, len(receita)):
            try:
                if available[receita[itens]] == 0:
                    return maxbolos
                if recipe[receita[itens]] - available[receita[itens]] <= 0:
                    available[receita[itens]] = available[receita[itens]] - recipe[receita[itens]]
                    cont += 1
                else:
                    return maxbolos
                if cont == len(recipe):
                    maxbolos += 1
                    cont = 0
            except KeyError:
                return maxbolos

recipe = {'cream': 200, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}
available = {'sugar': 950, 'flour': 18500, 'milk': 19500, 'oil': 29500, 'cream': 4000}
print(f'da pra fazer {cakes(recipe, available)} bolos')