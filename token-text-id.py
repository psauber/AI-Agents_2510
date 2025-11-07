# Installiere das Paket tiktoken (nur einmal nötig)
# pip install tiktoken

import tiktoken

# Tokenizer laden – GPT-4 verwendet denselben wie GPT-3.5-Turbo
encoding = tiktoken.encoding_for_model("gpt-4o") # tiktoken ist die offizielle Tokenizer-Bibliothek von OpenAI. 
# encoding_for_model("gpt-4o") lädt das Vokabular und die Regeln für das GPT-4-Modell.

# Beispieltext
text = "Diese Funktion zeigt, wie Tokenisierung funktioniert und wandelt Text in Tokens um."

# Tokenisierung
tokens = encoding.encode(text) # encode() zerlegt deinen Text in Token-IDs (Zahlen).

# Zurückübersetzen (nur zum Verständnis)
decoded = [encoding.decode([t]) for t in tokens] # decode() kann diese IDs wieder in Text zurückverwandeln.

# Ausgabe
print("Text:     ", text)
print("Tokens:   ", tokens)
print("Decoded:  ", decoded)
print("Anzahl Tokens:", len(tokens))
