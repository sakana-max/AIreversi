# AIreversi
[日本語版はこちら](README_JP.md)

This project allows you to play Reversi (Othello) against an LLM (Large Language Model) using Ollama.

(This was machine translated. The expression may not be appropriate.)
<img width="1549" height="857" alt="main" src="https://github.com/sakana-max/AIreversi/blob/main/main.png" />

## Execution
### Prerequisites to clone and run this repository:
(1)Python must be installed.

(2)The ollama Python module must be installed.

(3)Ollama must be installed on your system.

(Note: Since this project uses Tkinter, Linux users may need to install it separately via their package manager.)

If the required Python module is not installed, please run:

```
pip install ollama
````
Once the requirements are met, navigate to the cloned directory and run the following:

For GUI mode:

```
python ReversiGUI.py
```
For CUI (Terminal) mode:

```
python ReversiCUI.py
```
Language Settings:
To change the AI's responses to Japanese, rename setting-jp.py to setting.py (overwriting the existing file).

You are now ready to play Reversi against the AI!

## AI Model
The default model used is gemma3:12b.

You can change the model by modifying the value in the useAImodl() function within setting.py.

Note: Models with "Reasoning/Think" capabilities are not recommended, as they may result in infinite thinking loops.

You can also customize the AI's prompt by modifying the text in the sendAI() function within setting.py.
