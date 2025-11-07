# 🧠 AI Agents in Python — Lernprojekt

Dieses Repository begleitet meinen Coursera-Kurs **„AI Agents in Python“** und meine eigenen Experimente mit Large Language Models (LLMs).  
Ich dokumentiere hier, wie man mit **Python**, **litellm** und der **OpenAI API** einfache AI-Agenten aufbaut, testet und erweitert.

---

## 🎯 Ziel des Projekts
Das Ziel ist, die Funktionsweise von AI Agents und LLM-Prompts praktisch zu verstehen:

- Wie kommunizieren Modelle über `messages` (system / user / assistant)?
- Wie funktioniert ein einfaches „Memory“ durch Kontext?
- Wie kann man den Output von Modellen (z. B. generierten Code) weiterverarbeiten?
- Wie lassen sich API-Aufrufe in Python strukturieren?

---

## ⚙️ Technische Grundlage

**Programmiersprache:** Python 3.14  
**Bibliotheken:**  
- [`litellm`](https://github.com/BerriAI/litellm) – Wrapper für OpenAI-kompatible Modelle  
- [`python-dotenv`](https://pypi.org/project/python-dotenv/) – Laden von API-Keys  
- [`requests`](https://pypi.org/project/requests/) – HTTP-Kommunikation (optional)

---

## 📘 Beispiel: Einfacher Agent mit Memory

from litellm import completion

messages = [
    {"role": "system", "content": "You are a helpful assistant that remembers facts."},
    {"role": "user", "content": "My favorite number is 42."},
    {"role": "assistant", "content": "Got it, your favorite number is 42."},
    {"role": "user", "content": "What is my favorite number?"}
]

response = completion(model="openai/gpt-4o", messages=messages)
print(response.choices[0].message.content)

🧩 Themen, die ich hier erforsche
Aufbau von Prompts mit system, user und assistant
Nutzung von litellm zur Vereinfachung von OpenAI-Aufrufen
Simulation von Agent-Memory über Nachrichtenkontext
Generierung und Erweiterung von Python-Code durch LLMs
Verständnis von Tokens, Type Hints, Docstrings und Escape-Sequenzen

🚀 Nächste Schritte
Erweiterung der Agenten um Tool-Nutzung (Funktionen, Dateien, APIs)
Verbindung mehrerer Agents zu kooperativen Aufgaben
Test von Open-Source-Modellen (z. B. Mistral, Llama 3) über litellm

🧑‍💻 Autor
Philipp Sauber
Dieses Projekt ist Teil meines persönlichen Lernpfads rund um Python, KI und Agenten-Architekturen.

📜 Lizenz
Dieses Repository dient Lern- und Demonstrationszwecken.
Alle Beispiele dürfen frei verwendet und angepasst werden.

```python
