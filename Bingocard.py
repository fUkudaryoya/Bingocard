import tkinter as tk
import random

class BingoCard:
    def __init__(self,root):
        self.root=root
        self.root.title("Bingo Card")
        
        
        self.bingo_message=tk.Label(self.root,text="",font=("Arial", 16),fg="red")
        self.bingo_message.grid(row=0,column=0,columnspan=5)

        self.selected=[[False]*5 for _ in range(5)]  
        self.card_numbers=self.generate_card()
        self.buttons=[]  
        self.create_grid()

    def generate_card(self):
        
        card=[]
        ranges=[(1,15),(16,30),(31,45),(46,60),(61,75)]  

        for col in ranges:
            start,end=col
            column=random.sample(range(start,end+1),5)  
            card.append(column)

        card[2][2]="Bingo"  
        return list(map(list,zip(*card)))  # 行と列を入れ替える

    def create_grid(self):
        
        for i in range(5):
            row_buttons=[]
            for j in range(5):
                btn_text=self.card_numbers[i][j]
                btn=tk.Button(self.root,text=btn_text,width=5,height=2,command=lambda i=i,j=j:self.select_number(i,j))
                btn.grid(row=i+1,column=j)  
                
                
                if i==2 and j==2:
                    btn.config(bg="gray",text="")  
                    self.selected[i][j]=True

                row_buttons.append(btn)
            self.buttons.append(row_buttons)

    def select_number(self,row,col):
        if not self.selected[row][col]:  
            self.selected[row][col]=True  
            self.buttons[row][col].config(bg="gray",text="")  
        self.check_bingo_or_reach()

    def check_bingo_or_reach(self):
        
        for i in range(5):
            if self.is_bingo(self.selected[i]) or self.is_bingo([self.selected[j][i] for j in range(5)]):
                self.show_bingo_message()  
            elif self.is_reach(self.selected[i]) or self.is_reach([self.selected[j][i] for j in range(5)]):
                self.show_reach_message()  

        
        if self.is_bingo([self.selected[i][i] for i in range(5)]) or self.is_bingo([self.selected[i][4-i] for i in range(5)]):
            self.show_bingo_message()  
        elif self.is_reach([self.selected[i][i] for i in range(5)]) or self.is_reach([self.selected[i][4-i] for i in range(5)]):
            self.show_reach_message()  

    def is_bingo(self,line):
        
        return all(line)  

    def is_reach(self,line):
        
        return line.count(True)==4 and line.count(False)==1  

    def show_bingo_message(self):
        
        self.bingo_message.config(text="ビンゴ！")

    def show_reach_message(self):
        
        self.bingo_message.config(text="リーチ！")

if __name__=="__main__":
    root=tk.Tk()
    BingoCard(root)
    root.mainloop()









