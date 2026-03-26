# AIreversi

このプロジェクトは、Ollamaを使用し、LLMとリバーシをします。

<img width="1549" height="857" alt="main" src="https://github.com/sakana-max/AIreversi/blob/main/main.png" />


## 実行

### リポジトリをクローンし、実行するには、

1,pythonがインストールされている。

2,pythonにollamaモジュールがインストールされている。

3,Ollamaがインストールされている。



ことが必要です。(Tkinterを使用しているため、Linuxでは別途インストールが必要かもしれません。)


もしモジュールがインストールされていない場合は以下を実行してください。

```
pip install ollama
```

条件を満たしたら、クローンしたディレクトリで以下を実行してください。
```
python ReversiGUI.py
```
CUIを使用する場合は以下を実行してください。

```
python ReversiCUI.py
```

AIの返答を日本語にする際は、setting-jp.pyの名前をsetting.pyに変更し、上書き保存してください。

これでAIとリバーシをプレイすることができます。

## AIモデル

初期値では gemma3:12b　を使用します

‎setting.py‎の useAImodl() の値を変更することでモデルを変更できます。

Think機能があるモデルは推奨しません。永遠と考えを続けてしまいます。

また　‎setting.py‎のsendAI()の文字を変更することでAIのプロンプトを変更することができます。
