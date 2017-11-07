#!/usr/bin/python3
 
list1 = ['Google', 'Runoob', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];

print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])


list = ['Google', 'Runoob', 1997, 2000]
 
print ("第三个元素为 : ", list[2])
list[2] = 2001
print ("更新后的第三个元素为 : ", list[2])

list = ['Google', 'Runoob', 1997, 2000]
print (list)
del list[2]
print ("删除第三个元素 : ", list)

L = []
for x in range(1,11):
	L.append(x*x)
print(L)

#列表生成式则可以用一行语句代替循环生成上面的list：
print([x * x for x in range(1, 11)])
#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
print([x * x for x in range(1,11) if x % 2 == 0])
#使用两层循环，可以生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])


