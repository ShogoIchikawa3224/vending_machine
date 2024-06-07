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
        self.my_db = db.connect(host = "localhost", user = "root", password="", db = "vending_machine_db")
        self.my_db.ping(reconnect=True)
        print("is connected?: {}".format(self.my_db.is_connected()))
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
        self.cursor.close()
        self.my_db.close()
        print("database was closed.\n")     



app = vending_machine_UI()
        
        
        