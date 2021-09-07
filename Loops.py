x = 0
pessoas = []

while x < 6:
   nome = input('Qual o seu nome?')
   ## evitar que o nome joao entre na lista
   if nome =='Joao':
       break
   pessoas.append(nome)
   x += 1

print(pessoas)