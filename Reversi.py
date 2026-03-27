#盤面を保存するリストを作成
#Create a list to save the game board
bannmenn =[]

#初期セットアップ
#Initial setup
def setup():
    #マスは□●○で表している
    #The squares are represented by □●○
    global bannmenn
    bannmenn = [["□" for i in range(8)] for i in range(8)]
    
    #リバーシの初期配置を作る
    #Create the initial setup for Reversi.
    bannmenn[3][3] = "○"
    bannmenn[3][4] = "●"
    bannmenn[4][3] = "●"
    bannmenn[4][4] = "○"
    
def sendMasu():
    #盤面を数字の目印が付いた状態で文字で返す
    #Return the board with numbered markers as text.
    global bannmenn
    tempnum =0
    text =""
    for b in bannmenn:
        tempnum+=1
        text += str(tempnum)
        for bb in b:
            text += str(bb)
        text +="\n"
    text +=" 12345678\n"
    return text

def sendMasuNodAdd():
    #盤面を配列のまま返す
    # Return the board state as an array
    global bannmenn
    return bannmenn
        
def RePrint():
    #盤面の状況をPrintする
    #Print the board state
    global bannmenn
    tempnum =0
    for b in bannmenn:
        tempnum+=1
        tempText = ""
        for bb in b:
            tempText += bb
        print(str(tempnum) + tempText)
    print(" 12345678\n")
    
