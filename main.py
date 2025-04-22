def parser(filename):
    block = []
    in_blok = False
    with open(filename) as file:
        for line in file:
            line = line.strip()

            if line == 'players_countries={':
                in_blok = True

            if in_blok:
                if line == '}':
                    break

                block.append(line)
    block.pop(0)

    return block


def country_list(block):
    country = []
    for i, values in enumerate(block):
        if i % 2 == 0:
            continue
        if values == '"---"':
            continue
        else:
            country.append(values)
    return country


def main():
    penis = parser('TEST.eu4')
    country = country_list(penis)
    print(country)

main()
