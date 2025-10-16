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
