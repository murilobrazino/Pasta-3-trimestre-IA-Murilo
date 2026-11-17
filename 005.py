itens = ["pizza", "suco", "bolo", "refrigerante"]
precos = [10, 5, 7, 8]
total_compra = 0

print("--- Cardápio da Cantina ---")
for i in range(len(itens)):
    print(f"{i} - {itens[i]} (Preço: R$ {precos[i]})")

print("\nDigite -1 a qualquer momento para encerrar o pedido.")

while True:
    escolha = int(input("\nEscolha o número do item: "))

    if escolha == -1:
        break

    if 0 <= escolha < len(itens):
        total_compra += precos[escolha]
        print(f"-> {itens[escolha]} adicionado(a) com sucesso!")
    else:
        print("-> Opção inválida. Por favor, escolha um número do cardápio.")

print("\n--- Resumo do Pedido ---")
print(f"O valor total da sua compra é: R$ {total_compra}")