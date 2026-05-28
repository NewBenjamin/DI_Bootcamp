# ====================================
# CHALLENGE 1 : Multiples of a Number
# ====================================

print("=" * 40)
print("CHALLENGE 1 : Multiples")
print("=" * 40)

number = int(input("Enter a number: "))
length = int(input("Enter a length: "))

multiples = []
for i in range(1, length + 1):
    multiples.append(number * i)

print(f"Result: {multiples}")

# ====================================
# CHALLENGE 2 : Remove Duplicates
# ====================================

print("\n" + "=" * 40)
print("CHALLENGE 2 : Remove Consecutive Duplicates")
print("=" * 40)

word = input("Enter a word: ")

result = ""
for i in range(len(word)):
    if i == 0 or word[i] != word[i-1]:
        result += word[i]

print(f"Result: {result}")
