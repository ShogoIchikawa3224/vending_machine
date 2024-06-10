# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 08:55:08 2024

@author: Administrator
"""

import sys
import tkinter as tk
import math
import mysql.connector as db



class Vending_Machine_UI():
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
                #自販機の描写
        self.canvas.create_rectangle(10,50,430,750,fill='#ff0000')
        self.canvas.create_rectangle(30,600,300,670,fill='gray')
        self.canvas.create_rectangle(350,620,400,670,fill='gray')
        self.canvas.create_rectangle(30,80,410,380,fill='white')
        self.canvas.create_rectangle(220,430,270,480,fill='black')
        self.canvas.create_rectangle(300,400,360,450,fill='black')
        self.canvas.create_arc(200,300,400,500,fill='black',start=270)
        
        #ボタン上の温度と商品の配置
        self.merchandise_label = ["水","お\n茶","炭\n酸\n数","ソ\n |\nダ","コ\n |\nラ"]
        self.merchandise_labels = []
        
        j=0
        for i in range(12):
            self.merchandise_labels.append(self.merchandise_label[j])
            j+=1
            if j == 5:
                j=0
                
        for x in range(3):
            for y in range(12):
                    self.canvas.create_rectangle(45+y*30,155+x*100,62+y*30,163+x*100,fill='#0000ff')
                    self.canvas.create_rectangle(43+y*30,105+x*100,65+y*30,153+x*100,fill=self.color[y])
                    self.canvas.create_text(55+y*30,130+x*100,text = self.merchandise_labels[y],font=("",8))
        
        #入金額を表示
        #self.Deposit_amount=tk.Label(text=self.display_now_cash)
        
        
        #ボタンの生成        
        self.button_labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                             "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                             "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4",
                             "5", "6", "7", "8", "9", "0"]
        
        # ボタンの位置をリストで定義
        self.button_positions = [(50 + 30 * (i % 12), 170 + 100 * (i // 12)) for i in range(len(self.button_labels))]
        
        
        
        # ボタンを動的に配置
        for label, (x, y) in zip(self.button_labels, self.button_positions):
            button = tk.Button(self.root, relief="raised", bg="#1c1c1c", activebackground="#2c2c2c", text=label, command=lambda lbl=label: self.button_command(lbl))
            button.place(x=x, y=y, height=10, width=18)
            
            
                
        #金額ボタン
        self.Button10 = tk.Button(text=u'10円', font=("",30), relief="raised", fg="#ffffff", bg="#7f0000", activeforeground="#cccccc", activebackground="#af0000")
        self.Button50 = tk.Button(text=u'50円', font=("",30), relief="raised", fg="#ffffff", bg="#888888", activeforeground="#cccccc", activebackground="#aaaaaa")
        self.Button100 = tk.Button(text=u'100円', font=("",30), relief="raised", fg="#ffffff", bg="#888888", activeforeground="#cccccc", activebackground="#aaaaaa")
        self.Button500 = tk.Button(text=u'500円', font=("",30), relief="raised", fg="#ffffff", bg="#777700", activeforeground="#aaaaaa", activebackground="#aaaa00")
        self.Button1000 = tk.Button(text=u'1000円', font=("",30), relief="raised", fg="#ffffff", bg="#aaaa55", activeforeground="#cccccc", activebackground="#af0000")
        
        #返金
        self.ButtonReturn = tk.Button(text=u'返金', font=("",30), relief="raised", fg="#ffffff", bg="#aaaa55", activeforeground="#cccccc", activebackground="#af0000")
        
        #上記ボタンの配置
        self.Button10.place(x=500, y=100, height=50, width=200)
        self.Button50.place(x=500, y=160, height=50, width=200)
        self.Button100.place(x=500, y=220, height=50, width=200)
        self.Button500.place(x=500, y=280, height=50, width=200)
        self.Button1000.place(x=500, y=340, height=50, width=200)
        self.ButtonReturn.place(x=500, y=400, height=50, width=200)
        
        
        
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
        self.my_db: object = None
        self.my_db: object = None
        self.my_db = db.connect(host = "localhost", user = "root", password="", db = "vending_machine_db") 
        if self.my_db != None:
            self.my_db.ping(reconnect=True)
            print("is connected?: {}\n".format(self.my_db.is_connected()))
        if self.my_db != None and self.my_db != None:
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
        if self.cursor != None:
            self.cursor.close()
        self.my_db.close()
        print("database was closed.\n")     
        
# app = Vending_Machine_UI()
        
app = VendingMachineDB()
        
        
        