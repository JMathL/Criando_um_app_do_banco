#criando um programa simulando um caixa eletrônico
print("Seja bem-vindo ao nosso banco União!")

def validar_valor_monetario(valor_str):

    try:
        
        valor_str = valor_str.strip()
      
        if '.' in valor_str:
            partes = valor_str.split('.')
            if len(partes) == 2 and len(partes[1]) > 2:
                raise ValueError("O valor deve ter no máximo 2 casas decimais após o ponto (ex: 10.50 ou 100.00).")
        
        valor = float(valor_str)
        return valor
    except ValueError as e:
        if "casas decimais" in str(e):
            raise
        raise ValueError("Digite apenas números válidos.")

# Inicializando variáveis
total = 0.0
extrato_saque = 0
total_saque = 0.0
extrato_deposito = 0
total_deposito = 0.0

# Loop de login
while True:
  try:
    login = int(input("Digite seu CPF: "))
    senha = int(input("Digite sua senha: "))
    if login == 123 and senha == 123:
      print("Login realizado com sucesso!")
      break
    else:
      print("Login ou senha errado(s), por favor, tentar novamente.")
  except ValueError:
    print("Erro: Digite apenas números inteiros.")

while True:

  print(f"Insira [1]-Sacar, [2]-Depositar, [3]-Extrato, [4]-Cambiar, [5]-Sair.")

  try:
    escolha = int(input("Por favor, escolha a operação: "))
    if escolha < 1 or escolha > 5:
      print("Erro: Escolha um número de operação de 1 a 5")
      continue  
  except ValueError:
    print("Erro: Digite apenas números inteiros.")
    continue

  if escolha == 1:
    try:
      sacar = validar_valor_monetario(input("Insira quanto deseja sacar: "))
      if total <= 0:
        print("Erro: Sua conta está sem saldo, por favor faça um depósito.")
        continue
      elif sacar > total:
        print(f"Erro: Saldo insuficiente. Seu saldo atual é R$ {total:.2f}")
        print("Por favor, faça um depósito ou escolha um valor menor.")
        continue
      elif sacar <= 0:
        print("Erro: O valor do saque deve ser maior que zero.")
        continue
      total -= sacar
      extrato_saque += 1
      total_saque += sacar
      print(f"Você acabou de sacar R$ {sacar:.2f}!")
      print(f"Sua conta ficou com o total de R$ {total:.2f}")
    except ValueError as e:
      print(f"Erro: {e}")
  elif escolha == 2:
    try:
      depositar = validar_valor_monetario(input("Insira quanto deseja depositar: "))
      if depositar <= 0:
        print("Erro: O valor do depósito deve ser maior que zero.")
        continue
      total += depositar
      extrato_deposito += 1
      total_deposito += depositar
      print(f"Você acabou de depositar R$ {depositar:.2f}!")
      print(f"Sua conta ficou com o total de R$ {total:.2f}")
    except ValueError as e:
      print(f"Erro: {e}")
  elif escolha == 3:
    print(f"Foram sacadas {extrato_saque} vezes e foi sacado o total de R$ {total_saque:.2f}")
    print(f"Foram depositadas {extrato_deposito} vezes e foi depositado o total de R$ {total_deposito:.2f}")
    print(f"Saldo total da sua conta está em R$ {total:.2f}")
    if total <= 200:
      print(f"Saldo da conta está baixo, cuidado com os gastos!")
    elif total <= 2000:
      print(f"Saldo da conta está bom, bons investimentos!")
    elif total >= 10000:
      print(f"Saldo da conta está muito boa, continue assim!")
  elif escolha == 4:
    print("Suportamos as moedas: [1]-Real(R$), [2]-Euro(€), [3]-Dólar(US$) e [4]-Libra(£)")
    try:
      primeira_moeda = int(input("Selecione o número da moeda quer cambiar: "))
      segunda_moeda = int(input("Selecione o número da para qual moeda quer cambiar: "))
      valor = validar_valor_monetario(input("Digite quanto quer cambiar: "))
      if primeira_moeda == segunda_moeda:
        print("Não pode escolher a mesma moeda para cambiar! Tente novamente")
        continue
      if primeira_moeda == 1 and segunda_moeda == 2:
        resultado = valor/0.16
        print(f"O valor cambiado foi de R$ {valor:.2f} para € {resultado:.2f}")
      elif primeira_moeda == 1 and segunda_moeda == 3:
        resultado = valor/0.19
        print(f"O valor cambiado foi de R$ {valor:.2f} para US$ {resultado:.2f}")
      elif primeira_moeda == 1 and segunda_moeda == 4:
        resultado = valor/0.14
        print(f"O valor cambiado foi de R$ {valor:.2f} para £ {resultado:.2f}")
      elif primeira_moeda == 2 and segunda_moeda == 1:
        resultado = valor*6.13
        print(f"O valor cambiado foi de € {valor:.2f} para R$ {resultado:.2f}")
      elif primeira_moeda == 2 and segunda_moeda == 3:
        resultado = valor*1.16
        print(f"O valor cambiado foi de € {valor:.2f} para US$ {resultado:.2f}")
      elif primeira_moeda == 2 and segunda_moeda == 4:
        resultado = valor/0.88
        print(f"O valor cambiado foi de € {valor:.2f} para £ {resultado:.2f}")
      elif primeira_moeda == 3 and segunda_moeda == 1:
        resultado = valor*5.29
        print(f"O valor cambiado foi de US$ {valor:.2f} para R$ {resultado:.2f}")
      elif primeira_moeda == 3 and segunda_moeda == 2:
        resultado = valor*0.86
        print(f"O valor cambiado foi de US$ {valor:.2f} para € {resultado:.2f}")
      elif primeira_moeda == 3 and segunda_moeda == 4:
        resultado = valor/0.75
        print(f"O valor cambiado foi de US$ {valor:.2f} para £ {resultado:.2f}") 
      elif primeira_moeda == 4 and segunda_moeda == 1:
        resultado = valor*6.95
        print(f"O valor cambiado foi de £ {valor:.2f} para R$ {resultado:.2f}")
      elif primeira_moeda == 4 and segunda_moeda == 2:
        resultado = valor*1.13
        print(f"O valor cambiado foi de £ {valor:.2f} para € {resultado:.2f}")
      elif primeira_moeda == 4 and segunda_moeda == 3:
        resultado = valor*1.31
        print(f"O valor cambiado foi de £ {valor:.2f} para US$ {resultado:.2f}")         
    except ValueError as e:
      print(f"Erro: {e}")
      continue
  elif escolha == 5:
    print("Deslogando...")
    print("Até uma próxima vez!")
    break