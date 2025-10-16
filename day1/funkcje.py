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

