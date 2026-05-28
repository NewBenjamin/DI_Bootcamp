#challenge n°1
number = int(input("Number: "))
length = int(input("Length: "))

result = []

for i in range(1, length + 1):
    result.append(number * i)

print(result)

#------------

#challenge n°2

word = input("Enter a word: ")

result = ""
for i in range(len(word)):
    if i == 0 or word[i] != word[i-1]:
        result += word[i]

print(result)