def search(t,x,y):
    #Tのチームが、X、Yに石を置けるか調べる。そこに置けるならTrueそうでなければFalseが返る。同時に、変更できるすべての座標のリストを返す
    #複雑なコードにより、変更は要注意
    #Check if Team T can place a stone at X and Y. It returns True if possible, False otherwise. It also returns a list of all possible coordinates that can be changed.
    #Due to the complex code, changes require caution.
    global bannmenn
    searchX =y
    searchY =x
    flagSecrch = False
    SquareToChange = [[x,y]]
    SquareToChangeTemp = [[x,y]]
    if(t==0):
        if(bannmenn[x][y] =="□"):
            
            while searchX < 7:
               searchX+=1
               if bannmenn[searchY][searchX]== "□":
                   break
               elif(bannmenn[searchY][searchX]== "●"):
                   
                   SquareToChangeTemp.append([searchY,searchX])
                   
               elif(bannmenn[searchY][searchX]== "○" and y+1 != searchX):
                   flagSecrch = True
                   for L in SquareToChangeTemp:
                       SquareToChange.append(L)
                   break
               else:
                   break
            searchX =y
            searchY =x
            SquareToChangeTemp = [[x,y]]
            while searchX > 0:
               searchX-=1
               if bannmenn[searchY][searchX]== "□":
                   break
               elif(bannmenn[searchY][searchX]== "●"):
                   
                   SquareToChangeTemp.append([searchY,searchX])
                   
               elif(bannmenn[searchY][searchX]== "○" and y-1 != searchX):
                   flagSecrch = True
                   for L in SquareToChangeTemp:
                       SquareToChange.append(L)
                   break
               else:
                   break
            searchX =y
            searchY =x
            SquareToChangeTemp = [[x,y]]
            while searchY > 0:
               searchY-=1
               if bannmenn[searchY][searchX]== "□":
                   break
               elif(bannmenn[searchY][searchX]== "●"):
                   
                   SquareToChangeTemp.append([searchY,searchX])
                   
               elif(bannmenn[searchY][searchX]== "○" and x-1 != searchY):
                   flagSecrch = True
                   for L in SquareToChangeTemp:
                       SquareToChange.append(L)
                   break
               else:
                   break
            searchX =y
            searchY =x
            SquareToChangeTemp = [[x,y]]
            while searchY < 7:
               searchY+=1
               if bannmenn[searchY][searchX]== "□":
                   break
               elif(bannmenn[searchY][searchX]== "●"):
                   
                   SquareToChangeTemp.append([searchY,searchX])
                   
               elif(bannmenn[searchY][searchX]== "○" and x+1 != searchY):
                   flagSecrch = True
                   for L in SquareToChangeTemp:
                       SquareToChange.append(L)
                   break
               else:
                   break
            searchX =y
            searchY =x
            SquareToChangeTemp = [[x,y]]
            while searchY > 0 and searchX < 7:
               searchY-=1
               searchX+=1
               if bannmenn[searchY][searchX]== "□":
                   break
               elif(bannmenn[searchY][searchX]== "●"):
                   
                   SquareToChangeTemp.append([searchY,searchX])
                   
               elif(bannmenn[searchY][searchX]== "○" and x-1 != searchY and y+1 != searchX):
                   flagSecrch = True
                   for L in SquareToChangeTemp:
                       SquareToChange.append(L)
                   break
               else:
                   break
            searchX =y
            searchY =x
            SquareToChangeTemp = [[x,y]]
            while searchY < 7 and searchX < 7:
               searchY+=1
               searchX+=1
               if bannmenn[searchY][searchX]== "□":
                   break
               elif(bannmenn[searchY][searchX]== "●"):
                   
                   SquareToChangeTemp.append([searchY,searchX])
                   
               elif(bannmenn[searchY][searchX]== "○" and x+1 != searchY and y+1 != searchX):
                   flagSecrch = True
                   for L in SquareToChangeTemp:
                       SquareToChange.append(L)
                   break
               else:
                   break
            searchX =y
            searchY =x
            SquareToChangeTemp = [[x,y]]
            while searchY < 7 and searchX > 0:
               searchY+=1
               searchX-=1
               if bannmenn[searchY][searchX]== "□":
                   break
               elif(bannmenn[searchY][searchX]== "●"):
                   
                   SquareToChangeTemp.append([searchY,searchX])
                   
               elif(bannmenn[searchY][searchX]== "○" and x+1 != searchY and y-1 != searchX):
                   flagSecrch = True
                   for L in SquareToChangeTemp:
                       SquareToChange.append(L)
                   break
               else:
                   break
            searchX =y
            searchY =x
            SquareToChangeTemp = [[x,y]]
            while searchY > 0 and searchX > 0:
               searchY-=1
               searchX-=1
               if bannmenn[searchY][searchX]== "□":
                   break
               elif(bannmenn[searchY][searchX]== "●"):
                   
                   SquareToChangeTemp.append([searchY,searchX])
                   
               elif(bannmenn[searchY][searchX]== "○" and x-1 != searchY and y-1 != searchX):
                   flagSecrch = True
                   for L in SquareToChangeTemp:
                       SquareToChange.append(L)
                   break
               else:
                   break
    if(t==1):
        if(bannmenn[x][y] =="□"):
            
            while searchX < 7:
               searchX+=1
               if bannmenn[searchY][searchX]== "□":
                   break
               elif(bannmenn[searchY][searchX]== "○"):
                   
                   SquareToChangeTemp.append([searchY,searchX])
                   
               elif(bannmenn[searchY][searchX]== "●" and y+1 != searchX):
                   flagSecrch = True
                   for L in SquareToChangeTemp:
                       SquareToChange.append(L)
                   break
               else:
                   break
            searchX =y
            searchY =x
            SquareToChangeTemp = [[x,y]]
            while searchX > 0:
               searchX-=1
               if bannmenn[searchY][searchX]== "□":
                   break
               elif(bannmenn[searchY][searchX]== "○"):
                   
                   SquareToChangeTemp.append([searchY,searchX])
                   
               elif(bannmenn[searchY][searchX]== "●" and y-1 != searchX):
                   flagSecrch = True
                   for L in SquareToChangeTemp:
                       SquareToChange.append(L)
                   break
               else:
                   break
            searchX =y
            searchY =x
            SquareToChangeTemp = [[x,y]]
            while searchY > 0:
               searchY-=1
               if bannmenn[searchY][searchX]== "□":
                   break
               elif(bannmenn[searchY][searchX]== "○"):
                   
                   SquareToChangeTemp.append([searchY,searchX])
                   
               elif(bannmenn[searchY][searchX]== "●" and x-1 != searchY):
                   flagSecrch = True
                   for L in SquareToChangeTemp:
                       SquareToChange.append(L)
                   break
               else:
                   break
            searchX =y
            searchY =x
            SquareToChangeTemp = [[x,y]]
            while searchY < 7:
               searchY+=1
               if bannmenn[searchY][searchX]== "□":
                   break
               elif(bannmenn[searchY][searchX]== "○"):
                   
                   SquareToChangeTemp.append([searchY,searchX])
                   
               elif(bannmenn[searchY][searchX]== "●" and x+1 != searchY):
                   flagSecrch = True
                   for L in SquareToChangeTemp:
                       SquareToChange.append(L)
                   break
               else:
                   break
            searchX =y
            searchY =x
            SquareToChangeTemp = [[x,y]]
            while searchY > 0 and searchX < 7:
               searchY-=1
               searchX+=1
               if bannmenn[searchY][searchX]== "□":
                   break
               elif(bannmenn[searchY][searchX]== "○"):
                   
                   SquareToChangeTemp.append([searchY,searchX])
                   
               elif(bannmenn[searchY][searchX]== "●" and x-1 != searchY and y+1 != searchX):
                   flagSecrch = True
                   for L in SquareToChangeTemp:
                       SquareToChange.append(L)
                   break
               else:
                   break
            searchX =y
            searchY =x
            SquareToChangeTemp = [[x,y]]
            while searchY < 7 and searchX < 7:
               searchY+=1
               searchX+=1
               if bannmenn[searchY][searchX]== "□":
                   break
               elif(bannmenn[searchY][searchX]== "○"):
                   
                   SquareToChangeTemp.append([searchY,searchX])
                   
               elif(bannmenn[searchY][searchX]== "●" and x+1 != searchY and y+1 != searchX):
                   flagSecrch = True
                   for L in SquareToChangeTemp:
                       SquareToChange.append(L)
                   break
               else:
                   break
            searchX =y
            searchY =x
            SquareToChangeTemp = [[x,y]]
            while searchY < 7 and searchX > 0:
               searchY+=1
               searchX-=1
               if bannmenn[searchY][searchX]== "□":
                   break
               elif(bannmenn[searchY][searchX]== "○"):
                   
                   SquareToChangeTemp.append([searchY,searchX])
                   
               elif(bannmenn[searchY][searchX]== "●" and x+1 != searchY and y-1 != searchX):
                   flagSecrch = True
                   for L in SquareToChangeTemp:
                       SquareToChange.append(L)
                   break
               else:
                   break
            searchX =y
            searchY =x
            SquareToChangeTemp = [[x,y]]
            while searchY > 0 and searchX > 0:
               searchY-=1
               searchX-=1
               if bannmenn[searchY][searchX]== "□":
                   break
               elif(bannmenn[searchY][searchX]== "○"):
                   
                   SquareToChangeTemp.append([searchY,searchX])
                   
                   
               elif(bannmenn[searchY][searchX]== "●" and x-1 != searchY and y-1 != searchX):
                   flagSecrch = True
                   for L in SquareToChangeTemp:
                       SquareToChange.append(L)
                   break
               else:
                   break
               
    return flagSecrch,SquareToChange
                   
       
