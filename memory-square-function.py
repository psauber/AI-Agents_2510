# Mit "assistant" erinnert sich das Modell an vorherige Antworten,
# hier an eine einfache Rechenfunktion.

from litellm import completion
from typing import List, Dict

def generate_response(messages: List[Dict]) -> str:
    """Ruft das Sprachmodell auf und gibt die Textantwort zurück."""
    response = completion(
        model="openai/gpt-4o",
        messages=messages,
        max_tokens=300
    )
    return response.choices[0].message.content


# 🧮 Erster Aufruf – Modell soll eine einfache Funktion schreiben
messages = [
   {"role": "system", "content": "You are an expert software engineer that writes clean and simple Python code."},
   {"role": "user", "content": "Write a Python function that calculates the square of a number."}
]

response = generate_response(messages)
print("Antwort 1:", response)


# 💭 Zweiter Aufruf – das Modell bekommt seine eigene Antwort zurück (Memory)
# und wird gebeten, die Funktion mit Dokumentation zu erweitern.
messages = [
   {"role": "system", "content": "You are an expert software engineer that writes clean and simple Python code."},
   {"role": "user", "content": "Write a Python function that calculates the square of a number."},
   {"role": "assistant", "content": response},  # vorherige Antwort (Memory)
   {"role": "user", "content": "Update the function to include a docstring and a type hint."} # docstring hält die Funktionserklärung und type hint gibt den Datentyp an
]

response = generate_response(messages)
print("Antwort 2:", response)
