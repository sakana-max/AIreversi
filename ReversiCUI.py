from Reversi import OllsearchAI,setup,sendMasu,RePrint,search,Enter,Ollsearch,WhihcWin,sendMasuNodAdd
from ollama import ChatResponse
from ollama import chat
import setting
#モジュールをインポート
#Import module

#設定から使用するモデルを受け取る
#Receive the model to use from the settings
modelNAME=setting.useAImodl()

def sendAI(text):
  #AIにプロンプトを送り、座標を返す
  #Send a prompt to the AI ​​and return the coordinates.
  global modelNAME
  masu = sendMasu()
  send = (setting.sendAI()+"comment"+text+"\ntrout\n"+masu+"\nAll selectable coordinates\n"+str(OllsearchAI(0)))
  #print(send)
  response: ChatResponse = chat(model=modelNAME, messages=[
  {
    'role': 'user',
    'content':send,
  },
  ])
  print(response.message.content)
  return response.message.content.strip().splitlines()[-1]

#初期設定
#Initial settings
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
       #黒の番 
       #black turn 
        if(Ollsearch(1) == False):
            print("It seems there's no place to put it.")
            winF = True
            break
        pos =input("● During your turn, please specify the square where you will place the item. Example: 44\n")
        if(pos.isdigit()):
            if(len(str(pos))== 1 or len(str(pos))> 2 or int(str(pos[0]))>8 or int(str(pos[1]))>8 or int(str(pos[0])) ==0 and int(str(pos[1])) ==0):
                print("This is an invalid format. Please enter a number. Example: 44")
            else:
                
                if(Enter(t=1,x=int(str(pos[0]))-1,y=int(str(pos[1]))-1)):
                    break
                else: print("It seems there's no place to put it.")
        else:
            print("This is an invalid format. Please enter a number. Example: 44")
   RePrint()
   #白の番
   #White's turn
   while True:
        if(Ollsearch(0) == False):
            sendComentTemp=(" It seems there's no place to put it. Please wait.")
            print+=("AI: It seems there's no place to put it.")
            winF1 = True
            break
        pos =sendAI("It's ○'s turn, please specify the square where you want to place your piece."+sendComentTemp)
        if(pos.isdigit()):
            if(len(str(pos))== 1 or len(str(pos))> 2 or int(str(pos[0]))>8 and int(str(pos[1]))>8 or int(str(pos[0])) ==0 and int(str(pos[1])) ==0):
                sendComentTemp=(" This is an invalid format. Please enter a number. Example: XY")
            else:
                
                if(Enter(t=0,x=int(str(pos[0]))-1,y=int(str(pos[1]))-1)):
                    sendComentTemp = ""
                    break
                else: sendComentTemp=(" You have specified the wrong location. Please refer to Rule 1.")
                
        else:
            sendComentTemp=(" This is an invalid format. Please enter a number. Example: XY")
   #両者置ける場所がない場合に勝利判定
   #Victory is determined when neither player has a place to put their piece.         
   if(winF == True and winF1 == True):
       print("We will now proceed to the victory determination.")
       WW=0
       AC=0
       BC=0
       WW,AC,BC  = WhihcWin()
       WS = ""
       if(WW==0):
           WS = "○ wins"
       elif(WW==1):
           WS = "● wins"
       else:
           WS="draw"
           
       print("○:"+str(AC)+":●:"+str(BC)+" "+WS)
       break
input("Pressing Enter will exit...")