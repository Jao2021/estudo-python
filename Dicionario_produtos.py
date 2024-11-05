opcoes = ("1", "2", "3", "4", "5")
produtos = {}

while True:
  while True:
    print("\nEscolha a opção desejada: ")
    print("1 - cadastrar item")
    print("2 - alterar item")
    print("3 - excluir item")
    print("4 - exibir itens cadastrados")
    print("5 - sair\n")
    op = input()
    if op not in opcoes:
      print("Opção invalida\n")
    else:
      break
  if op == "5":
    break
  elif op == "1":
    nome = input("insira o nome do produto: ")
    qtd = int(input("insira a quantidade comprada: "))
    valor = float(input(f"insira o preço do produto {nome} : "))
    nome = nome.strip().upper()
    produtos[nome] = [qtd, valor]
    print(f"\nProduto {nome} cadastrado")
  elif op == "2":
    if not produtos:
      print("nenhum produto cadastrado")
    else:
      for c, v in produtos.items():
        print(f"{c:10} | Quantidade: {v[0]} | Valor: {v[1]}")
      alterar = input("Qual produto voce quer alterar")
      alterar = alterar.strip().upper()
      if alterar in produtos:
        nome = input("insira o nome do produto: ")
        qtd = int(input("insira a quantidade comprada: "))
        valor = float(input(f"insira o preço do produto {nome} : "))
        del produtos[alterar]
        produtos[nome] = [qtd, valor]
        print("\n Produto alterado com sucesso\n")
  elif op == "3":
    print("digite o nome do produto que deseja excluir\n")
    for c, v in produtos.items():
      print(f"{c:10} | Quantidade: {v[0]} | Valor: {v[1]}")
    apagar = input()
    apagar = apagar.strip().upper()
    if apagar in produtos:
      del produtos[apagar]
      print("produto apagado")
    else:
      print("produto cadastrado")
  elif op == "4":
    if not produtos:
      print("não tem produtos cadastrados")
    else:
      total = 0
      for c, v in produtos.items():
        print(f"{c:10} | Quantidade: {v[0]} | Valor: {v[1]} | Total unitario: {v[0] * v[1]}\n")
        total += v[0] * v[1]
      print(f"TOTAL: {total}")