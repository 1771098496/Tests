# del 删除
# 如果使用del之后，id的值和删除前不一样，则说明删除生成了一个新的列表
a = [1,2,3,4,5,6]
print(id(a))
del a[2]
print(id(a))
print(a)

# 列表的遍历
b = [1,3,4,5]
for i in b:
    print(i)


# 双层列表嵌套
c = [["one",1,"eins"],["two",2,"zwei"],["three",3,"rei"]]
# 这个例子说明，k,v,w的个数应该跟解包出来的变量个数一致
for k,v,w in c:
    print(k,"---",v,"---",w)

# 使用for创建列表
a1 = [1,2,3,4]
# 使用list a1创建一个list b1
b1 = [i for i in a1]
b2 = [i*10 for i in a1]
print(b1)
print(b2)

a2 = [x for x in range(1,35)]
# 把a2中所有偶数生成一个新的列表b3
b3 = [m for m in a2 if m % 2 == 0]
print(b3)

# 列表生成式可以嵌套
a3 = [i for i in range(1,10)]
print(a3)

b4 = [i for i in range(100,1000) if i % 100 == 0]
print(b4)

c1 = [m+n for m in a3 for n in b4 if n % 100 == 0]
print(c1)
# for循环嵌套遍历
for m in a3:
    for n in b4:
        print(m+n,end="  ")
print("")
