# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 14:17:25 2023

@author: Ruijie Li
"""

class LinkNode:                      	#单链表结点类
    def __init__(self,data=None): 		#构造方法
        self.data=data       		#data属性
        self.next=None                  	#next属性
        
        
class LinkList:                    #单链表类
    def __init__(self):              #构造方法
        self.head=LinkNode()          #头结点head
        self.head.next=None


    def CreateListF(self, a):	#头插法：由数组a整体建立单链表
        for i in range(0,len(a)):     	#循环建立数据结点s
            s=LinkNode(a[i])		#新建存放a[i]元素的结点s
            s.next=self.head.next	#将s结点插入到开始结点之前,头结点之后
            self.head.next=s




    def CreateListR(self, a):	#尾插法：由数组a整体建立单链表
        t=self.head			#t始终指向尾结点,开始时指向头结点
        for i in range(0,len(a)):	#循环建立数据结点s
            s=LinkNode(a[i])		#新建存放a[i]元素的结点s
            t.next=s			#将s结点插入t结点之后
            t=s
        ## 如果没有这个命令会怎么样    
        t.next=None			#将尾结点的next成员置为空  





    def geti(self, i):	    #返回序号为i的结点
        p=self.head
        j=-1
        while (j<i and p is not None):
            j+=1
            p=p.next
        return p
    
    
    def Add(self, e):		#在线性表的末尾添加一个元素e
        s=LinkNode(e)		       	#新建结点s
        p=self.head
        while p.next is not None:	#查找尾结点p
            p=p.next
            p.next=s;			#在尾结点之后插入结点s


    def getsize(self):                   	#返回长度
        p=self.head
        cnt=0
        while p.next is not None:		#找到尾结点为止
            cnt+=1
            p=p.next
        return cnt



    def __getitem__(self,i):                	#求序号为i的元素
        assert i>=0                          	#检测参数i正确性的断言
        p=self.geti(i)
        assert p is not None                  	#p不为空的检测
        return p.data

    def __setitem__(self, i, e):           	#设置序号为i的元素
        assert i>=0                        	#检测参数i正确性的断言
        p=self.geti(i)
        assert p is not None                  	#p不为空的检测
        p.data=e



    def GetNo(self,e):		#查找第一个为e的元素的序号
        j=0
        p=self.head.next
        while p is not None and p.data!=e:
            j+=1				#查找元素e
            p=p.next
        if p is None:
            return -1			#未找到时返回-1
        else:
            return j			#找到后返回其序号





My_list = LinkList()
a = [1,2,3,4]


My_list.CreateListF(a)


for i in range(len(a)+1):
    if i == 0:
        current_LinkNode = My_list.head
        print(current_LinkNode.data)
    else:
        current_LinkNode = current_LinkNode.next
        print(current_LinkNode.data)


'''
My_list = LinkList()
My_list.CreateListR(a)

for i in range(len(a)+1):
    if i == 0:
        current_LinkNode = My_list.head
        print(current_LinkNode.data)
    else:
        current_LinkNode = current_LinkNode.next
        print(current_LinkNode.data)
'''       
        
node_i = My_list.geti(1)        

My_list_cnt = My_list.getsize()    
print("链表长度为{}".format(My_list_cnt))  

print("线性表中序号为0的元素{}".format(My_list.__getitem__(0))) 
print("线性表中序号为1的元素{}".format(My_list.__getitem__(1))) 

    