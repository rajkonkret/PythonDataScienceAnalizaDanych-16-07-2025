# https://kariera.comarch.pl/blog/clean-code-15-krokow-do-stworzenia-czystego-kodu/
# https://peps.python.org/pep-0008/ - zasady formatowania kodu
# snake_case
import sys

print("Radek")
print('Radek')
# Radek
# Radek

# ctrl / - komentarz
# print('Radek")
#   File "C:\Users\CSComarch\PycharmProjects\PythonDataScienceAnalizaDanych-16-07-2025\day1\pierwszy.py", line 10
#     print('Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 10)
#
# Process finished with exit code 1
# ctrl alt l - formatowanie

# typy danych
# type()
print(type("Radek"))  # <class 'str'>, typ tekstowy

print("39" + "14")  # 3914, łaczenie tekstów, konkatencja
print(39 + 14)  # 53

print(type(39))  # <class 'int'>, integer, liczby całkowite
print(sys.int_info)

# sys.int_info(bits_per_digit=30,
# sizeof_digit=4,
# default_max_str_digits=4300,
# str_digits_check_threshold=640)

# zmienna - pudełko na dane

# typowanie dynamiczne
name = 'Radek'
print(name)
print(type(name))  # <class 'str'>

name = 90
print(name)  # 90
print(type(name))  # <class 'int'>

# podpowiedzi typów
name: str = 90
print(name)  # 90

# mypy
# pip install mypy
# mypy main.py

tekst = "Witaj wiecie"
print(tekst)
print(type(tekst))

# teksty niemutowalne
# """ Return a copy of the string converted to uppercase. """
tekst.upper()
print(tekst)  # Witaj wiecie
print(tekst.upper())  # WITAJ WIECIE
zmienna = tekst.upper()
print(zmienna)  # WITAJ WIECIE

print(tekst.lower())  # witaj wiecie
print(tekst.capitalize())  # Witaj wiecie

# https://naukapythona.com.pl/
zmienna1 = "GROSS"
zmienna2 = "groẞ"

print(zmienna1.lower() == zmienna2.lower())  # False
# ctrl d - powielenie linii
print(zmienna1.casefold() == zmienna2.casefold())  # True

# != różne
print(1 != 8)  # True
# typy logiczne, boolean -> True, False

# rzutowanie - zamiana typów
print(int("39"))  # zamiana na int, 39
print(str(39))  # zamiana str

print(int(True))  # 1
print(int(False))  # 0

print(bool(1))  # True
print(bool(0))  # False

print(bool(100))  # True
print(bool("radek"))  # True

print(bool(""))  # False

# None - nie wiem, stan nieokreslony, odpowiednik null
print(bool(None))  # False

temp = 36.6
print(type(temp))  # <class 'float'>, zmiennoprzecinkowe
print(temp)  # 36.6
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024,
# max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
# min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

# float - bład zaokaglenia
print(0.1 + 0.9)  # 1.0
print(0.1 + 0.7)  # 0.7999999999999999
print(0.1 + 0.2)  # 0.30000000000000004
#  For example, in a floating-point arithmetic with five base-ten digits,
#  the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
# decimal - ominięcie problemu zaokrąglenia

# f - string format
print(f"Nazywam się {name}, Dzień dobry")
# Nazywam się 90, Dzień dobry
print("Nazywam się {}.".format(name))  # Nazywam się 90.

liczba = 3.900001
print(f"Wersja pythona: {liczba}")  # Wersja pythona: 3.900001
print(f"Wersja pythona: {liczba:.2f}")  # Wersja pythona: 3.90 - zaokrągla

print(f"""Tekst
    wielolinijkowy""")
# "Tekst
#     wielolinijkowy"

"""Komentarz
    wielolinijkowy - dokumentacja"""
print(print.__doc__)
