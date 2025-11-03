# Importiere die Funktion 'completion' aus der Bibliothek 'litellm'.
# Diese Funktion wird verwendet, um eine Anfrage an ein Sprachmodell (z. B. GPT-4o) zu schicken.
from litellm import completion

# Importiere Typdefinitionen, um klar zu machen, dass 'messages' eine Liste von Wörterbüchern (Dicts) ist.
from typing import List, Dict

# Importiere das Modul 'json', um Python-Daten in JSON-Text umzuwandeln.
import json

# Definiere eine Funktion, die das Sprachmodell aufruft und den Text der Antwort zurückgibt.
def generate_response(messages: List[Dict]) -> str:
    """Ruft ein Sprachmodell (LLM) auf und gibt dessen Antworttext zurück."""
    response = completion(
        model="openai/gpt-4o",   # Modellname: GPT-4o (OpenAI)
        messages=messages,       # Nachrichten im Chat-Format (Liste mit Rollen und Inhalten)
        max_tokens=1024          # Maximale Länge der Antwort in Tokens
    )
    # 'response.choices[0].message.content' enthält den Text der ersten Modellantwort.
    return response.choices[0].message.content

# Dieses Dictionary beschreibt, was das Modell programmieren soll.
# Es enthält Name, Beschreibung und Parameter einer Funktion.
code_spec = {
    'name': 'swap_keys_values',               # Funktionsname
    'description': 'Vertauscht Schlüssel und Werte in einem Dictionary.',  # Beschreibung
    'params': {
        'd': 'Ein Dictionary mit eindeutigen Werten.'                      # Parameterbeschreibung
    },
}

# Die Nachrichten für das Sprachmodell werden im Chat-Format definiert:
messages = [
    # 1️⃣ Systemrolle: beschreibt, wie sich das Modell verhalten soll.
    {"role": "system",
     "content": "You are an expert software engineer that writes clean functional code. "
                "You always document your functions."},

    # 2️⃣ Benutzerrolle: hier kommt die eigentliche Aufgabe.
    # Mit json.dumps() wird das Python-Dictionary 'code_spec' in Textform (JSON) übergeben.
    {"role": "user", "content": f"Please implement: {json.dumps(code_spec)}"}
]

# Rufe das Modell auf und speichere die Antwort in 'response'.
response = generate_response(messages)

# Gib die Antwort (also den generierten Code) in der Konsole aus.
print(response)


"""Kurz erklärt:
system → beschreibt die Persönlichkeit oder Rolle des Modells („Experte für sauberen Code“).
user → enthält die eigentliche Programmieraufgabe.
completion() → ruft das Modell auf, ähnlich wie openai.ChatCompletion.create() bei der OpenAI-API.
max_tokens → begrenzt die Länge der Antwort."""