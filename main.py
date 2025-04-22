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
        if values in country:
            continue
        else:
            country.append(values)
    return country

def country_remove_list(country):
    remove_list = ['"CAS"','"HUN"']
    alive_country = []
    for i in country:
        if i not in remove_list:
            alive_country.append(i)
    return alive_country

def finally_command(country):
    command = ''
    for i in country:
        for j in country:
            if i == j:
                continue
            else:
                command += f"clearae {i} {j}\n"
    return command


def main():
    penis = parser('TEST.eu4')
    country = country_list(penis)
    #print(country)
    alive_country = country_remove_list(country)
    command = finally_command(alive_country)
    print(command)
    print(len(command))

main()
