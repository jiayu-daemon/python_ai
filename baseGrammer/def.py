"""
语法
Python 定义函数使用 def 关键字，一般格式如下：
def 函数名（参数列表）:
    函数体
"""
#!/usr/bin/python3

# 计算面积函数
def area(width, height):
    return width * height
 
def print_welcome(name):
    print("Welcome", name)

print_welcome("Runoob")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))

"""
参数传递
在 python 中，类型属于对象，变量是没有类型的
"""

# 可写函数说明
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4]);
   print ("函数内取值: ", mylist)
   return


# 调用changeme函数
mylist = [10,20,30];
changeme( mylist );
print ("函数外取值: ", mylist)


