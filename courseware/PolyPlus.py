# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 15:04:46 2023

@author: Ruijie Li
"""

from operator import itemgetter

class PolyList:                 	#多项式顺序表类
    def __init__(self):	  	#构造方法
        self.data=[]               	#存放多项式项的列表
    
    def Add(self,e):                	#添加一个多项式项e
        self.data.append(e) 



    def CreateList(self,fname):    	#从fname文件中读取多项式数据并添加到data
        fin=open(fname,"r")
        n=int(fin.readline().strip())
        for i in range(n):
            print(i)
            p=fin.readline().strip().split()
            self.data.append([float(p[0]),int(p[1])])
        fin.close()


    def getsize(self):                  #求多项式的项数
        return len(self.data)
    
    
    def __getitem__(self,i):      	#求序号为i的元素
        return self.data[i]
    
    
    def getdata(self):             	#返回多项式列表
        return self.data
    
    def Sort(self):                #对data按指数递减排序
        self.data=sorted(self.data,key=itemgetter(1),reverse=True)



    def PolyAdd(self,B):             #当前多项式和多项式B的相加运算
        C=PolyList()                   #新建结果多项式顺序表
        m=len(self.data)		#多项式A的项数
        n=B.getsize()			#多项式B的项数
        i,j=0,0
        while i<m and j<n:
            print(i)
            print(j)
            p,q=self.data[i],B[j]
            if p[1]>q[1]:                #将较大指数的p项添加到C中
                C.Add(p)
                i+=1
            elif q[1]>p[1]:              #将较大指数的q项添加到C中
                C.Add(q)
                j+=1
            else:                        #两指数相同，即p[1]=q[1]
                k=p[0]+q[0]                #系数相加为k
                if (k!=0):                 #k不为0时添加相应项到C中
                    C.Add([k,p[1]])
                    i+=1
                    j+=1            
        while i<m:                	#将A余下的项添加到C中
            print(i)
            print(j)
            p=self.data[i]
            C.Add(p)
            i+=1
        while j<n:                  	#将B余下的项添加到C中
            print(i)
            print(j)
            q=B[j]
            C.Add(q)
            j+=1
        return C
   
    
    
fout=open("out.txt","w+")
p=PolyList()                         	#创建第1个多项式顺序表p
p.CreateList("abc1.txt")
print("第1个多项式:",end=' ',file=fout)	#输出结果写入到abc.out文件中
print(p.getdata(),file=fout)
p.Sort()                              	#第1个多项式顺序表按指数递减排序
print("排序后结果: ",end=' ',file=fout)
print(p.getdata(),file=fout)
q=PolyList()                          	#创建第2个多项式顺序表q
q.CreateList("abc2.txt")
print("第2个多项式:",end=' ',file=fout)
print(q.getdata(),file=fout)
q.Sort()                              	#第2个多项式顺序表按指数递减排序
print("排序后结果: ",end=' ',file=fout)
print(q.getdata(),file=fout)
r=p.PolyAdd(q)                        	#r=p+q
print("相加多项式: ",end=' ',file=fout)
print(r.getdata(),file=fout)
fout.close()
    
    
    
    
    