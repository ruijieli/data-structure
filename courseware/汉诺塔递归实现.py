def Hanoi(n,X,Y,Z):         	#Hanoi递归算法
    count = 0
    if n==1:			#只有一个盘片的情况
        print("将第%d个盘片从%c移动到%c" %(n,X,Z))
        count = count +1
    else:				#有两个或多个盘片的情况
        Hanoi(n-1,X,Z,Y)
        print("将第%d个盘片从%c移动到%c" %(n,X,Z))
        count = count +1
        Hanoi(n-1,Y,X,Z)
    return  count



count = Hanoi(2,'X','Y','Z') 
print(count) 