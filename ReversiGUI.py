import tkinter as tk
from tkinter import messagebox,scrolledtext
import threading
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
        #ログウィンドウにメッセージを追記し、自動スクロールする
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)

    def draw_grid(self):
        for i in range(9):
            pos = i * self.cell_size
            self.canvas.create_line(pos, 0, pos, 480, fill="black")
            self.canvas.create_line(0, pos, 480, pos, fill="black")

    def refresh_display(self):
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
        #キャンバス上の石を更新
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
     #AIの思考プロセスを別スレッドで開始する（フリーズ防止)
     self.log("--- AI's Turn ---")
     self.log("AI is thinking...")
    
     # 思考処理をバックグラウンドで実行
     thread = threading.Thread(target=self._ai_logic_thread)
     thread.daemon = True # アプリ終了時に一緒に終了するように
     thread.start()

    def _ai_logic_thread(self):
     #重いLLM通信とループ処理を行うスレッド
     sendComentTemp = ""
     AIrespos = ""

     while True:
        # パス判定
        if not Ollsearch(0):
            self.root.after(0, self.log, "AI: It seems there's no place to put it.")
            break

        # LLMへの問い合わせ（ここが重い）
        try:
            # 内部関数 sendAI を実行（元のコードのロジックを維持）
            pos_str, full_response = self.send_ai_request("It's ○'s turn, please specify the square where you want to place your piece." + sendComentTemp)
            
            # ログにAIの生の声（思考内容）を出力
            self.root.after(0, self.log, f"AI Thought:\n{full_response}")

            # 座標バリデーション
            if pos_str.isdigit() and len(pos_str) == 2:
                ix = int(pos_str[0]) - 1
                iy = int(pos_str[1]) - 1
                
                # 重要：先ほどの修正（iy, ix）に合わせて呼び出し
                if Enter(0, ix, iy): 
                    self.root.after(0, self.log, f"AI placed at {pos_str}")
                    break # 成功
                else:
                    sendComentTemp = " You have specified the wrong location. Please refer to Rule 1.out put"+pos_str
                    self.root.after(0, self.log, "warning AI chose an invalid square. Retrying...")
            else:
                sendComentTemp = " This is an invalid format. Please enter a number. Example: XY"
                self.root.after(0, self.log, f"warning AI gave invalid format: {pos_str}. Retrying...")

        except Exception as e:
            self.root.after(0, self.log, f"Communication Error: {e}")
            break
     # 処理が終わったらメインスレッドで画面更新
     self.root.after(0, self.after_move_process)
    def send_ai_request(self, text):
        
     from ollama import chat, ChatResponse # ライブラリに合わせて調整してください
    
     masu = sendMasu() # 文字列形式のマス
     selectable = str(OllsearchAI(0)) # 置ける場所リスト
    
     # プロンプト作成
     send_content = (
        setting.sendAI() + 
        "comment " + text + 
        "\ntrout\n" + masu + 
        "\nAll selectable coordinates\n" + selectable
     )
     #print(send_content)
     response: ChatResponse = chat(
        model=setting.useAImodl(), 
        messages=[{'role': 'user', 'content': send_content}]
     )
    
     content = response.message.content.strip()
     # 最終行を座標(XY)、全体を思考ログとして返す
     #print(content)
     return content.splitlines()[-1], content
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