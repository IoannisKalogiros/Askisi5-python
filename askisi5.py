from collections import Counter

# Ερώτημα α

with open('two_cities_ascii.txt') as fin:
    counter = Counter(fin.read().strip().lower().split())

print("Oi 10 dimofilesteres lexeis einai oi:",counter.most_common(10))


# Ερώτημα β

with open('two_cities_ascii.txt', 'r') as file:
    text = file.read().strip().lower().split()

counter2 = {}
for word in text:
    char = word[:2]
    if char in counter2.keys():
        counter2[char] += 1
    else:
        counter2[char] = 1

counter2 = sorted(counter2.items(), key=lambda x: x[1])
counter2.reverse()

print ("Oi 3 prwtoi sundiasmoi twn 2 prwtwn grammatwn pou arxizoun oi perissoteres oi lexeis einai:")
for i in range(3):
    print (counter2[i])


# Ερώτημα γ

counter3 = {}
for word in text:
    char = word[:3]
    if char in counter3.keys():
        counter3[char] += 1
    else:
        counter3[char] = 1

counter3 = sorted(counter3.items(), key=lambda x: x[1])
counter3.reverse()


print ("Oi 3 prwtoi sundiasmoi twn 3 prwtwn grammatwn pou arxizoun oi perissoteres lexeis einai:")
for i in range(3):
    print (counter3[i])