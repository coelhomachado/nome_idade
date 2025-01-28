name = input("Digite seu nome completo:")
executar = True
while executar == True:
  ano = input("Digite ano que nasceu (Ex - aaaa):")
  try:
    ano = int(ano)
    if ano < 1922 or ano > 2024:
      print("O ano precisa obedecer o seguinte intervalo: 1922-2024")
    else:
      idade = 2025 - ano
      executar = False
      print("O usuário", name, "completou ou completará", idade, "anos de idade em 2025")
  except:
    print("Os anos precisam ser escritos apenas com números")