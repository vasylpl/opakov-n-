cisla = [3, 5, 8, 1, 2, 4, 6, 7]
vzestupne = []
while cisla:
    max_cislo = cisla[0]
    for cislo in cisla:
        if cislo > max_cislo:
            max_cislo = cislo
    vzestupne.append(max_cislo)
    cisla.remove(max_cislo)

print(vzestupne)