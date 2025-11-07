# Mit "assistant" erinnert sich das Modell an vorherige Antworten, in diesem Fall an eine Zahl.

from litellm import completion
from typing import List, Dict

def generate_response(messages: List[Dict]) -> str:
    """Ruft das Sprachmodell auf und gibt die Textantwort zurück."""
    response = completion(
        model="openai/gpt-4o",
        messages=messages,
        max_tokens=200
    )
    return response.choices[0].message.content


# Erster Aufruf – das Modell soll sich eine Zahl merken
messages = [
    {"role": "system", "content": "You are a helpful assistant that remembers facts."},
    {"role": "user", "content": "My favorite number is 42. Schreibe diese Nummer in die Antwort, mehr nicht."}
]

response = generate_response(messages)
print("Antwort 1:", response)


# 💭 Zweiter Aufruf – dieselbe Unterhaltung mit 'assistant'-Gedächtnis
# Wir geben die vorige Antwort wieder zurück an das Modell
messages = [
    {"role": "system", "content": "You are a helpful assistant that remembers facts."},
    # {"role": "user", "content": f"My favorite number is {response}"},
    {"role": "assistant", "content": f"My favorite number is {response}"},  # hier wird die vorherige Modellantwort eingefügt
    {"role": "user", "content": "What is my favorite number?"}
]

response = generate_response(messages)
print("Antwort 2:", response)
