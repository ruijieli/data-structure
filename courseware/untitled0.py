# -*- coding: utf-8 -*-
"""
Created on Mon May 22 13:52:11 2023

@author: Ruijie Li
"""
#import numpy as np

def move(n, a, buffer, c):
    if(n == 1):
        print(a,"->",c)
        return
    move(n-1, a, c, buffer)
    move(1, a, buffer, c)
    move(n-1, buffer, a, c)
move(10, "a", "b", "c")


def Hanoi(n,X,Y,Z):            	#Hanoi递归算法
    if n==1:			#只有一个盘片的情况
        print("将第%d个盘片从%c移动到%c" %(n,X,Z))
    else:				#有两个或多个盘片的情况
        Hanoi(n-1,X,Z,Y)
        print("将第%d个盘片从%c移动到%c" %(n,X,Z))
        Hanoi(n-1,Y,X,Z)

Hanoi(9,'X','Y','Z')






    
    
    
    
    

