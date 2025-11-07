
import math

def ziehe_quadratwurzel(num):
    """
    Berechnet die Quadratwurzel einer nicht-negativen ganzen Zahl.

    Diese Funktion nimmt eine nicht-negative ganze Zahl als Eingabewert entgegen 
    und berechnet deren Quadratwurzel. Bei einer negativen Eingabe wird 
    eine Fehlermeldung ausgegeben.

    Args:
    - num (int): Die Zahl, aus der die Quadratwurzel gezogen werden soll. 
      Diese Zahl muss nicht-negativ sein.

    Returns:
    - float: Die Quadratwurzel der übergebenen Zahl.

    Raises:
    - ValueError: Falls die Eingabezahl negativ ist, da die Quadratwurzel einer negativen
      Zahl im Bereich der reellen Zahlen nicht definiert ist.

    Beispiele:
    - ziehe_quadratwurzel(4) gibt 2.0 zurück.
    - ziehe_quadratwurzel(9) gibt 3.0 zurück.

    Randfälle:
    - Fördert eine Ausnahme bei einer negativen Eingabe, z.B. ziehe_quadratwurzel(-1).
    - Gibt 0.0 für die Eingabe 0 zurück.
    """
    if num < 0:
        raise ValueError("Die Zahl darf nicht negativ sein, um eine reale Quadratwurzel zu ziehen.")
    
    return math.sqrt(num)

# Beispielverwendung:
def main():
    try:
        eingabe = input("Gib eine Zahl ein (z.B. 16): ")
        # Erlaubt Ganzzahlen und Kommazahlen; float() wirft ValueError bei ungültiger Eingabe
        num = float(eingabe)
        ergebnis = ziehe_quadratwurzel(num)
        print(ergebnis)
    except ValueError as e:
        # Deckt sowohl ungültige Eingabe (float-Konvertierung) als auch negative Zahlen durch die Funktion ab
        print(f"Fehler: {e}")
    except TypeError as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    main()

import unittest
import math

def ziehe_quadratwurzel(num):
    """
    Berechnet die Quadratwurzel einer nicht-negativen ganzen Zahl.
    """
    if num < 0:
        raise ValueError("Die Zahl muss nicht-negativ sein, um eine reale Quadratwurzel zu ziehen.")
    return math.sqrt(num)

class TestZieheQuadratwurzel(unittest.TestCase):
    
    def test_basic_functionality(self):
        self.assertEqual(ziehe_quadratwurzel(4), 2.0) # self.assertEqual testet, ob der erste Wert dem zweiten entspricht. self.assertEqual ist eine Methode der unittest.TestCase Klasse und erwartet zwei Argumente: den tatsächlichen Wert und den erwarteten Wert.
        self.assertEqual(ziehe_quadratwurzel(9), 3.0)
        self.assertEqual(ziehe_quadratwurzel(16), 4.0)
    
    def test_edge_cases(self):
        self.assertEqual(ziehe_quadratwurzel(0), 0.0)
        self.assertAlmostEqual(ziehe_quadratwurzel(2), math.sqrt(2))
    
    def test_error_cases(self):
        with self.assertRaises(ValueError):
            ziehe_quadratwurzel(-1)
        
        with self.assertRaises(ValueError):
            ziehe_quadratwurzel(-20)
    
    def test_large_numbers(self):
        self.assertEqual(ziehe_quadratwurzel(1000000), 1000.0)
        self.assertEqual(ziehe_quadratwurzel(123456789), math.sqrt(123456789))
    
    def test_type_errors(self):
    # Beispiel: Testet, ob ein TypeError ausgelöst wird, wenn kein int/float übergeben wird
        with self.assertRaises(TypeError):
            ziehe_quadratwurzel("abc")
        with self.assertRaises(TypeError):
            ziehe_quadratwurzel(None)