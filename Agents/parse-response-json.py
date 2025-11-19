"""Analysiert (parst) die Antwort des Sprachmodells (LLM) und wandelt sie in ein strukturiertes Aktions-Dictionary um."""

def parse_action(response: str) -> Dict:
    
    try:
        # Extrahiere den Teil der Antwort, der den JSON-Code enthält.
        # Viele Modelle liefern Antworten im Markdown-Format, z. B.:
        # ```action
        # {"tool_name": "list_files", "args": {}}
        # ```
        # Diese Hilfsfunktion holt den Inhalt zwischen den Markierungen ```action ... ``` heraus,
        # damit nur der JSON-Text übrig bleibt.
        response = extract_markdown_block(response, "action")

        # Wandle den JSON-Text in ein Python-Dictionary um.
        # Beispiel: '{"tool_name": "read_file", "args": {"file_name": "notes.txt"}}'
        # wird zu {'tool_name': 'read_file', 'args': {'file_name': 'notes.txt'}}
        response_json = json.loads(response)

        # Prüfe, ob die beiden erforderlichen Schlüssel vorhanden sind:
        # "tool_name" → Name des Werkzeugs (z. B. list_files, read_file)
        # "args" → Argumente für das Tool (z. B. {"file_name": "notes.txt"})
        if "tool_name" in response_json and "args" in response_json:
            # Wenn alles korrekt ist, wird das Dictionary zurückgegeben, damit der Agent weiß, welches Tool er ausführen soll.
            return response_json
        else:
            # Wenn die Struktur nicht stimmt, gib eine standardisierte Fehlermeldung zurück, damit das Modell weiß, dass es im JSON-Format antworten muss.
            return {"tool_name": "error", "args": {"message": "You must respond with a JSON tool invocation."}}

    except json.JSONDecodeError:
        # Falls das Parsen des JSON-Strings fehlschlägt (z. B. wegen Tippfehlern oder ungültigem Format),
        # gib ebenfalls eine Fehlerstruktur zurück, die auf das Problem hinweist.
        return {"tool_name": "error", "args": {"message": "Invalid JSON response. You must respond with a JSON tool invocation."}}
