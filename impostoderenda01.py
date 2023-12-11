print("IMPOSTO DE RENDA")
salario = float(input("""Digite o valor do seu salario, contendo duas casas decimais:    
EXEMPLO: 3002.00 :"""))    # primeiro: receber o salario do habitante

if salario <= 2000.00:
    print(f"De acordo com seu salário de: {salario} você não precisa pagar imposto (ISENTO)") # verificar se o valor se adequa ao isento, aqui usamos if para comecar o a solucao

elif salario <= 3000.00:
   imposto = (salario*8)/100
   print (f"Seu salário se enquadra no imposto de renda, você pagará 8% do seu salario dando um total de: R$ {imposto:.2f}")# se o bloco anterior nao se aplicar sera aplicado esse usando elif 


elif salario <=4500.00:
    imposto2 =(salario*18)/100
    print (f"Seu salário se enquadra no imposto de renda, você pagará 18% do seu salario dando um total de: R$ {imposto2:.2f}")

elif salario > 4500.00:
    imposto2=(salario*28)/100
    print (f"Seu salário se enquadra no imposto de renda, você pagará 28% do seu salario dando um total de: R$ {imposto2:.2f}")

#nos 3 blocos acima usamos elif para decidir a direcao da variavel em cada elif, so modificando o valor do salario sua porcentagem multiplicada e seu sinal > < =
# em cada print colocamos o imposto modificando suas casas decimais