print("Vamos lá descobrir o valor do seu aumento.")          
salario = float(input("Qual seu salário atual: "))  #receber o salário
if salario <= 400:   #passar o valor pelo if e realizar os calculos
    print(f"Novo salário: {salario+(salario*(15/100)):.2f} \nReajuste ganho: {salario*(15/100):.2f} \nEm percentual: 15 %")
elif salario > 400 and salario <= 800:
    print(f"Novo salário: {salario+(salario*(12/100)):.2f} \nReajuste ganho: {salario*(12/100):.2f} \nEm percentual: 12 %")#o mesmo processo que ocorreu acima ocorrera aqui mas com else nesse bloco ha a verificacao do valor e os calculos nessesarios para o reajuste
elif salario > 800 and salario <= 1200:
    print(f"Novo salário: {salario+(salario*(10/100)):.2f} \nReajuste ganho: {salario*(10/100):.2f} \nEm percentual: 10 %")
elif salario > 1200 and salario <= 2000:
    print(f"Novo salário: {salario+(salario*(7/100)):.2f} \nReajuste ganho: {salario*(7/100):.2f} \nEm percentual: 7 %")
else:
    print(f"Novo salário: {salario+(salario*(4/100)):.2f} \nReajuste ganho: {salario*(4/100):.2f} \nEm percentual: 4 %")

# em cada print e elif, else e if acima teremos os calculos e ajustes em cada bloco para se adequar a porcentagem requirida 