cisla = [3, 5, 8, 1, 2, 4, 6, 7]
sestupne = []
while cisla:
    min_cislo = cisla[0]
    for cislo in cisla:
        if cislo < min_cislo:
            min_cislo = cislo
    sestupne.append(min_cislo)
    cisla.remove(min_cislo)

print(sestupne)