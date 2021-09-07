cores = {'verde':'green', 'vermelho': 'red', 'preto': 'black', 'branco': 'white'}
cor = input('Escolha a cor que deseja traduzir:').lower()
traduçao =cores.get(cor,'Esta cor nao consta no meu dicionãrio')
print(traduçao)