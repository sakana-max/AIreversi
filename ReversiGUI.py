import tkinter as tk
from tkinter import messagebox,scrolledtext
from ollama import ChatResponse
from ollama import chat
from Reversi import setup, Enter, sendMasu,sendMasuNodAdd, Ollsearch, WhihcWin, OllsearchAI
import setting

class OthelloGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Reversi")
        
        # メインフレーム（盤面とログを横に並べる）
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(padx=10, pady=10)
        
        # 左側：盤面
        self.cell_size = 60
        self.canvas = tk.Canvas(self.main_frame, width=480, height=480, bg="#006400")
        self.canvas.pack(side=tk.LEFT)
        
        # 右側：ログウィンドウ
        self.log_frame = tk.Frame(self.main_frame)
        self.log_frame.pack(side=tk.LEFT, padx=(10, 0), fill=tk.Y)
        
        tk.Label(self.log_frame, text="AI Thinking Log").pack()
        self.log_area = scrolledtext.ScrolledText(self.log_frame, width=30, height=35, font=("MS Gothic", 9))
        self.log_area.pack()
        
        self.stone_ids = {}
        self.player_team = 1
        self.ai_team = 0
        self.current_team = 1

        setup()
        self.draw_grid()
        self.refresh_display()
        self.log("Game Started. Your turn (Black).")
        
        self.canvas.bind("<Button-1>", self.on_click)

    def log(self, message):
        """ログウィンドウにメッセージを追記し、自動スクロールする"""
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)

    def draw_grid(self):
        for i in range(9):
            pos = i * self.cell_size
            self.canvas.create_line(pos, 0, pos, 480, fill="black")
            self.canvas.create_line(0, pos, 480, pos, fill="black")

    def refresh_display(self):
        """Reversi.py の 8x8 配列を読み込んで描画を同期"""
        board_data = sendMasuNodAdd()
        for y in range(8):
            for x in range(8):
                mark = board_data[y][x]
                coord_key = f"X{x}Y{y}" # 0-7のインデックスで管理
                
                color = None
                if mark == '●': color = "black"
                elif mark == '○': color = "white"
                
                self._update_stone_graphic(coord_key, color, x, y)

    def _update_stone_graphic(self, key, color, x, y):
        """キャンバス上の石を更新"""
        if key in self.stone_ids:
            self.canvas.delete(self.stone_ids[key])
            del self.stone_ids[key]
        
        if color:
            pad = 6
            x1, y1 = x * self.cell_size + pad, y * self.cell_size + pad
            x2, y2 = (x + 1) * self.cell_size - pad, (y + 1) * self.cell_size - pad
            self.stone_ids[key] = self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline="black")

    def on_click(self, event):
        if self.current_team != self.player_team:
            return

        ix, iy = event.x // self.cell_size, event.y // self.cell_size
        
        if 0 <= ix < 8 and 0 <= iy < 8:
            if  Enter(self.player_team, iy, ix) == True:# ここは直った (iy, ix) の順
                self.log(f"You placed at: ({iy+1}, {ix+1})")
                self.after_move_process()

    def run_ai_turn(self):
     self.log("AI is thinking...")
     def sendAI(text):
     
      masu = sendMasu()
      send = (setting.sendAI()+"コメント"+text+"\nマス\n"+masu+"\n選択可能なすべての座標\n"+str(OllsearchAI(0)))
      #print(send)
      response: ChatResponse = chat(model=setting.useAImodl(), messages=[
       {
      'role': 'user',
      'content':send,
       },
      ])
      #print(response.message.content)
      return response.message.content.strip().splitlines()[-1],response.message.content.strip()
     sendComentTemp =""
     
     AIrespos  = ""
     while True:
        if(Ollsearch(0) == False):
            sendComentTemp+=("置ける場所が無いようです待機してください")
            #print+=("AIは置ける場所がない")
            break
        pos,AIrespos =sendAI("○のターン、置くマスを指定してください。"+sendComentTemp)
        if(pos.isdigit()):
            if(len(str(pos))== 1 or len(str(pos))> 2 or int(str(pos[0]))>8 and int(str(pos[1]))>8 or int(str(pos[0])) ==0 and int(str(pos[1])) ==0):
                sendComentTemp+=("不正な形式です数値で入力してください。例　XY")
            else:
                
                if(Enter(t=0,x=int(str(pos[0]))-1,y=int(str(pos[1]))-1)):
                    sendComentTemp = ""
                    break
                else: sendComentTemp+=("間違えた場所を指定しています。ルール１を参照してください。")
                
        else:
            sendComentTemp+=("不正な形式です数値で入力してください。例　XY")

        
        # LLMから思考内容と着手座標を取得する想定
        # OllsearchAIが(座標, 理由)のタプルなどを返すようにしておくと便利です
        
     self.log("AI chose:"+AIrespos)  
     self.after_move_process()

    def after_move_process(self):
        self.refresh_display()
        next_t = 1 - self.current_team
        
        if Ollsearch(next_t):
            self.current_team = next_t
            if self.current_team == self.ai_team:
                self.root.after(500, self.run_ai_turn)
        elif Ollsearch(self.current_team):
            self.log(f"Team {next_t} passed.")
            if self.current_team == self.ai_team:
                self.root.after(500, self.run_ai_turn)
        else:
            self.finish_game()

    def finish_game(self):
        winner, a, b = WhihcWin()
        res_msg = f"Winner: {'Black' if winner==1 else 'White'}\nScore: Black {b} - White {a}"
        self.log("--- Game Over ---")
        self.log(res_msg)
        messagebox.showinfo("Result", res_msg)

if __name__ == "__main__":
    root = tk.Tk()
    app = OthelloGUI(root)
    root.mainloop()