import sys

lang1 = set({}) # Mumbo
lang2 = set({}) # Jumbo

i = 0
for line in sys.stdin:
    if i % 2:
        for j in range(len(line)):
            lang2.add(line[j])
    else:
        for j in range(len(line)):
            lang1.add(line[j])
    i += 1

print("Mumbo" if len(lang1) > len(lang2) else "Jumbo")
