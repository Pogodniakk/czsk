def binary_search(szukana, tab):
    l = 0
    p = len(tab) - 1

    while l <= p:
        sr = (l + p) // 2

        if tab[sr] == szukana:
            return sr
        elif tab[sr] > szukana:
            p = sr - 1
        else:
            l = sr + 1

    return -1

tab = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
szukana = int(input("Podaj liczbę, którą chcesz znaleźć: "))

indeks = binary_search(szukana, tab)

if indeks != -1:
    print(f"Liczba {szukana} jest w tym zbiorze mordo i ma taki smieszny numerek -  {indeks}")
else:
    print("Kekw, towjej liczby nie ma w zbiorze - beka z ciebie")