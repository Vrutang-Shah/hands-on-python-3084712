NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

for name in NAMES:
    print(name)

for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")

for name in reversed(NAMES):
    print(name)

for i in range(5):
    print(i)

# enumerate

square_set = {x**2 for x in range(5) if x%2 == 0}
print(square_set)


Square_set1 = {x for x in range(5) if x%2 == 0}
print(Square_set1)

Square_set1 = {x**2 for x in range(5) if x%2 == 0}
print(Square_set1)