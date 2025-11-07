# Datentypen in Python und Umwandlung zwischen Typen
response = {"status": "ok", "code": 200} # definieren eines Datentyps Dictionaries

# Wenn du das einfach printest:
print(response)  # -> {'status': 'ok', 'code': 200}

response_str = str(response) # umwandeln in String
print(type(response_str)) # type gibt den Datentyp zurück

x = 42
print(type(x))        # <class 'int'>

x = "Hallo"
print(type(x))        # <class 'str'>

x = [1, 2, 3]
print(type(x))        # <class 'list'>

# ================================================
# 🐍 Übersicht der grundlegenden Datentypen in Python
# ================================================
# 🔢 Zahlen (Numeric Types)
# int      -> Ganze Zahl, z. B. 42
# float    -> Kommazahl, z. B. 3.14
# complex  -> Komplexe Zahl, z. B. 2 + 3j

# 🔤 Text
# str      -> Zeichenkette (String), z. B. "Hallo Welt"

# ✅ Boolesche WerteBi
# bool     -> Wahr/Falsch, True oder False

# 📦 Sequenzen (geordnete Sammlungen)
# list     -> Veränderliste, z. B. [1, 2, 3]
# tuple    -> Unveränderlich, z. B. (1, 2, 3)
# range    -> Zahlenbereich, z. B. range(5) = 0, 1, 2, 3, 4 oder range(1, 6) = 1, 2, 3, 4, 5 oder range(2, 11, 2) = 2, 4, 6, 8, 10

# 📚 Sets (ungeordnete Sammlungen ohne Duplikate)
# set      -> z. B. {1, 2, 3}
# frozenset-> Unveränderliche Variante von set

# 🔑 Dictionaries (Schlüssel-Wert-Paare)
# dict     -> z. B. {"name": "Philipp", "alter": 54}

# 🪣 NoneType
# None     -> Platzhalter für "keinen Wert", z. B. wenn eine Funktion nichts zurückgibt

# ================================================
# Zusätzliche/abgeleitete Typen (aus Modulen):
# bytes, bytearray, memoryview -> Für Binärdaten
# datetime, date, time         -> Aus dem datetime-Modul
# Decimal, Fraction            -> Aus dem decimal- bzw. fractions-Modul
# ================================================
