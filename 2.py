'''
#filter()内置函数
def id_odd(n):
    return n % 2==0
l=list(filter(id_odd,range(0,15)))
print(l)
#删除序列中空字符串
def not_empty(s):
    return s and s.strip()
l=list(filter(not_empty,['a','','b',None,'c',' ']))
print(l)
#用filter求素数
def su():
    n=1
    while True:
        n+=2
        yield n     #n=3
def shaixuan(n):
    return lambda x: x%n>0
def shengchengqi():
    yield 2
    startnum= su()
    while True:
        n=next(startnum)
        yield n
        startnum = filter(shaixuan(n),startnum)

for n in shengchengqi():
    if n<1000:
        print(n)
    else:
        break
#筛选出回数例如12321，909
def is_palindrome(n):
    str(n)==str(n)[::-1]
    return str(n)==str(n)[::-1]
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
'''
'''
#sorted()内置函数
l=sorted([1,4,-4,6,0])
print(l)
l=sorted([1,3,-4,5,-6],key=abs)
print(l)
l=sorted(['A','Z','a','zn','cxy','zhy'])
print(l)
l=sorted(['A','Z','a','zn','cxy','zhy'],key=str.lower)
print(l)
l=sorted(['A','Z','a','zn','cxy','zhy'],key=str.lower,reverse=True)
print(l)

from operator import itemgetter
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)] 
#按人名排序
a=sorted(L,key=itemgetter(0))
print(a)
#按成绩排序{低到高}
b=sorted(L,key=itemgetter(1))
print(b)
#按成绩排序{低到高}
c=sorted(L,key=itemgetter(1),reverse=True)
print(c)
'''
'''
#return 
def createCounter():
    def counter(x):
        def g():
            return x+1
        return g
    f=[]
    for i in range(1,6):
        f.append(counter(i))
    return f      

def count():
    fs = []
    def f(n):
        def j():
            return n * n
        return j
    for i in range(1, 4):
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
'''
'''
#lambda表达式
f=lambda x:x*x
print(f(2))

def is_odd(n):
    return n%2==1
l=list(filter(is_odd,range(1,20)))
print(l)
L=list(filter(lambda n:n%2==1,range(1,20)))
print(L)
'''
'''
def now():
    print('zn')
f=now
print(f())
print(now.__name__)
print(f.__name__)

def log(func):
    def w(*args,**kw):
        print('call %s():'%func.__name__)
        return func(*args,**kw)
    return w
@log
def now():
    print('20181025')
now = log(now)
print(now())
'''
'''
#偏函数,传入base参数，就可以做N进制的转换
l=int('12345',base=16)
print(l)
#二进制转十进制
def int2(x,base=2):
    return int(x,base)
print(int2('101'))
#二进制转十进制换一种实现
import functools 
#functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数
int2=functools.partial(int,base=2)
print(int2('111'))
print(int2('111',base=2))

args=(10,2,3,4)
print(max(*args))
'''
'test'
'''
def zn():
    l=[]
    for x in range(1,100,2):
        l.append(x*(x+1))
        print(l[len(l)-1])

print(zn())
'''
'''
try:
    print('try---')
    r=10/2
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('END____')

try:
    print('try...')
    r=10/int('a')
    print('result:',r)
except ValueError as e:
    print('ValueError:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
finally:
    print('finally...')
print('END')
'''
'''
from functools import reduce

def str2num(s):
    return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()

class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
d=dict(a=1,b=2)
print(d['a'])
print(d)

import unittest

from mydict import Dict

class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
if __name__ == '__main__':
    unittest.main()
'''
'''
import unittest
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score>100 or self.score<0:
            raise ValueError("the score is wrong!")
        if 80>self.score >= 60:
            return 'B'
        if self.score >= 80:
            return 'A'
        return 'C'
        

class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        print(s1.get_grade())
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

if __name__ == '__main__':
    unittest.main()
'''
'''
#读取文件内容并关闭文件方法1
try:
    f=open("C:/Users/zn/Desktop/hexo.txt",'r')
    print(f.read())
finally:
    if f:
        f.close()

#读取文件内容并关闭文件方法2
with open("C:/Users/zn/Desktop/hexo.txt",'r') as f:
    print(f.read())

#读取图片,视频用'rb'
with open("C:/Users/zn/Desktop/1.png",'rb') as f:
    print(f.read())  
#读取非Utf-8编码的文本文件用'gbk'
'''
'''
#写文件'w'，会覆盖原有文件内容，'a'追加到文件中，不覆盖

with open("/Users/zn/Desktop/test.txt",'w') as f:
    f.write('hello zn')
'''
'''
#StringIO
#内容中写str
from io import StringIO
f=StringIO()
f.write('hello')
f.write('  ')
f.write('world')
print(f.getvalue())
#内存中读str
from io import StringIO
f=StringIO('hello\nnihaoa\nbye')
while True:
    s=f.readline()
    if s=="":
        break
    print(s.strip())
#BytesIO[只能操作str]
#写
from io import BytesIO
f=BytesIO()
a=f.write('中国'.encode('utf-8'))
print(a)
print(f.getvalue())
#读
from io import BytesIO
f=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
'''
'''
import os
#print(os.name)
#print(os.environ)
#print(os.environ.get('PATH'))
#print(os.environ.get('x','default'))
#print(os.path.abspath('.'))
#print(os.path.join('/Users/zn/Desktop','testdir'))
#print(os.mkdir('/Users/zn/Desktop/testdir'))
#print(os.rmdir('/Users/zn/Desktop/testdir'))
#print(os.rename('test.txt','test.py'))
#要列出所有的.py文件
a=[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(a)
'''
'''
#json序列化，反序列化
import json
d=dict(name='Bob',age=20,score=88)
print(json.dumps(d))
#输出{"name": "Bob", "age": 20, "score": 88}
json_str='{"age":20,"score":88,"name":"bob"}'
print(json.loads(json_str))
'''
'''
import json

class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
s=Student('Bob',20,88)
def student2dic(std):
    return{
        'name':std.name,
        'age':std.age,
        'score':std.score
    }
print(json.dumps(s,default=student2dic))
'''
'''
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
'''







