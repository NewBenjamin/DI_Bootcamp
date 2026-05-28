import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728

pairs = set()

for i in range(len(list_of_numbers)):
    complement = target_number - list_of_numbers[i]
    if complement in list_of_numbers:
        pair = tuple(sorted([list_of_numbers[i], complement]))
        pairs.add(pair)

for pair in sorted(pairs):
    print(f"{pair[0]} and {pair[1]} sums to the target_number {target_number}")