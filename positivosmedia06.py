print("POSITIVOS MÉDIA:")
intero= []   #usar lista para armazenar numeros futuros
soma = 0   #e o contador para soma os numeros positivos
for i in range(6): #usar for e range para repeticao
    num= float(input("digite o número:"))
    if num>0:                           #usar if para os numeros se enquadrarem nas condicoes necessarias
        intero.append(num)  # usar append para substituir
    soma= sum(intero) # somar
quantidade=len(intero) #contar quantos sao
media= soma/quantidade # calculo da media
print(f"{quantidade} valores positivos.\n{media}") # mostrar ao usuario sua resposta