from collections import deque

class Box:			#方块类
  def __init__(self,i1,j1):   	#构造方法
    self.i=i1			#方块的行号
    self.j=j1			#方块的列号
    self.pre=None		#前驱方块



def mgpath(xi,yi,xe,ye):        	#求(xi,yi)到(xe,ye)的一条迷宫路径
    global mg                     	#迷宫数组为全局变量 
    dx=[-1,0,1,0]                 	#x方向的偏移量
    dy=[0,1,0,-1]                 	#y方向的偏移量
    qu=deque()                    	#定义一个队列
    b=Box(xi,yi)			#建立入口结点b
    qu.appendleft(b)		#结点b进队
    mg[xi][yi]=-1			#进队方块mg值置为-1

    while len(qu)!=0:	  		#队不空时循环
        b=qu.pop()				#出队一个方块b
        if b.i==xe and b.j==ye:		#找到了出口,输出路径
            p=b                             	#从b出发回推导出迷宫路径并输出
            path=[]				#path存放逆路径
            while p!=None:			#找到入口为止
                path.append("["+str(p.i)+","+str(p.j)+"]")
                p=p.pre
            for i in range(len(path)-1,-1,-1):	#反向输出path得到正向路径
                print(path[i],end=' ')
            return True		      		#找到一条路径时返回True
   
        for di in range(4):  		#循环扫描每个相邻方位的方块
            i,j=b.i+dx[di],b.j+dy[di]       	#找b的di方位的相邻方块(i,j)
            if mg[i][j]==0:              	#找相邻可走方块
                b1=Box(i,j)			#建立后继方块结点b1
                b1.pre=b			#设置其前驱方块为b
                qu.appendleft(b1)		#b1进队
                mg[i][j]=-1			#进队的方块置为-1
    return False				#未找到任何路径时返回False


xi,yi=1,1
xe,ye=4,4
mg= [[1,1,1,1,1,1],
  [1,0,1,0,0,1],   
  [1,0,0,1,1,1],
  [1,0,1,0,0,1],    
  [1,0,0,0,0,1],
  [1,1,1,1,1,1]]
 
print("一条迷宫路径:",end=' ')
if not mgpath(xi,yi,xe,ye):		#(1,1)->(4,4)
    print("不存在迷宫路径")
print()
