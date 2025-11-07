früchte = ["Apfel", "Banane", "Kirsche"] # frucht nimmt die Werte von Früchte an — zum Beispiel, um über eine Liste, Zahlenreihe oder Zeichen in einem String zu iterieren.
for frucht in früchte:  # "frucht" ist ein Platzhalter, der bei jedem Durchlauf einen neuen Wert annimmt.
    print("Ich mag", frucht)

input("Drücke Enter, um mit der nächsten Schleife fortzufahren...")

# range(2, 11, 2) erzeugt die geraden Zahlen von 2 bis 10
for zahl in range(2, 11, 2):  # "zahl" ist ein Platzhalter, der bei jedem Durchlauf den nächsten Wert von range() annimmt.
    print("Die Zahl ist:", zahl)

# range(5) erzeugt die Zahlen 0 bis 4
#     for zahl in range(5):  # "zahl" ist ein Platzhalter, der bei jedem Durchlauf einen neuen Wert annimmt.
#     print("Die Zahl ist:", zahl)

# input("Drücke Enter, um mit der nächsten Schleife fortzufahren...")

# range(1, 6) erzeugt die Zahlen 1 bis 5
# for zahl in range(1, 6):  # "zahl" ist ein Platzhalter, der bei jedem Durchlauf einen neuen Wert annimmt.
#     print("Die Zahl ist:", zahl)

# input("Drücke Enter, um mit der nächsten Schleife fortzufahren...")

# Wenn du input() nicht in eine Variable speicherst, passiert Folgendes:
# Der Benutzer gibt etwas ein (oder drückt einfach Enter). Python wartet, bis Enter gedrückt wurde. Das Programm läuft dann einfach weiter — egal, was eingegeben wurde.

# ----------------------------------------------------------------
input("Drücke Enter, um mit der nächsten Schleife fortzufahren...") 

zahlen = [10, 20, 30] # Eine Liste mit Zahlen erstellen
summe = 0 # Variable "summe" initialisieren (Startwert = 0)

# for-loop: geht jede Zahl in der Liste "zahlen" der Reihe nach durch
for z in zahlen:  # "z" ist ein Platzhalter, der bei jedem Durchlauf den nächsten Wert aus der Liste zahlen[] annimmt
    summe = summe + z  # aktuelle Zahl "z" zur bisherigen Summe addieren
    print("Zwischensumme:", summe, "& aktuelle Zahl in Liste:", z)  # Zwischensumme nach jeder Addition ausgeben

print("Die Gesamtsumme ist:", summe) # Nach der Schleife: Gesamtsumme ausgeben

# ----------------------------------------------------------------
# Werte aus CSV-Datei lesen und mit for-Loop verarbeiten - liegt im selben Ordner wie dieses Script
import csv  # Modul zum Lesen von CSV-Dateien

# Datei öffnen (read-Modus)
with open("personen-liste.csv", "r", encoding="latin1") as file:  # r steht für "read" (lesen) und latin1 wegen Umlauten
    reader = csv.reader(file, delimiter=";")  # CSV-Reader erzeugen, delimiter auf ; setzen
    next(reader)  # Überspringt die Kopfzeile ("Vorname, Name,Alter,Wohnort")

    # for-loop über jede Zeile in der CSV-Datei
    for zeile in reader:  # "zeile" ist eine Liste mit den Werten der jeweiligen Zeile. For geht über jede Zeile der CSV-Datei.
        vorname = zeile[0] # [0] steht für die erste Spalte
        name = zeile[1]
        alter = zeile[2]
        wohnort = zeile[3]

        print(f"{vorname} {name} ist {alter} Jahre alt und wohnt in {wohnort}.")
