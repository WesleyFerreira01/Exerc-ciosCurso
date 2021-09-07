from matplotlib import pyplot as plt
vendas = [3000, 2300, 1000, 500]
labels = ['E-commerce', 'Loja Física', 'e-mail', 'Marketplace']

# define o nível de separabilidade entre as partes, ordem do vetor representa as partes
explode = (0.1, 0, 0, 0)

# define o formato de visualização com saída em 1.1%%, sombras e a separação entre as partes
plt.pie(vendas, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode)

# inseri a legenda e a localização da legenda.
plt.legend(labels, loc=3)


# define que o gráfico será plotado em circulo
plt.axis('equal')

plt.show()