# -*- coding:utf-8 -*-
'''
sum=0
# num=[9,8,7,6,5,4,3,2,1]
num=list(range(101))
for x in num:
    sum=sum+x
print(sum)
'''
'''
sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
print(sum)
'''
'''
n = 1
while n <= 10:
   if n > 5:
       break
    print(n)
    n = n + 1
print('end')
我写的报错
'''
'''
n = 1
while n <= 100:
    if n > 10: 
        break 
    print(n)
    n = n + 1
print('END')
我复制的不报错
'''
'''
n=0
while n<10:
    n=n+1
    print(n)
'''
'''
n1=255
n2=1000
h=hex
print(h(n1))
print(h(n2))

print(hex(255))
print(hex(1000))
'''
'''
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))

def no():
    pass
'''
'''
import math

def move(x,y,step,angle=0):
    nx = x+step*math.cos(angle)
    ny = y-step*math.sin(angle)
    return nx,ny
print(move(100,100,60,math.pi/6))
'''
'''
18.10.22表达式报错
import math
def quadratic(a,b,c,x1,x2):
    a*x*x+b*x+c=0
    return a,b,c
print(x1,x2)
'''
'''
def power(x):
    return x*x
print(power(5))

def power2(x,n=2):
    s=1
    while n>0:
        s=s*x
        n=n-1
    return s
print(power2(5,3))
print(power2(5))
'''
'''
def e(L=None):
    if L is None:
        L=[]
    L.append('end')
    return L
a=e()
print(a)
print(e(a))
'''
'''
def cal(*list):
    sum =0
    for n in list:
        sum =sum+ n*n
    return sum
l=[1,2,3,5]
# zn=cal(l[0],l[1],l[2],l[3])
print(cal(*l))
'''
'''
 #关键字参数  
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('zn',20)
person('cxy',200,city='dalian')
person('kexin',20,gender='m',job='ceo')
'''
'''
def person(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456,job='cto')
'''
'''
def person(name,age,*,city,job):
    print(name,age,city,job)
person('jack',24,city='beijing',job='engineer')
'''
'''
def person(name,age,*args,city,job):
    print(name,age,args,city,job)
person('jack',24,(10),city='beijing',job='engineer')
'''
'''
#多数相乘
def product(x,*nums):
    sum=1
    for n in nums:
        sum =sum*n
        return x*sum
l=product(2,3)
print(l)
'''
'''
#多数相乘
def product(*numbers):
    mult = 1
    for n in numbers:
        mult = mult*n
    return mult
print(product(5,6))
'''
'''
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(1000))
'''
'''
def fact(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num-1,num*product)

print(fact(1000))
'''
'''
# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print( a, '-->', c)
    else:
        move(n-1, a, c, b)
        print(a, '-->', c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')
'''
'''
#循环取出前三个元素
L=['a','b','c','d','e']
n=3
r=[]
for i in range(n):
    r.append(L[i])
print(r)
'''
'''
#切片方法取前3个元素
L=['a','b','c','d','e']
print(L[0:3])
print(L[:3])
'''
'''
l=list(range(100))
print(l)
print(l[:10])
print(l[-10:])
print(l[0:10:2]) #0-9能被2整除的
print(l[0:10:3]) #0-9能被3整除的
print(l[:])
'''
# l=(0,1,2,3,4,5)[:3]
# print(l)
'''
#使用切片去除字符串前后空格
def trim(s:str)->str:
    ret = ''
    left ,right = -1, -1
    for index in range(len(s)):
        if s[index] != ' ' and left == -1:
            left = index
        if s[len(s)-index-1] != ' ' and right == -1:
            right = len(s)-index
        if left != -1 and right != -1:
            break
    ret = s[left:right]
    return ret

if trim('hello  ') != 'hello':
    print('33')
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('22')
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('11')
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('00')
    print('测试失败!')
elif trim('') != '':
    print('12')
    print('测试失败!')
elif trim('    ') != '':
    print('..')
    print('测试失败!')
else:
    print('测试成功!')
'''
'''
d={'a':1,'b':2,'c':3}
for key in d:
    print(key)
for ch in 'ABC':
    print(ch)
'''
'''
for i,value in enumerate([1,2,3]):
    print(i,value)
for x,y in [(1,1),(2,4),(3,9)]:
    print(x,y)
'''
'''
#迭代查找一个list中最小和最大值，并返回一个tuple
#方式1
def findMinAndMax(L):
    if len(L)==0 :
        return (None,None)
    else:
        max = L[0]
        min = L[0]
        for i in L:
            if i > max:
                max = i
            if i < min:
                min = i
        return (min,max)   
#方式2
def findMinAndMax(L):
    if L != []:
        max = L[0]
        min = L[0]
        for l in L:
            if max < l:
                max = l
            if min > l:
                min = l
        return (min, max)
    else:
        return (None, None)
#测试用例
if findMinAndMax([]) != (None, None):
    print('测试失败1!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败2!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败3!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败4!')
else:
    print('测试成功!')
'''
'''
l= list(range(1,11))
print(l)

l=[]
for x in range(1,11):
    l.append(x*x)
print(l)
#列表生成式代替上面的循环
a=[x*x for x in range(1,11)]
print(a)

b=[x*x for x in range(1,11) if x%2 ==0]
print(b)

b=[m+n for m in range(1,3) for n in range(1,3)]
print(b)

c=[m+n for m in 'zn' for n in 'cxy']
print(c)
'''
'''
import os
l=[d for d in os.listdir('.')]
print(l)
'''
'''
d={'x':'a','y':'b','z':'c'}
for k,v in d.items():
    print(k,"=",v)
'''
'''
d={'x':'a','y':'b','z':'c'}
l= [k+'='+v for k,v in d.items()]
print(l)

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])
'''
'''
#list中既包含字符串，又包含整数,把字母变为小写
L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[s.lower() for s in L1 if isinstance(s,str)==True]
#测试用例
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
'''
'''
l=[x*x for x in range(10)]
print(l)

g= (x*x for x in range(10))
for n in g:
    print(n)
'''
'''
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'
print(fib(5))
'''
'''
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a=b
        b=a+b
        n=n+1
    return 'done'
g=fib(6)
while True:
    try:
        x=next(g)
        print('g=',x)
    except StopIteration as e:
        print('return value:',e.value)
        break

def odd():
    print('1')
    yield 1
    print('2')
    yield (3)
    print('3')
    yield (5)
o=odd()
print(next(o))
print(next(o))
print(next(o))
'''
'''
s = (x * x for x in range(5))
print(s)
for x in s:
    print(x)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)

# call generator manually:
g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
'''
'''
for x in [1,2,3,4,5]:
    pass
print(x)

it = iter([1,2,3,4,5])
while True:
    try:
        x=next(it)
    except StopIteration:
        break
print(x)
'''
'''
def f(x):
    return x*x
#r=map(f,[1,2,3,4])
#a=list(r)
#print(a)

l=[]
for n in[1,2,3,4]:
    l.append(f(n))
print(l)

s=list(map(str,[1,2,3,4]))
print(s)
'''
'''
from functools import reduce
def add(x,y):
    return x+y
a=reduce(add,[1,3,5])
print(a)

print(sum([1,3,5]))
'''
'''
from functools import reduce
def f(x,y):
    return x*10+y
sum=reduce(f,[1,2,4])
print(sum)
'''
'''
########string to int
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
       return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
print(str2int('34'))    
'''
'''
#变为首字母大写，其他小写的规范名字
from functools import reduce
def normalize(name):
    name=name[0].upper()+name[1:].lower()
    return name
#测试用例
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
'''

''' 
from functools import reduce
def prod(L):
    return reduce(lambda x, y: x*y, L)
print(prod([3, 5, 7, 9]))
'''
'''
#编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce
def prod(L):
    def f(x,y):
        return x*y
    return reduce(f,L)
print(prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
'''
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2float(s):
    def f(x,y):
        return x*10+y
    
    def chartonum(s):
        return DIGITS[s]
    return reduce(f,map(chartonum,s.replace('.','')))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

































