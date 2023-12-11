nuM = [] #criada uma lista para adicionarmos o mumero
pstv=0

for a in range(5):#repeticao range
    n = float(input(f'Digite o {a+1}° número: ')) #receber a variavel
#usamos if para aplicarmos a condicao de 'se o numero colocado é maior que 0"
    if n>0:
        pstv = pstv+1
        nuM.append(n)
#entao se sim ele executa o bloco entrando na lista e na variavel pstv
soma = sum(nuM) #e soma os numeros dentro da lista
print(f"{pstv} valores positivos")#mostra ao usuario seus valores positivos
#e a media calculada
print(f"{soma/5}")