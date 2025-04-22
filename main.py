block = []
country = []
in_blok = False

with open('TEST.eu4') as file:
    for line in file:
        line = line.strip()

        if line == 'players_countries={':
            in_blok = True

        if in_blok:
            if line == '}':
                break

            block.append(line)
block.pop(0)
for i, values in enumerate(block):
    if i % 2 == 0:
        continue
    if values == '"---"':
        continue
    else:
        country.append(values)



