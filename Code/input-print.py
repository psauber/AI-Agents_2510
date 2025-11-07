vorname = input("Wie heisst du zum Vorname? ")
nachname = input("Wie ist dein Nachname? ")
print("Dein voller Name ist:", vorname, nachname, " - willkommen bei Python." )

projekt = input("An welchem Projekt hast du gearbeitet? ")
stundenlohn = float(input(f"Wie viel verdienst du pro Stunde in CHF? ")) # Umwandlung in float, da input() immer einen String zurückgibt
arbeitsstunden = float(input(f"Wie viele Stunden hast Du auf dem Projekt {projekt} gearbeitet? ")) # f-String für Variable im Prompt, da input() nur eine Variable aufnehmen kann.
honorar = stundenlohn * arbeitsstunden

print("Dein Honorar für das Projekt", projekt, "beträgt:", honorar, "CHF.")
spesen = float(input(f"Wie hoch sind deine Spesen in CHF für das Projekt {projekt} gewesen? "))
gesamtabrechnung = honorar + spesen

print("Deine Gesamtabrechnung für das Projekt", projekt, "beträgt:", gesamtabrechnung, "CHF.")

# print() = kann mehrere Argumente haben
# input() = darf nur einen String haben → also f-String nutzen, wenn du Variablen einbauen willst
    # Python ersetzt {projekt} durch den Wert der Variablen, noch bevor input() ausgeführt wird.
    # So erhält input() wieder nur einen String → und das funktioniert.


