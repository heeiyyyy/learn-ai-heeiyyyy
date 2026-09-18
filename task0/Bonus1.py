#方法一传统逐个比较
line = input()
parts = line.split()
x = int(parts[0])
y = int(parts[1])
z = int(parts[2])

a = b = c = 0
if x >= y and x >= z:
    a = x
    if y >= z:
        b = y
        c = z
    else:
        b = z
        c = y
elif y >= x and y >= z:
    a = y
    if x >= z:
        b = x
        c = z
    else:
        b = z
        c = x
else:
    a = z
    if x >= y:
        b = x
        c = y
    else:
        b = y
        c = x
print(a, b, c)

#方法二运用sort函数
line = input()
p = line.split()
x = int(p[0])
y = int(p[1])
z = int(p[2])
ls=[x,y,z]
ls.sort(reverse=True)
for i in ls:
    print(i, end=' ')#试过直接print(ls)，会使输出结果是个列表，
    #故用for循环输出每个元素


#方法三使用min，max，sum函数
line = input()
p = line.split()
x = int(p[0])
y = int(p[1])
z = int(p[2])
ls=[x,y,z]
max1=max(ls)
min1=min(ls)
middle = sum(ls)-max1-min1
print(max1, middle, min1)

