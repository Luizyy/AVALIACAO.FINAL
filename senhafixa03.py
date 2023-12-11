s = 2002 #guarda a senha para comparar com as tentativas depois
tentativa = int(input("Digite a senha: ")) # pedir a senha para conferir e autorizar a entrada
while tentativa != s:#usando essa forma temos se em casa de sim um 0 no resto em casa de nao temos um tente novamente
    print("Senha Invalida.(TENTE NOVAMENTE)")
    tentativa = int(input("Digite a senha: "))
print("Acesso permitido.") # em caso de acerto temos como resposta essa linha