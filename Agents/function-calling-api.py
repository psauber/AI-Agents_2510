import json
import os
from typing import List

from litellm import completion

def list_files() -> List[str]:
    """List files in the current directory."""
    return os.listdir(".")

def read_file(file_name: str) -> str:
    """Read a file's contents."""
    try:
        with open(file_name, "r") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: {file_name} not found."
    except Exception as e:
        return f"Error: {str(e)}"


tool_functions = { # Mapping Tool-Namen zu Funktionen für späteren Aufruf
    "list_files": list_files,
    "read_file": read_file
}

tools = [ # Eckige Klammer, da es eine Liste von Tools ist und somit ein Array
    {
        "type": "function", # Erste Tool ist eine Funktion
        "function": {
            "name": "list_files",
            "description": "Returns a list of files in the directory.",
            "parameters": {"type": "object", "properties": {}, "required": []} # Keine Parameter da "properties" und "required" leer sind
        }
    },
    {
        "type": "function", # Zweites Tool ist ebenfalls eine Funktion
        "function": {
            "name": "read_file",
            "description": "Reads the content of a specified file in the directory.",
            "parameters": {
                "type": "object",
                "properties": {"file_name": {"type": "string"}}, # Ein Parameter "file_name" vom Typ String
                "required": ["file_name"]
            }
        }
    }
]

# Our rules are simplified since we don't have to worry about getting a specific output format
agent_rules = [{ # Definiere die Regeln für den Agenten (System-Prompt)
    "role": "system",
    "content": """
You are an AI agent that can perform tasks by using available tools. 

If a user asks about files, documents, or content, first list the files before reading them.
"""
}]

user_task = input("What would you like me to do? ") # User-Eingabe für die Aufgabe des Agenten

memory = [{"role": "user", "content": user_task}] # Speichere die User-Aufgabe im Memory

messages = agent_rules + memory # Kombiniere die Agenten-Regeln mit dem Memory zu den Messages

# Hier ist die Liste der Tools, die du aufrufen darfst. Wähle eines davon und gib einen Tool-Call zurück.
response = completion( # Anfrage an das LLM mit Tools
    model="openai/gpt-4o", # 
    messages=messages, # Messages inklusive System-Prompt und User-Input
    tools=tools, # Liste der verfügbaren Tools!!!
    max_tokens=1024 # Maximale Token-Anzahl für die Antwort
)

# Extract the tool call from the response, note we don't have to parse now!
tool = response.choices[0].message.tool_calls[0] # Extrahiere den Tool-Call aus der LLM-Antwort
tool_name = tool.function.name # Name des ausgewählten Tools
tool_args = json.loads(tool.function.arguments) # Argumente des Tools als Dictionary
result = tool_functions[tool_name](**tool_args) # Rufe die entsprechende Funktion mit den Argumenten auf

print(f"Tool Name: {tool_name}")
print(f"Tool Arguments: {tool_args}")
print(f"Result: {result}")