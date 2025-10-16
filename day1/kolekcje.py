# kolekcje - przechowuje wiele elementow, róznego typu na raz

# lista - zachowuje kolejnosc przy dodawania elementów
lista = []  # pusta lista
lista_pusta = list()  # pusta lista
print(lista)  # []
print(lista_pusta)  # []
print(type(lista_pusta))  # <class 'list'>

lista_pusta.append("Piotr")
lista_pusta.append("Anna")
lista_pusta.append("Przemek")
lista_pusta.append("Radek")
lista_pusta.append("Zenek")
print(lista_pusta)  # ['Piotr', 'Anna', 'Przemek', 'Radek', 'Zenek']

lista_pusta.sort()  # zmienia oryginał
print(lista_pusta)  # ['Anna', 'Piotr', 'Przemek', 'Radek', 'Zenek']

lista_pusta.append(345)
print(lista_pusta)  # ['Anna', 'Piotr', 'Przemek', 'Radek', 'Zenek', 345]
# lista_pusta.sort() # TypeError: '<' not supported between instances of 'int' and 'str'

print(lista_pusta[0])  # Anna, indeksowanie od 0
print(lista_pusta[5])  # 345
print(len(lista_pusta))  # 6, liczba elementów w liście
print(lista_pusta[len(lista) - 1])  # 345
print(lista_pusta[-1])  # 345 ostatni eleemnt z listy
print(lista_pusta[-3])  # Radek

# print(lista_pusta[56])  # IndexError: list index out of range

# wstawienie elementu w konkretne miejsce
lista_pusta.insert(1, "Magda")
print(lista_pusta)  # ['Anna', 'Magda', 'Piotr', 'Przemek', 'Radek', 'Zenek', 345]

# zamina elementu na wskazanym indeksie
lista_pusta[6] = "Aneta"
print(lista_pusta)  # ['Anna', 'Magda', 'Piotr', 'Przemek', 'Radek', 'Zenek', 'Aneta']

# slicowanie - fragment listy
print(lista_pusta[0:2])  # ['Anna', 'Magda'], 0,1 z prawej zbiór otwarty
print(lista_pusta[:2])  # ['Anna', 'Magda']
print(lista_pusta[1:])  # ['Magda', 'Piotr', 'Przemek', 'Radek', 'Zenek', 'Aneta']
print(lista_pusta[1:6])  # ['Magda', 'Piotr', 'Przemek', 'Radek', 'Zenek']
print(lista_pusta[:])  # ['Anna', 'Magda', 'Piotr', 'Przemek', 'Radek', 'Zenek', 'Aneta']

print(lista_pusta[1:-1])  # ['Magda', 'Piotr', 'Przemek', 'Radek', 'Zenek']
print(lista_pusta[0:4:2])  # ['Anna', 'Piotr'], co drugi [start:stop:krok]
print(lista_pusta[::-1])  # ['Aneta', 'Zenek', 'Radek', 'Przemek', 'Piotr', 'Magda', 'Anna'] odwrotna kolejność

print(lista_pusta[67:90])  # []

#  ['Anna', 'Magda', 'Piotr', 'Przemek', 'Radek', 'Zenek', 'Aneta']
# pop() - zwraca co usnął, po indeksie
print(lista_pusta.pop())  # Aneta, ostatni
print(lista_pusta)  # ['Anna', 'Magda', 'Piotr', 'Przemek', 'Radek', 'Zenek']
print(lista_pusta.pop(4))  # Radek

# usunicie po elemencie
lista_pusta.remove('Magda')
print(lista_pusta)  # ['Anna', 'Piotr', 'Przemek', 'Zenek']

osoby = ["Tomek", "Ewa", "Adam"]
print(osoby)
osoby.extend(lista_pusta)
print(osoby)  # ['Tomek', 'Ewa', 'Adam', 'Anna', 'Piotr', 'Przemek', 'Zenek']

nowa_lista = osoby + lista_pusta
print(nowa_lista)
# ['Tomek', 'Ewa', 'Adam', 'Anna', 'Piotr', 'Przemek', 'Zenek', 'Anna', 'Piotr', 'Przemek', 'Zenek']

n_lista = nowa_lista  # kopia referencji, miejsca w pamięci
print(n_lista)
print(nowa_lista)
lista_copy = nowa_lista.copy()  # kopia elementów listy
# ['Tomek', 'Ewa', 'Adam', 'Anna', 'Piotr', 'Przemek', 'Zenek', 'Anna', 'Piotr', 'Przemek', 'Zenek']
# ['Tomek', 'Ewa', 'Adam', 'Anna', 'Piotr', 'Przemek', 'Zenek', 'Anna', 'Piotr', 'Przemek', 'Zenek']
nowa_lista.clear()  # usunicie wszystkich elementw z listy
print(n_lista)  # []
print(nowa_lista)  # []
print(lista_copy)
# ['Tomek', 'Ewa', 'Adam', 'Anna', 'Piotr', 'Przemek', 'Zenek', 'Anna', 'Piotr', 'Przemek', 'Zenek']
print(id(nowa_lista))
print(id(n_lista))
print(id(lista_copy))
# 2655419609344
# 2655419609344
# 2655422290624

