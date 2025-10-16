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
