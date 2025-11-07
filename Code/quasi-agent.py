# Mit "assistant" erinnert sich das Modell an vorherige Antworten,
# hier an eine einfache Rechenfunktion.

from litellm import completion
from typing import List, Dict

def generate_response(messages: List[Dict]) -> str: # generate_response = Funktion, die eine Liste von Dicts (messages) entgegennimmt und einen String zurückgibt
    """Ruft das Sprachmodell auf und gibt die Textantwort zurück."""
    response = completion(
        model="openai/gpt-4o",
        messages=messages,
        max_tokens=300
    )
    return response.choices[0].message.content  # resonse = gesamte Antwort des Modells, .choicesc = Liste der Antwortmöglichkeiten, 
                                                # [0] = erste Antwort und keine weiteren Varianten, .message.content = Text der Antwort

def extract_code_block(response: str) -> str: # Extrahiert (parses) den Codeblock aus der Modellantwort.
    
    # Wenn im Text keine Code-Markierung (```) vorkommt, gibt es nichts zu extrahieren → Rückgabe der Originalantwort.
    if not '```' in response:
        return response

    # Antwort-Text an den Code-Markierungen auftrennen und den Teil zwischen dem ersten und zweiten ``` auswählen.
    code_block = response.split('```')[1].strip() #strip() entfernt überflüssige Leerzeichen oder Zeilenumbrüche.

    # Manche Modelle schreiben ```python am Anfang.Falls vorhanden, wird "python" entfernt, damit nur der reine Code übrig bleibt.
    if code_block.startswith("python"): # startswith("python") löscht das optionale Sprachlabel.
        code_block = code_block[6:] # Entfernt die ersten 6 Zeichen ("python")

    return code_block # Den bereinigten Codeblock zurückgeben.

def develop_custom_function():
   # Get user input for function description
   print("\nWhat kind of function would you like to create?")
   print("Example: 'A function that calculates the factorial of a number'")
   print("Your description: ", end='') # en=d='' verhindert den Zeilenumbruch nach der Eingabeaufforderung
   function_description = input().strip() # Liest die Benutzereingabe ein und entfernt überflüssige Leerzeichen.

   # Initialize conversation with system prompt
   messages = [
      {"role": "system", "content": "You are a Python expert helping to develop a function."}
   ]

   # First prompt - Basic function
   messages.append({ #.append() fügt eine neue Nachricht am Ende der Liste hinzu.
      "role": "user", "content": f"Write a Python function that {function_description}. Output the function in a ```python code block```."
   })
   initial_function = generate_response(messages) # Erste Antwort des Modells (Grundfunktion) wird in Variable initial_function gespeichert.

   initial_function = extract_code_block(initial_function)  # Parse the response to get the function code

   print("\n=== Initial Function ===")
   print(initial_function)

   # Add assistant's response to conversation. Notice that I am purposely causing it to forget its commentary and just see the code so that
   # it appears that is always outputting just code.
   messages.append({"role": "assistant", "content": "\`\`\`python\n\n"+initial_function+"\n\n\`\`\`"})

   # Second prompt - Add documentation
   messages.append({
      "role": "user",
      "content": "Add comprehensive documentation to this function, including description, parameters, "
                 "return value, examples, and edge cases. Output the function in a ```python code block```."
   })
   documented_function = generate_response(messages) #schreibt die Antwort des Modells mit Dokumentation in die Variable documented_function
   documented_function = extract_code_block(documented_function) # Parse the response to get the function code - siehe Funktion extract_code_block oben
   print("\n=== Documented Function ===")
   print(documented_function)

   # Add documentation response to conversation, wieder über assistant role
   messages.append({"role": "assistant", "content": "\`\`\`python\n\n"+documented_function+"\n\n\`\`\`"})

   # Third prompt - Add test cases
   messages.append({
      "role": "user",
      "content": "Add unittest test cases for this function, including tests for basic functionality, "
                 "edge cases, error cases, and various input scenarios. Output the code in a \`\`\`python code block\`\`\`."
   })
   test_cases = generate_response(messages)
   # We will likely run into random problems here depending on if it outputs JUST the test cases or the
   # test cases AND the code. This is the type of issue we will learn to work through with agents in the course.
   test_cases = extract_code_block(test_cases) # Parse the response to get the test case code only, without any extra text.
   print("\n=== Test Cases ===")
   print(test_cases)

   # Generate filename from function description
   filename = function_description.lower() # .lower() macht alle Buchstaben klein
   filename = ''.join(c for c in filename if c.isalnum() or c.isspace()) # Nur alphanumerische Zeichen und Leerzeichen behalten. c steht für jedes Zeichen im String.
   filename = filename.replace(' ', '_')[:30] + '.py' # Nur alphanumerische Zeichen und Unterstriche, max. 30 Zeichen lang und .py Endung

   # Save final version
   with open(filename, 'w') as f:
      f.write(documented_function + '\n\n' + test_cases)

   # print(f"{documented_function}\n\n{test_cases}\n\n{filename}") # Ausgabe der finalen Ergebnisse in der Konsole
   
   return documented_function, test_cases, filename # Rückgabe der finalen Funktion, Testfälle und Dateiname aus der Funktion develop_custom_function an das Hauptprogramm

if __name__ == "__main__": # Hauptprogramm: Wenn die Datei direkt ausgeführt wird, wird dieser Block ausgeführt. 
   # __name__ == "__main__" ist eine spezielle Bedingung in Python und stellt sicher, dass der Code nur ausgeführt wird, wenn die Datei direkt gestartet wird, und nicht, wenn sie als Modul importiert wird.

   function_code, tests, filename = develop_custom_function() # Aufruf der Funktion develop_custom_function und Speichern der Rückgabewerte in Variablen.
   print(f"\nFinal code has been saved to {filename}")

