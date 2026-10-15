
def Hanoi(n,X,Y,Z, count = 0):
    if n==1:			#只有一个盘片的情况
        count += 1
        #print("将第%d个盘片从%c移动到%c,步数%d" %(n,X,Z,count))
    else:				#有两个或多个盘片的情况
        count = Hanoi(n-1,X,Z,Y, count)
        count += 1
        #print("将第%d个盘片从%c移动到%c,步数%d" %(n,X,Z,count))
        count = Hanoi(n-1,Y,X,Z, count)

    return count


count = Hanoi(64,'X','Y','Z')  
print("一共移动了%d步" %(count))




