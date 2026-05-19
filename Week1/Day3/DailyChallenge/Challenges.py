#Challenge 1


word = input("Enter a word: ")

letters = {}

for index, letter in enumerate(word):
    if letter in letters:
        letters[letter].append(index)
    else:
        letters[letter] = [index]

print(letters)


#Challenge 2
# =========================

items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}

wallet = "$300"

wallet_amount = int(wallet.replace("$", "").replace(",", ""))

basket = []

for item, price in items_purchase.items():

    clean_price = int(price.replace("$", "").replace(",", ""))

    if clean_price <= wallet_amount:
        basket.append(item)
        wallet_amount -= clean_price

if len(basket) == 0:
    print("Nothing")
else:
    print(sorted(basket))