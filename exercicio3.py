senha = input("Digite a senha para acessar o sistema: ")

if senha == "1234":
    print("Acesso permitido.")
    resposta = input("Deseja acessar a área administrativa? (S para sim, N para não): ")
    if resposta == "S":
        print("Entrando na área administrativa...")
    else:
        print("Você está na área de usuário comum.")
else:
    print("Senha incorreta! Acesso negado.")
