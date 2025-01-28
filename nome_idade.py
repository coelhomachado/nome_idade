name = input("Digite seu nome completo:")
ano = int(input("Digite ano que nasceu (Ex - aaaa):"))
executar = True
while executar == True:
  if ano >= 1922 and ano <= 2024:
    try:
      idade = 2025 - ano
      executar = False
      print(name, idade)
    except:
      print("Erro, tente outra vez!")
      break
  else:
    print("Erro, tente outra vez!")
    executar = True