def Enter(t,x,y):
    #TのチームがX,Yに石を置く。置けたらTrueそうでなければFalseが返る
    #Team T places stones on X and Y. The result is True if the stones are placed, otherwise it's False.
    flagTemp,chemge =search(t,x,y)
    if(t==0):
       if(flagTemp == True):
           for t in chemge:
             bannmenn[t[0]][t[1]]  ="○"
    if(t==1):
        if(flagTemp == True):
           for t in chemge:
             bannmenn[t[0]][t[1]]  ="●"
    return flagTemp

def OllsearchAI(T=1):
    #Tのチームが置くことのできるすべてのリストを返す
    #Returns a list of all possible places that team T can place.
    global bannmenn
    tempF = False
    temp=[]
    sendAIlist =[]
    X=0
    Y=0
    for A in bannmenn:
        for B in A:
            tempF,temp=search(t=T,x=X,y=Y)
            
            if(tempF == True):
                sendAIlist.append([X,Y])
            X+=1
        Y+=1
        X=0
    sendtext = ""
    for L in sendAIlist:
        for LL in L:
            sendtext += str(LL+1)
        sendtext +="  "
    return sendtext
def Ollsearch(T):
    #Tのチームが石を置けるかを返す
    #T's team will return whether they can place a stone.
    global bannmenn
    tempF = False
    temp=[]
    X=0
    Y=0
    for A in bannmenn:
        for B in A:
            tempF,temp=search(t=T,x=X,y=Y)
            if(tempF == True):
                break
            X+=1
        if(tempF == True):
                break 
        Y+=1
        X=0

    return tempF
def WhihcWin():
    #勝利判定をする
    # Determine the winner.
    Acount=0
    Bcount=0
    global bannmenn
    
    for m in bannmenn:
        for mm in m:
            if(mm =="○"):
                Acount+=1
            if(mm =="●"):
                Bcount+=1
    Winflag =0
    if(Acount > Bcount):
        WinHlag=0
    elif(Acount < Bcount):
        WinHlag=1
    else:
        WinHlag=2
    return WinHlag,Acount,Bcount