import json
import os
from typing import List

from litellm import completion

# Definition der Funktionen, die als Tools verwendet werden können
def list_files() -> List[str]: # Funktion 1 zum Auflisten von Dateien
    """List files in the current directory."""
    return os.listdir(".")

def read_file(file_name: str) -> str: # Funktion 2 zum Lesen von Dateien
    """Read a file's contents."""
    try:
        with open(file_name, "r") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: {file_name} not found."
    except Exception as e:
        return f"Error: {str(e)}"

def terminate(message: str) -> None: # Funktion 3 zum Beenden des Agenten
    """Terminate the agent loop and provide a summary message."""
    print(f"Termination message: {message}")

# Mapping Tool-Namen zu Funktionen für späteren Aufruf
tool_functions = {
    "list_files": list_files,
    "read_file": read_file,
    "terminate": terminate
}
# Definition der verfügbaren Tools für den Agenten
tools = [ # Eckige Klammer, da es eine Liste von Tools ist und somit ein Array
    {
        "type": "function", # Erste Tool ist eine Funktion
        "function": {
            "name": "list_files",
            "description": "Returns a list of files in the directory.",
            "parameters": {"type": "object", "properties": {}, "required": []}
        }
    },
    {
        "type": "function", # Zweites Tool ist ebenfalls eine Funktion
        "function": {
            "name": "read_file",
            "description": "Reads the content of a specified file in the directory.",
            "parameters": {
                "type": "object",
                "properties": {"file_name": {"type": "string"}},
                "required": ["file_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "terminate",
            "description": "Terminates the conversation. No further actions or interactions are possible after this. Prints the provided message for the user.",
            "parameters": {
                "type": "object",
                "properties": {
                    "message": {"type": "string"},
                },
                "required": ["message"]
            }
        }
    }
]
# Definiere die Regeln für den Agenten (System-Prompt)
agent_rules = [{
    "role": "system",
    "content": """
You are an AI agent that can perform tasks by using available tools. 

If a user asks about files, documents, or content, first list the files before reading them.

When you are done, terminate the conversation by using the "terminate" tool and I will provide the results to the user.
"""
}]

# Initialize agent parameters
iterations = 0
max_iterations = 10

user_task = input("What would you like me to do? ")

memory = [{"role": "user", "content": user_task}]

# The Agent Loop
while iterations < max_iterations:

    messages = agent_rules + memory

    response = completion(
        model="openai/gpt-4o",
        messages=messages,
        tools=tools,
        max_tokens=1024
    )

    if response.choices[0].message.tool_calls:
        tool = response.choices[0].message.tool_calls[0]
        tool_name = tool.function.name
        tool_args = json.loads(tool.function.arguments)

        action = {
            "tool_name": tool_name,
            "args": tool_args
        }

        if tool_name == "terminate":
            print(f"Termination message: {tool_args['message']}")
            break
        elif tool_name in tool_functions:
            try:
                result = {"result": tool_functions[tool_name](**tool_args)}
            except Exception as e:
                result = {"error":f"Error executing {tool_name}: {str(e)}"}
        else:
            result = {"error": f"Unknown tool: {tool_name}"}

        print(f"Executing: {tool_name} with args {tool_args}")
        print(f"Result: {result}")
        memory.extend([
            {"role": "assistant", "content": json.dumps(action)},
            {"role": "user", "content": json.dumps(result)}
        ])
    else:
        result = response.choices[0].message.content
        print(f"Response: {result}")
        break