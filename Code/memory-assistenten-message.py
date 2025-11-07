# Memory mit Assistenten importieren

# Importiere die Funktion 'completion' aus der Bibliothek 'litellm'.
# Diese Funktion wird verwendet, um eine Anfrage an ein Sprachmodell (z. B. GPT-4o) zu schicken.
from litellm import completion

# Importiere Typdefinitionen, um klar zu machen, dass 'messages' eine Liste von Wörterbüchern (Dicts) ist.
from typing import List, Dict

# Definiere eine Funktion, die das Sprachmodell aufruft und den Text der Antwort zurückgibt.
def generate_response(messages: List[Dict]) -> str:
    """Ruft ein Sprachmodell (LLM) auf und gibt dessen Antworttext zurück."""
    response = completion(
        model="openai/gpt-4o",   # Modellname: GPT-4o (OpenAI)
        messages=messages,       # Nachrichten im Chat-Format (Liste mit Rollen und Inhalten)
        max_tokens=1024          # Maximale Länge der Antwort in Tokens
            )
    return response.choices[0].message.content
# Erste Aufruf ohne Gedächtnis. die Antwort wird später als Gedächtnis genutzt und enthält die Funktion zum Vertauschen von Schlüssel und Wert in einem Dictionary
messages = [
   {"role": "system", "content": "You are an expert software engineer that prefers functional programming."},
   {"role": "user", "content": "Write a function to swap the keys and values in a dictionary."}
]

response = generate_response(messages)
print(response)

# Nachrichtenverlauf definieren (System, User, Assistant, User)
messages = [
   {"role": "system", "content": "You are an expert software engineer that prefers functional programming."},  # Modellrolle: Experte für funktionale Programmierung
   {"role": "user", "content": "Write a function to swap the keys and values in a dictionary."},  # Benutzer fragt nach einer Funktion
   {"role": "assistant", "content": response},  # Antwort des Modells aus vorherigem Schritt (Gedächtnis)
   {"role": "user", "content": "Update the function to include documentation."}  # Benutzer fordert aktualisierte Version mit Doku
]

response = generate_response(messages)  # Modell (=LLM) aufrufen (LLM Anfrage schicken) mit erweitertem Chatverlauf
print(response)  # Antwort (aktualisierter Code) ausgeben