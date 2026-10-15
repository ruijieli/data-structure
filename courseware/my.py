class SqList:				#顺序表类
    def __init__(self):			#构造方法
        self.initcapacity=5;          	#初始容量设置为5
        self.capacity=self.initcapacity	#容量设置为初始容量
        self.data=[None]*self.capacity	#设置顺序表的空间
        self.size=0				#长度设置为0


    def resize(self, newcapacity):	#改变顺序表的容量为newcapacity
        assert newcapacity>=0		#检测参数正确性的断言
        olddata=self.data
        self.data=[None]*newcapacity
        self.capacity=newcapacity
        for i in range(self.size):
            self.data[i]=olddata[i]



    def Insert(self, i, e):               	#在线性表中序号i位置插入元素e
        assert 0<=i<=self.size           	#检测参数i正确性的断言
        if self.size==self.capacity:		#满时倍增容量
            self.resize(2*self.size)
        for j in range(self.size,i-1,-1):	#将data[i]及后面元素后移一个位置
            self.data[j]=self.data[j-1]
            self.data[i]=e			        	#插入元素e
            self.size+=1				#长度增1


    def MyAdd(self, e): 			#在线性表的末尾添加一个元素e
        if self.size==self.capacity:		#顺序表空间满时倍增容量
            self.resize(self.capacity+len(e))
        for i in range(0,len(e)):
            self.data[self.size]=e[i]			#添加元素e
            self.size+=1				#长度增1



L1 = SqList()
L2 = SqList()

L1.MyAdd([1,3,5,7,9])
L2.MyAdd([2,4,6,8,10])




      
    
