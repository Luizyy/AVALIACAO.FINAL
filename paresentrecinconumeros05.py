quantidade = []
par=0
#cria-se uma lista para adicionarmos os numeros futuros
for i in range(5):
#usamos range para repetir a acao
    quantidade = int(input(f'Digite o {i+1} nº: '))
#Se a variavel passar pela condicao ela sera adiciona em outra variavel
    if quantidade % 2 == 0:
        par = par+1
#ao final sera visualizada a quantidade de numeros pares
print(f"{par} valores pares")