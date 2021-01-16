import numpy as np
import random


class Chess():

    def __init__(self):      
        self.l=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.score=0
    def firstchess(self): #初始化生成两个数       
        self.n1,self.n2=random.sample(range(0,16),2)
        self.l[int(self.n1)]=2
        self.l[int(self.n2)]=2
        return self.l

    def creartnum(self): #生成一个数        
        while True:            
            self.num=random.randint(0,15)
            if self.l[self.num]==0:
                self.l[self.num]=random.choice([2,4])               
                break
            
        return self.l

    def rightmove(self):
        x=np.array(self.l).reshape(4,4)
        # print(f'第1次的x是{self.l}')
        x=x[:,::-1]
        self.l=x.reshape(16)
        # print(f'第2次的x是{x}')
        # print(f'第2次的l是{self.l}')
        self.leftmove()
        y=np.array(self.l).reshape(4,4)
        # print(f'第1次的x是{self.l}')
        y=y[:,::-1]
        self.l=y.reshape(16)


    def leftmove(self):   #[2,2,0,2]->[4,2]

        for y in range(0,4):
            m=[]            
            for i in range(0,4):
                if self.l[y*4+i]!=0:
                    m.append(self.l[y*4+i])
            # print(f'这里是m{m},y是{y}')

            if len(m)==0:
                continue

            elif len(m)==1:
                while len(m)<4:
                    m.append(0)
                for i in range(0,4):
                    self.l[y*4+i]=m[i]

            else:
                for x in range(0,len(m)-1):
                    

                    if m[x]==m[x+1]:
                        m[x]=m[x]*2
                        m[x+1]=0                
                # print(f'这时候是m是{m},x是{x}')

                if m[1]==0:
                    m.pop(1)

                
                while len(m)<4:
                    m.append(0)

                for i in range(0,4):
                    self.l[y*4+i]=m[i]
        
        # print('*'*50)

    def upmove(self):
        x=np.array(self.l).reshape(4,4)
        
        x=np.transpose(x)
        self.l=x.reshape(16)

        self.leftmove()
        y=np.array(self.l).reshape(4,4)
        
        y=np.transpose(y)
        self.l=y.reshape(16)
    def downmove(self):
        x=np.array(self.l).reshape(4,4)
        
        x=np.transpose(x)
        x=x[::,::-1]
        self.l=x.reshape(16)

        self.leftmove()
        y=np.array(self.l).reshape(4,4)
        
        y=np.transpose(y)
        y=y[::,::-1]
        self.l=y.reshape(16)

    def win_game(self):
        for i in range(0,len(self.l)):
            if self.l[i]==2048:                
                return True
        return False
    def lose_game(self):
        ss=[]
        for i in range(0,len(self.l)):
            if self.l[i]==0:
                ss.append(self.l[i])

        if len(ss)==0:
            return True
        else:
            return False
            
    def restart(self):
        self.n1,self.n2=random.sample(range(0,16),2)
        self.l[int(self.n1)]=2
        self.l[int(self.n2)]=2
        self.drawchess() 
        

    def drawchess(self):
        print('-'*22)
        print(f'{self.l[0]}      {self.l[1]}      {self.l[2]}      {self.l[3]}')
        print('-'*22)
        print(f'{self.l[4]}      {self.l[5]}      {self.l[6]}      {self.l[7]}')
        print('-'*22)
        print(f'{self.l[8]}      {self.l[9]}      {self.l[10]}      {self.l[11]}')
        print('-'*22)
        print(f'{self.l[12]}      {self.l[13]}      {self.l[14]}      {self.l[15]}')
        print('-'*22)
        print(f'SCORE:{self.score}')
        
    def starts(self):
        self.restart()
        while True:
            if self.win_game():
                print('YOU WIN!!!')
                break
            elif self.lose_game():
                print('YOU LOSE!!!')
                break
             
            self.keys=input('选择a d w s移动，q退出，请输入：')           
            if self.keys=='a':
                self.leftmove()
            elif self.keys=='d':
                self.rightmove()
            elif self.keys=='w':
                self.upmove()
            elif self.keys=='s':
                self.downmove()
            elif self.keys=='q':
                exit('退出')
            elif self.keys=='r':
                self.restart()
            else:                
                print('你的输入有误，请重新输入：')
            
            self.creartnum()
            self.drawchess() 

if __name__ == "__main__":      
    chess=Chess()
    chess.starts()
