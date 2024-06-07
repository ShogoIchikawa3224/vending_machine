# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 08:55:08 2024

@author: Administrator
"""

import sys
import tkinter as tk
import math
import mysql.connector as db



class vending_machine_UI():
    
    
    def __init__(self):
        self.root = tk.Tk()
        self.product_list: list = None
        self.display_now_cash: int = 0
        self.root.title(u"自動販売機")
        self.root.geometry("800x800")
        self.canvas = tk.Canvas(self.root, width=500, height=800)
        self.canvas.place(x=5,y=5)
        self.color = ['#ff0000','#00ff00','#0000ff','#ffff00','#ff00ff','#00ffff',
                      '#ff5500','#55ff00','#0055ff','#ffff55','#ff55ff','#55ffff',]
        self.canvas.create_rectangle(10,50,430,750,fill='#ff0000')
        self.canvas.create_rectangle(30,600,300,670,fill='gray')
        self.canvas.create_rectangle(350,620,400,670,fill='gray')
        self.canvas.create_rectangle(30,80,410,380,fill='white')
        self.canvas.create_rectangle(220,430,270,480,fill='black')
        self.canvas.create_rectangle(300,400,360,450,fill='black')
        #ボタン上の温度と商品の配置
        for x in range(3):
            for y in range(12):
                    self.canvas.create_rectangle(45+y*30,155+x*100,62+y*30,163+x*100,fill='#0000ff')
                    self.canvas.create_rectangle(43+y*30,105+x*100,65+y*30,153+x*100,fill=self.color[y])

        
        
        self.canvas.create_arc(200,300,400,500,fill='black',start=270)
        self.ButtonA = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.ButtonB = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.ButtonC = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.ButtonD = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.ButtonE = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.ButtonF = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.ButtonG = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.ButtonH = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.ButtonI = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.ButtonJ = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.ButtonK = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.ButtonL = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.ButtonM = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.ButtonN = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.ButtonO = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.ButtonP = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.ButtonQ = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.ButtonR = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.ButtonS = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.ButtonT = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.ButtonU = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.ButtonV = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.ButtonW = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.ButtonX = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.ButtonY = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.ButtonZ = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.Button1 = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.Button2 = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.Button3 = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.Button4 = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.Button5 = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.Button6 = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.Button7 = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.Button8 = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.Button9 = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.Button0 = tk.Button(relief="raised", bg="#1c1c1c",  activebackground="#2c2c2c")
        self.Button10 = tk.Button(text=u'10円', font=("",30), relief="raised", fg="#ffffff", bg="#7f0000", activeforeground="#cccccc", activebackground="#af0000", command= lambda: self.push_product_btn(10))
        self.Button50 = tk.Button(text=u'50円', font=("",30), relief="raised", fg="#ffffff", bg="#888888", activeforeground="#cccccc", activebackground="#aaaaaa", command= lambda: self.push_product_btn(50))
        self.Button100 = tk.Button(text=u'100円', font=("",30), relief="raised", fg="#ffffff", bg="#888888", activeforeground="#cccccc", activebackground="#aaaaaa", command= lambda: self.push_product_btn(100))
        self.Button500 = tk.Button(text=u'500円', font=("",30), relief="raised", fg="#ffffff", bg="#777700", activeforeground="#aaaaaa", activebackground="#aaaa00", command= lambda: self.push_product_btn(500))
        self.Button1000 = tk.Button(text=u'1000円', font=("",30), relief="raised", fg="#ffffff", bg="#aaaa55", activeforeground="#cccccc", activebackground="#af0000", command= lambda: self.push_product_btn(1000))
        
        
        self.ButtonA.place(x=50, y=170, height=10, width=18)
        self.ButtonB.place(x=80, y=170, height=10, width=18)
        self.ButtonC.place(x=110, y=170, height=10, width=18)
        self.ButtonD.place(x=140, y=170, height=10, width=18)
        self.ButtonE.place(x=170, y=170, height=10, width=18)
        self.ButtonF.place(x=200, y=170, height=10, width=18)
        self.ButtonG.place(x=230, y=170, height=10, width=18)
        self.ButtonH.place(x=260, y=170, height=10, width=18)
        self.ButtonI.place(x=290, y=170, height=10, width=18)
        self.ButtonJ.place(x=320, y=170, height=10, width=18)
        self.ButtonK.place(x=350, y=170, height=10, width=18)
        self.ButtonL.place(x=380, y=170, height=10, width=18)
        self.ButtonM.place(x=50, y=270, height=10, width=18)
        self.ButtonN.place(x=80, y=270, height=10, width=18)
        self.ButtonO.place(x=110, y=270, height=10, width=18)
        self.ButtonP.place(x=140, y=270, height=10, width=18)
        self.ButtonQ.place(x=170, y=270, height=10, width=18)
        self.ButtonR.place(x=200, y=270, height=10, width=18)
        self.ButtonS.place(x=230, y=270, height=10, width=18)
        self.ButtonT.place(x=260, y=270, height=10, width=18)
        self.ButtonU.place(x=290, y=270, height=10, width=18)
        self.ButtonV.place(x=320, y=270, height=10, width=18)
        self.ButtonW.place(x=350, y=270, height=10, width=18)
        self.ButtonX.place(x=380, y=270, height=10, width=18)
        self.ButtonY.place(x=50, y=370, height=10, width=18)
        self.ButtonZ.place(x=80, y=370, height=10, width=18)
        self.Button1.place(x=110, y=370, height=10, width=18)
        self.Button2.place(x=140, y=370, height=10, width=18)
        self.Button3.place(x=170, y=370, height=10, width=18)
        self.Button4.place(x=200, y=370, height=10, width=18)
        self.Button5.place(x=230, y=370, height=10, width=18)
        self.Button6.place(x=260, y=370, height=10, width=18)
        self.Button7.place(x=290, y=370, height=10, width=18)
        self.Button8.place(x=320, y=370, height=10, width=18)
        self.Button9.place(x=350, y=370, height=10, width=18)
        self.Button0.place(x=380, y=370, height=10, width=18)
        self.Button10.place(x=500, y=100, height=50, width=200)
        self.Button50.place(x=500, y=160, height=50, width=200)
        self.Button100.place(x=500, y=220, height=50, width=200)
        self.Button500.place(x=500, y=280, height=50, width=200)
        self.Button1000.place(x=500, y=340, height=50, width=200)
        self.root.mainloop()

        self.set_product_from_db()

    # データベースと接続して商品を配置する
    def set_product_from_db(self) -> None:
        my_db = VendingMachineDB()
        self.product_list = my_db.show_table("SELECT * FROM `product_tb`;")
        del my_db
        # ここで取得した商品を自動販売機に対して割り振る動作も追加する

    # 押されたボタンに対して処理を実装
    def push_product_btn(self, product_num: str) -> None:
        pass

    # dbとのやり取りを行う
        
    # 投入金額に対して購入できる商品を表示する

    # 投入金額の取得
    def push_cash_btn(self, cash_price: int) -> list:
        if(cash_price == 10):
            pass
        elif(cash_price == 10):
            pass
        elif(cash_price == 50):
            pass
        elif(cash_price == 500):
            pass
        elif(cash_price == 1000):
            pass






class VendingMachineDB:
    def __init__(self) -> None:
        self.my_db = db.connect(host = "localhost", user = "root", password="", db = "vending_machine_db")
        self.my_db.ping(reconnect=True)
        print("is connected?: {}\n".format(self.my_db.is_connected()))
        self.cursor = self.my_db.cursor(buffered=True)

    # クエリ実行
    def execute_the_query(self, query: str) -> None:
        try:
            self.cursor.execute(query)
            self.my_db.commit()
        except Exception as err:
            print(f"Error: '{err}'")

    # 表示 未実装
    def show_table(self, query: str) -> list:
        result: list = []
        try:
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            if data != None:
                for d in data:
                    result.append(d)
            print(result)
            return result
        except Exception as err:
            print(f"Error: {err}")

    # 削除時実行
    def __del__(self) -> None:
        self.cursor.close()
        self.my_db.close()
        print("database was closed.\n")     

        

app = vending_machine_UI()
        
        
        