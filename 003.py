cardapio = {
    "Pizza": 10,
    "Suco": 5,
    "Bolo": 7,
    "Refrigerante": 8
}

itens = list(cardapio.keys())
preco_total = 0

for i in range(len(itens)):
    item = itens[i]
    preco = cardapio[item]
    preco_total += preco
    print(f"{item}: R$ {preco}")

print(f"Total: R$ {preco_total}")