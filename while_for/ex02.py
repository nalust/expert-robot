user = input("Digite seu nome de usuário: ")
password = input("Digite sua senha: ")

while user == password:
    print("O nome de usário não pode ser igual a senha. Por favor, tente novamente.")
    user = input("Digite seu nome de usuário: ")
    password = input("Digite sua senha: ")