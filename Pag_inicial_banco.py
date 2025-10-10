
print("Seja bem-vindo ao nosso banco União!")
print("Insira [1]-Sacar, [2]-Depositar, [3]-Extrato, [4]-Sair")

funcao = input("Por favor, insira um número: ")
funcao_int = int(funcao)

total = 1000
extrato_saque = 0
extrato_deposito = 0
total_saque = 0
total_deposito = 0

while funcao_int != 4:
  if total == 0:
    print("Sua conta está sem dinheiro, por favor faça algum deposito!")

  if funcao_int == 1:
    sacar = input("Insira quanto deseja sacar: ")
    sacar_float = float(sacar)
    total -= sacar_float
    extrato_saque += 1
    total_saque += sacar_float
    print(f"Você acabou de sacar R$ {total:.2f}")

  elif funcao_int == 2:
    depositar = input("Insira quanto você deseja depositar: ")
    depositar_float = float(depositar)
    total += depositar_float
    extrato_deposito += 1
    total_deposito += depositar_float
    print(f"Você acabou de depositar R$ {total:.2f}")

  elif funcao_int == 3:
    print(f"Foram sacadas {extrato_saque} vezes e foi sacado o total de R$ {total_saque:.2f}")
    print(f"Foram depositadas {extrato_deposito} vezes e foi depositado o total de R$ {total_deposito:.2f}")
    print(f"Saldo total da sua conta está em R$ {total:.2f}")
    if total <= 200:
      print(f"Saldo da conta está baixo, cuidado com os gastos!")
    elif total <= 2000:
      print(f"Saldo da conta está bom, bons investimentos!")
    elif total >= 10000:
      print(f"Saldo da conta está muito boa, continue assim!")
  break
print("Obrigado por usar nossos serviços, volte sempre!")