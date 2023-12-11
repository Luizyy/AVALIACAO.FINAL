print("Descubra o ddd")
ddd = int(input("Digite seu DDD:" )) #RECEBER O DDD
if ddd==61:# VERICAR USANDO IF SE O DDD COM A PRIMEIRA CONDICAO SE ELA FOR ELA É DE BRASILIA
  print("Brasilia")
elif ddd==71:
  print("Salvador")#como vimos no bloco acima acontecera a mesma logica seguindo elif verificando se o dd corresponde a condicao
elif ddd==11:
  print("Sao Paulo")  
elif ddd==21:
  print("Rio de Janeiro") 
elif ddd==32:
  print("Juiz de Fora") 
elif ddd==19:
  print("Campinas") 
elif ddd==27:
  print("Vitoria") 
elif ddd==31:
  print("Belo Horizonte") 
else:
  print("DDD nao cadastrado :( )") # na ultima condicao usada se todas as acima nao funcionarem sera aplicada quando o ddd nao existe no sistema