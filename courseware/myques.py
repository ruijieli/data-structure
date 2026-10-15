import random



class Child:	        		#结点类型
    def __init__(self,no1,HP):      	#构造方法
        self.no = no1                 	#编号no属性
        self.hp = HP                     # HP属性
        self.next=None              	#next属性



class Joseph:		    		#求解约瑟夫问题类
    def __init__(self, n1, m1, HP):       	#构造方法
        self.n=n1
        self.m=m1
        self.first=Child(1,HP);            	#循环单链表首结点
        t=self.first
        for i in range(2,self.n+1):
            p=Child(i,HP)			#建立一个编号为i的新结点p
            t.next=p				#将p结点链到末尾
            t=p
        t.next=self.first			#构成一个首结点为first的循环单链表


    def Jsequence(self):		#求约瑟夫序列
        for i in range(1,self.n+1):	#共出列n个小孩
            p=self.first			#每次都从first开始
            j=1
            tep = True            
            while tep:
                if (j+1)%self.m == 0:
                    q=p.next
                    tep = random.random()
                    print("当前随机数为{}".format(tep))
                    if tep< 0.5:
                        print("{}小于0.5，因此该小孩报数为错的，减少1滴血".format(tep))
                        tep = False
                        q.hp =  q.hp-1
                        if q.hp<=0:
                            print("血量为0，移除该小孩")
                            print(q.no,end=' ')
                            #self.first=p.next
                            p.next=q.next
                    else:
                        print("{}大于等于0.5，因此该该小孩报数为对的".format(tep))
                        j+=1
                        p=p.next
                else:
                    j+=1
                    p=p.next
            self.first=p.next        

        print()



        

n=10
m=4
HP = 1
L=Joseph(n,m, HP)
print("n=%d，m=%d的约瑟夫序列:" %(n,m))
L.Jsequence()
