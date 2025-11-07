# 🔁 Der "Agent Loop" – Hauptschleife des AI-Agenten
# Diese Schleife wird wiederholt ausgeführt, bis eine Abbruchbedingung erreicht ist.
# Sie simuliert, wie ein KI-Agent denkt, handelt und sein Gedächtnis aktualisiert.

while iterations < max_iterations:

    # 1️⃣ Prompt erstellen: Agenten-Regeln + bisheriges Gedächtnis kombinieren.
    # 'agent_rules' enthält die fixen Verhaltensregeln (z. B. "Du bist ein hilfreicher Assistent"),
    # 'memory' enthält den bisherigen Gesprächsverlauf oder Kontext.
    prompt = agent_rules + memory

    # 2️⃣ Antwort generieren / vom Sprachmodell (LLM) erzeugen
    print("Agent thinking...")  # Statusausgabe für den Benutzer
    response = generate_response(prompt)  # Anfrage an das LLM (Large Language Model)
    print(f"Agent response: {response}")  # Ausgabe der Antwort (z. B. welche Aktion es vorschlägt)

    # 3️⃣ Antwort analysieren, um herauszufinden, welche Aktion ausgeführt werden soll
    # 'parse_action' ist eine Hilfsfunktion, die den Text der LLM-Antwort
    # in eine strukturierte Aktion (Dictionary) umwandelt.
    action = parse_action(response)

    # Variable zum Speichern des Aktionsergebnisses
    result = "Action executed"

    # 4️⃣ Aktion ausführen: Mögliche Aktionen prüfen und ausführen:
    # Das LLM entscheidet, welches "Tool" (Werkzeug/Funktion) der Agent verwenden soll.

    # Wenn das Modell "list_files" auswählt → alle Dateien im aktuellen Verzeichnis auflisten.
    if action["tool_name"] == "list_files":
        result = {"result": list_files()}

    # Wenn "read_file" → Dateiinhalt lesen, Dateiname wird aus den Argumenten geholt.
    elif action["tool_name"] == "read_file":
        result = {"result": read_file(action["args"]["file_name"])}

    # Wenn ein Fehler erkannt wurde → Fehlermeldung zurückgeben.
    elif action["tool_name"] == "error":
        result = {"error": action["args"]["message"]}

    # Wenn das Modell signalisiert, dass der Agent seine Arbeit beenden soll → Schleife abbrechen.
    elif action["tool_name"] == "terminate":
        print(action["args"]["message"])  # Nachricht anzeigen (z. B. "Task completed.")
        break

    # Wenn der Aktionsname unbekannt ist → Fehler melden.
    else:
        result = {"error": "Unknown action: " + action["tool_name"]}

    # Ergebnis der ausgeführten Aktion anzeigen (zur Kontrolle oder Debugging)
    print(f"Action result: {result}")

    # 5️⃣ Ergebnis in Zeichenfolge konvertieren: Gedächtnis (memory) aktualisieren:
    # Der Agent merkt sich, was er gesagt hat (assistant)
    # und was als Ergebnis (user input) zurückkam.
    # So kann das Modell später darauf Bezug nehmen.
    memory.extend([
        {"role": "assistant", "content": response},
        {"role": "user", "content": json.dumps(result)}  # Ergebnis als JSON-Text speichern
    ])

    # 6️⃣ Schleife fortsetzen: Prüfen, ob das Modell das Ende signalisiert hat
    # (z. B. Tool "terminate" wurde aufgerufen)
    if action["tool_name"] == "terminate":
        break

    # 7️⃣ Zähler erhöhen, um Endlosschleifen zu vermeiden 
    iterations += 1