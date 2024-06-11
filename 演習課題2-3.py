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
        self.product_list: list = []              # 商品のidを獲得する
        self.display_now_cash: int = 0              # 投入合計金額
        self.button_labels: list = ["","","","","","","","","","",
                                "","","","","","","","","","",
                                "","","","","","","","","","",
                                "","","","","",""]                 # ボタンのlabelを登録する.(ここでは商品idを格納しておく)
                                
        self.user_cash_list = [0, 0, 0, 0, 0]       # どの硬貨がどれだけ投入されたかを保持
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

# 購入ボタン反応チェックーーーーーーーーーーーーーーーー        
        # self.push_cash_btn(10)
        # self.push_cash_btn(10)
        # self.push_cash_btn(10)
        # self.push_cash_btn(50)
        # self.push_cash_btn(100)
        # self.push_cash_btn(100)
        # self.push_cash_btn(100)
        # self.push_cash_btn(500)
        # self.push_cash_btn(1000)
        # self.connection_with_db_cash()
# 購入ボタン反応チェックーーーーーーーーーーーーーーーー

        # 初期設定(DBから商品を引っ張ってくる)
        self.set_product_from_db("product_tb")

    # データベースと接続して商品を配置する
    def set_product_from_db(self, tb_name:str) -> None:
        my_db = VendingMachineDB()
        for product_key in my_db.show_table_all(tb_name):
            self.product_list.append(product_key)
        del my_db
        # ここで取得した商品を自動販売機に対して割り振る動作も追加する
        j = 0
        for i in range(len(self.button_labels)):
            self.button_labels[i] = self.product_list[j][0]
            j = j + 1
            if(j == len(self.product_list)):
                j = 0

    # 押されたボタンに対して処理を実装
    def push_product_btn(self, label: int) -> None:
        pass
        # 押されたボタンの商品が何かを判定し、その金額を把握
        # 投入された硬貨に対して
        
    # 投入金額に対して購入できる商品を表示する
    def is_products_available_purchase(self) -> None:
        pass

    # 投入金額の取得
    def push_cash_btn(self, cash_price: int) -> None:
        if(cash_price == 10):
            self.user_cash_list[0] = self.user_cash_list[0] + 1
        elif(cash_price == 10):
            self.user_cash_list[1] = self.user_cash_list[1] + 1
        elif(cash_price == 50):
            self.user_cash_list[2] = self.user_cash_list[2] + 1
        elif(cash_price == 500):
            self.user_cash_list[3] = self.user_cash_list[3] + 1
        elif(cash_price == 1000):
            self.user_cash_list[4] = self.user_cash_list[4] + 1
        elif(cash_price == 0):
            self.user_cash_list = [0, 0, 0, 0, 0]
        # ここでお金が投入されるまいに購入可能商品のチェックをする
        self.display_now_cash: int = self.user_cash_list[0] * 10 + self.user_cash_list[1] * 50 + self.user_cash_list[2] * 100 + self.user_cash_list[3] * 500 + self.user_cash_list[4] * 1000


    def connection_with_db_cash(self) -> None:
        my_db = VendingMachineDB()
        # 複数の文のｓｑｌを実行するとエラるよ, まとめて書きましょう.
        my_db.execute_the_query("""UPDATE `cash_tb` SET cash_num=cash_num-{} WHERE cash_price=10;
                                    UPDATE `cash_tb` SET cash_num=cash_num-{} WHERE cash_price=50;
                                    UPDATE `cash_tb` SET cash_num=cash_num-{} WHERE cash_price=100;
                                    UPDATE `cash_tb` SET cash_num=cash_num-{} WHERE cash_price=500;
                                    UPDATE `cash_tb` SET cash_num=cash_num-{} WHERE cash_price=1000;
                                    """.format(self.user_cash_list[0], self.user_cash_list[1], self.user_cash_list[2], self.user_cash_list[3], self.user_cash_list[4]))
        del my_db


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
    
    def show_table_all(self, tb_name:str):
        result: list = []
        try:
            self.cursor.execute("SELECT * FROM {};".format(tb_name))
            data = self.cursor.fetchall()
            if data != None:
                for d in data:
                    result.append(d)
            print("show_table_all: {}".format(result))
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
        
        
        