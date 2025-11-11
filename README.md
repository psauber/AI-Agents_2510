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

## 🚀🚀🚀 Detaillierte Beschreibung der Fähigkeiten eines Agents 🚀🚀🚀

Each of the “tools” in the system prompt correspond to a function in the code. The agent is going to choose what function to execute and when. Moreover, it is going to decide the parameters that are provided to the functions.
The agent is not creating the functions at this point; it is orchestrating their behavior. This means that the logic for how each tool operates is predefined in the code, and the agent focuses on selecting the right tool for the job and providing the correct input to that tool.
Because agents can adapt as the loop progresses, they can dynamically decide which tool to use based on the current context and task requirements. This ability allows the agent to adjust its behavior as new information becomes available, making it more flexible and responsive to the user’s input.
For example, if the user asks the agent to read the contents of a specific file, the agent will first use the list_files tool to identify the available files. Then, based on the result, it will determine whether to proceed with the read_file tool or respond with an error if the file does not exist. The agent evaluates each step iteratively, ensuring its actions are informed by the current state of the environment.
This orchestration process, driven by the agent rules and the tools available, showcases the power of combining pre-defined functions with adaptive decision-making. By allowing the agent to focus on what to do rather than how to do it, we create a system that leverages the LLM for high-level reasoning while relying on well-defined code for execution.
This separation of reasoning and execution is what makes the agent loop so powerful—it creates a modular, extensible framework that can handle increasingly complex tasks without rewriting the underlying tools.
Additionally, the agent loop eliminates much of the “glue code”* traditionally required to tie these fundamental functions together. Instead of hardcoding workflows, the agent dynamically decides the sequence of actions needed to achieve a task, effectively realizing a program on top of its components. This dynamic nature enables the agent to combine its tools in ways that would typically require custom logic, making it far more versatile and capable of addressing a broader range of use cases without additional development overhead.

*Der Agent Loop ersetzt oder automatisiert viel von dem "glue code" Kleber-Code, den man früher manuell schreiben musste, um die einzelnen Funktionen (wie Denken, Handeln, Gedächtnis) zu verbinden.

```python