# krotka (tuple) - niemutowalna lista, tylko do odczytu
# pozwala lepiej zarzadzac pamięcią
krotka = (23, 45, 67, "Radek")
print(krotka)

krotka1 = "radek", "tomek", "zenek"
print(krotka1)  # ('radek', 'tomek', 'zenek')
print(type(krotka1))  # <class 'tuple'>

krotka2 = ("Radek",)
print(type(krotka2))
temp = 36, 6
print(type(temp))  # <class 'tuple'>

print(len(krotka1))  # 3

# rozpakowanie tupli
a, *b = "radek", "tomek", "zenek"
print(a, b)  # radek, ['tomek', 'zenek']

# krotka[4] = 4  # TypeError: 'tuple' object does not support item assignment

# słownik - dane typu klucz-wartosc
# {"name" : "John"}
# odpowiednik jsona
oceny = {"Tomek": 4,
         "Radek": 5,
         "Agata": 5,
         "Zenek": 3
         }

print(oceny)  # {'Tomek': 4, 'Radek': 5, 'Agata': 5, 'Zenek': 3}
print(type(oceny))  # <class 'dict'>
print(oceny["Tomek"])  # wypisanie wartości z słownika dla danego klucza
# print(oceny["tomek"]) # KeyError: 'tomek'
print(oceny.get("Tomek"))  # 4
print(oceny.get("tomek"))  # None

print(oceny.keys())
print(oceny.values())
print(oceny.items())
# dict_keys(['Tomek', 'Radek', 'Agata', 'Zenek'])
# dict_values([4, 5, 5, 3])
# dict_items([('Tomek', 4), ('Radek', 5), ('Agata', 5), ('Zenek', 3)])

oceny['Agata'] = 6  # zmiana wartości dla klucza
print(oceny)  # {'Tomek': 4, 'Radek': 5, 'Agata': 6, 'Zenek': 3}

lista_oceny = [3, 4, 5, 6, 5, 5]
oceny['Tomek'] = lista_oceny
print(oceny)
# {'Tomek': [3, 4, 5, 6, 5, 5], 'Radek': 5, 'Agata': 6, 'Zenek': 3}

print(oceny['Tomek'])  # [3, 4, 5, 6, 5, 5]
print(oceny['Tomek'][0])  # 3

dictionary = {}  # pusty słownik
dict_pusty = dict()
print(dictionary)  # {}
print(dict_pusty)  # {}
print(type(dict_pusty))  # <class 'dict'> pusty słownik

# zbiór - set()
# przechowuje unikalne wartości
# nie zachowuje kolejności przy dodawaniu eleemntów
# nie posiada indeksu
lista = [45, 55, 66, 77, 45, 55, 66]
zbior1 = set(lista)
print(zbior1)  # {66, 77, 45, 55}

zbior1.add(100)
zbior1.add(102)
zbior1.add(105)
zbior1.add(77)
zbior1.add(55)
print(zbior1)  # {66, 100, 102, 105, 77, 45, 55}

zbior2 = {45, 55, 166, 177}

print(zbior1.difference(zbior2))  # {66, 100, 102, 105, 77}
print(zbior2.difference(zbior1))  # {177, 166}

print(zbior1 & zbior2)  # {45, 55}, część wspólna zbiorów
print(zbior1.intersection(zbior2))  # {45, 55}

pusty_zbior = set()  # tylko i wyłacznie słowko set()
print(pusty_zbior)  # set()
print(type(pusty_zbior))  # <class 'set'>

lista_ze_zbioru = list(zbior1)
print(lista_ze_zbioru)  # [66, 100, 102, 105, 77, 45, 55]

matrix = [[3, 4, 5], [6, 7, 8], [9, 10, 11]]
print(matrix)  # [[3, 4, 5], [6, 7, 8], [9, 10, 11]]

print(type(matrix))  # <class 'list'>
print(matrix[0][0])  # 3

# input() - zwraca str
a = int(input("Podaj  liczbę a"))
b = input("Podaj  liczbę b")
print(f"Suma liczb {a} + {b} = {a + float(b)}")
# Podaj  liczbę a45
# Podaj  liczbę b67
# Suma liczb 45 + 67 = 112.0
