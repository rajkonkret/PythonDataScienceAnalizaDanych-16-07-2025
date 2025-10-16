# funkcja - wydzielony frgment kodu, można wywołąć w dowolnym momencie
# moze przyjmować argumenty

# dekalracja funkcji
# funkcja nie zwraca wyniku
def witaj():
    print("Witaj!")


# wywołanie funkcji
witaj()  # Witaj!


def ksero(tekst: str, ile: int):
    """
    Ta funkcja zwraca string pomnożony ilosc razy
    :param tekst:
    :param ile:
    :return:
    """
    return str(tekst) * ile  # zwraca wynik


print(ksero("Radek", 5))  # RadekRadekRadekRadekRadek

print(ksero(5, 5))  # "5" * 5, 55555
wynik = ksero("Radek", 5)
print(wynik)  # RadekRadekRadekRadekRadek


def ksero2(tekst: str, ile: int = 1):
    """
    Ta funkcja zwraca string pomnożony ilosc razy
    :param tekst:
    :param ile:
    :return:
    """
    return str(tekst) * ile  # zwraca wynik


print(ksero2("Radek"))  # Radek
print(ksero2("Radek", 2))  # RadekRadek


def ksero3(tekst: str = "tresc", ile: int = 1):
    """
    Ta funkcja zwraca string pomnożony ilosc razy
    :param tekst:
    :param ile:
    :return:
    """
    return str(tekst) * ile  # zwraca wynik


print(ksero3())  # tresc
print(ksero3(tekst="Radek", ile=3))  # RadekRadekRadek


def ile_razy(*ile, **co):
    print(ile)
    print(co)


# * argumenty pozycyjne
# ** argumentów nazwane, słownikowe
ile_razy((4, 5, 6))  # ((4, 5, 6),) -> ile
ile_razy(4, 5, 6, name="Radek", status="OK")  # ((4, 5, 6),) -> ile
# (4, 5, 6)
# {'name': 'Radek', 'status': 'OK'}
