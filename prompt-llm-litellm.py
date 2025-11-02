# Importiere die Funktion 'completion' aus dem Modul 'litellm'
# → 'litellm' ist eine leichtgewichtige Bibliothek, um Sprachmodelle (LLMs) wie GPT zu verwenden.
from litellm import completion

# Importiere Typdefinitionen, um Parameter klarer zu dokumentieren
# List und Dict werden für die Typannotationen der Nachrichten verwendet.
from typing import List, Dict


# Definiere eine Funktion, die mit einem LLM (Large Language Model) kommuniziert.
# Sie nimmt eine Liste von Nachrichten im Chat-Format entgegen und gibt die Antwort als Text zurück.
def generate_response(messages: List[Dict]) -> str:
    """Call LLM to get response"""

    # Aufruf des Modells über die LiteLLM-API.
    # - model: welches Modell verwendet werden soll (hier: GPT-4o)
    # - messages: Liste von Chat-Nachrichten mit Rollen (system, user, assistant)
    # - max_tokens: maximale Länge der Antwort
    response = completion(
        model="openai/gpt-4o",
        messages=messages,
        max_tokens=1024
    )

    # Die Antwortstruktur enthält mehrere Wahlmöglichkeiten (choices),
    # wir greifen hier auf die erste zu ([0]).
    # Danach holen wir uns den generierten Text (message.content).
    return response.choices[0].message.content


# Beispielkonversation für das Modell - "role" beschreibt die Art der Nachricht:
# - Die "system"-Nachricht beschreibt das Verhalten oder die Rolle des Modells.
# - Die "user"-Nachricht enthält die eigentliche Frage oder Aufgabe.
messages = [
    {"role": "system", "content": "You are an expert software engineer that prefers functional programming."},
    {"role": "user", "content": "Write a function to swap the keys and values in a dictionary."}
]

""" messages = [
    {"role": "system", "content": "Du bist ein Verkäufter von Autos"},
    {"role": "user", "content": "Was sagst Du einem Ferrari-Fan, wenn Du ihm ein EV verkaufen willst?"}
] """

# Der eigentliche Funktionsaufruf – sendet die Nachrichten an das Modell
# und speichert die Antwort in der Variable 'response'.
response = generate_response(messages)

# Ausgabe der vom Modell generierten Antwort auf der Konsole.
print(response)
