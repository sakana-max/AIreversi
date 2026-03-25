from Reversi import OllsearchAI,setup,sendMasu,RePrint,search,Enter,Ollsearch,WhihcWin,sendMasuNodAdd
from ollama import ChatResponse
from ollama import chat
import setting
modelNAME=setting.useAImodl()
def sendAI(text):
  global modelNAME
  masu = sendMasu()
  send = (setting.sendAI()+"コメント"+text+"\nマス\n"+masu+"\n選択可能なすべての座標\n"+str(OllsearchAI(1)))
  #print(send)
  response: ChatResponse = chat(model=modelNAME, messages=[
  {
    'role': 'user',
    'content':send,
  },
  ])
  print(response.message.content)
  return response.message.content.strip().splitlines()[-1]
print("strat")
setup()
winF = False
winF1 = False
sendComentTemp = ""
while True:
   RePrint()
   winF1 = False
   winF = False
   while True:
        if(Ollsearch(0) == False):
            print("置ける場所が無いようです")
            winF = True
            break
        pos =input("○のターン、置くマスを指定してください。例：44\n")
        if(pos.isdigit()):
            if(len(str(pos))== 1 or len(str(pos))> 2 or int(str(pos[0]))>8 or int(str(pos[1]))>8 or int(str(pos[0])) ==0 and int(str(pos[1])) ==0):
                print("不正な形式です数値で入力してください。例　XY")
            else:
                
                if(Enter(t=0,x=int(str(pos[0]))-1,y=int(str(pos[1]))-1)):
                    break
                else: print("置ける場所では無いないようです")
        else:
            print("不正な形式です数値で入力してください。例　XY")
   RePrint()
   while True:
        if(Ollsearch(1) == False):
            sendComentTemp+=("置ける場所が無いようです待機してください")
            print+=("AIは置ける場所がない")
            winF1 = True
            break
        pos =sendAI("●のターン、置くマスを指定してください。"+sendComentTemp)
        if(pos.isdigit()):
            if(len(str(pos))== 1 or len(str(pos))> 2 or int(str(pos[0]))>8 and int(str(pos[1]))>8 or int(str(pos[0])) ==0 and int(str(pos[1])) ==0):
                sendComentTemp+=("不正な形式です数値で入力してください。例　XY")
            else:
                
                if(Enter(t=1,x=int(str(pos[0]))-1,y=int(str(pos[1]))-1)):
                    sendComentTemp = ""
                    break
                else: sendComentTemp+=("間違えた場所を指定しています。ルール１を参照してください。")
                
        else:
            sendComentTemp+=("不正な形式です数値で入力してください。例　XY")
   if(winF == True and winF1 == True):
       print("勝利判定へ移行します")
       WW=0
       AC=0
       BC=0
       WW,AC,BC  = WhihcWin()
       WS = ""
       if(WW==0):
           WS = "○の勝ち"
       elif(WW==1):
           WS = "●の勝ち"
       else:
           WS="引き分け"
           
       print("○が"+str(AC)+":●が"+str(BC)+"で"+WS)
       break
input("Enterキーを押すと終了します...")