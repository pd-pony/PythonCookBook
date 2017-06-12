#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : string_and_text.py
# @Software: PyCharm

# 字符串和文本

# 1.1 使用多个界定符分割字符串
# 问题：将一个字符串分割为多个字段，但是分隔符（还有周围的空格）并不是固定的
# 解决：string 对象的split() 方法只适应于非常简单的字符串分割情形，它并不允许有
# 多个分隔符或者是分隔符周围不确定的空格。当你需要更加灵活的切割字符串的时候，
# 最好使用re.split() 方法：
line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
print(re.split(r'[:,\s]\s*', line))
# 当你使用re.split() 函数时候，需要特别注意的是正则表达式中是否包含一个括
# 号捕获分组。如果使用了捕获分组，那么被匹配的文本也将出现在结果列表中
print(re.split(r'(;|,|\s)\s*', line))
# 带分隔符的字符数组
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
# 获取字符
values = fields[::2]
# 获取字符分隔符
delimiters = fields[1::2] + [' ']
print(values)
print(delimiters)
# 合并字符及分隔符
res = ''.join(v + d for v, d in zip(values, delimiters))
print(res)
# 如果你不想保留分割字符串到结果列表中去，但仍然需要使用到括号来分组正则表
# 达式的话，确保你的分组是非捕获分组，形如(?:...)
print(re.split(r'(?:,|;|\s)\s*', line))

# 1.2 字符串开头或结尾匹配
# 问题：通过指定的文本模式去检查字符串的开头或者结尾，比如文件名后缀，URL
# Scheme 等等
# 解决：检查字符串开头或结尾的一个简单方法是使用str.startswith() 或者是
# str.endswith() 方法。
filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file'))
url = 'http://www.python.org'
print(url.startswith('http:'))
# 如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去，然后传
# 给startswith() 或者endswith() 方法：
import os
filenames = os.listdir('.')
print(filenames)
# 输出所有以.py或.c为结尾的文件名
print([name for name in filenames if name.endswith(('.py', '.c'))])
# 判断所有文件是否都是以.py结尾
print(any(name.endswith('.py') for name in filenames))
# 这个方法中必须要输入一个元组作为参数。如果你恰巧有一个list 或
# 者set 类型的选择项，要确保传递参数前先调用tuple() 将其转换为元组类型
from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

# startswith() 和endswith() 方法提供了一个非常方便的方式去做字符串开头和
# 结尾的检查。类似的操作也可以使用切片来实现，但是代码看起来没有那么优雅
filename = 'spam.txt'
print(filename[-4:] == '.txt')

# 1.3 用shell通配符匹配字符串
# 问题：使用Unix Shell 中常用的通配符(比如*.py , Dat[0-9]*.csv 等) 去匹配文
# 本字符串
# 解决：fnmatch 模块提供了两个函数—— fnmatch() 和fnmatchcase() ，可以用来实现
# 这样的匹配
from fnmatch import fnmatch, fnmatchcase
print(fnmatch('foo,txt', '*txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])
# fnmatch() 函数使用底层操作系统的大小写敏感规则(不同的系统是不一样的) 来
# 匹配模式,如果你对这个区别很在意，可以使用fnmatchcase() 来代替。它完全使用你的模
# 式大小写匹配
print(fnmatchcase('foo.txt', '*.TXT'))

# 这两个函数通常会被忽略的一个特性是在处理非文件名的字符串时候它们也是很有用的
addresses = [
   '5412 N CLARK ST',
   '1060 W ADDISON ST',
   '1039 W GRANVILLE AVE',
   '2122 N CLARK ST',
   '4802 N BROADWAY',
]
from fnmatch import fnmatchcase
print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])

# 1.4 字符串匹配和搜索
# 如果你想匹配的是字面字符串，那么你通常只需要调用基本字符串方法就行，比如
# str.find() , str.endswith() , str.startswith() 或者类似的方法：
text = 'yeah, but no, but yeah, but no, but yeah'
print(text == 'yeah')
# 匹配开头
print(text.startswith('yeah'))
# 匹配结尾
print(text.endswith('no'))
# 查找关键字
print(text.find('no'))

# 对于复杂的匹配需要使用正则表达式和re 模块
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
import re
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')
if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')
# 如果你想使用同一个模式去做多次匹配，你应该先将模式字符串预编译为模式对象
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')
if datepat.match(text2):
    print('yes')
else:
    print('no')
# match() 总是从字符串开始去匹配，如果你想查找字符串任意部分的模式出现位
# 置，使用findall() 方法去代替
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))
# 在定义正则式的时候，通常会利用括号去捕获分组,捕获分组可以使得后面的处理更加简单，因为可以分别将每个组的内容提取出来
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.findall(text)
for month, dat, year in m:
    print('{}-{}-{}'.format(year, month, year))
print(m)
print(m[0])
n = datepat.match('11/27/2012')
print(n)
print(n.group(0))
# findall() 方法会搜索文本并以列表形式返回所有的匹配。如果你想以迭代方式返回匹配，可以使用finditer() 方法来代替
for a in datepat.finditer(text):
    print(a.groups())
# 使用re模块进行匹配和搜索文本的最基本方法。核心步骤就是先使用re.compile() 编译正则
# 表达式字符串，然后使用match() , findall() 或者finditer() 等方法

# 1.5 字符串搜索和替换
# 对于简单的字面模式，直接使用str.repalce() 方法即可
text = 'yeah, but no, but yeah, but no, but yeah'
new = text.replace('yeah', 'yep')
print(text)
print(new)
# 对于复杂的模式，请使用re 模块中的sub() 函数。为了说明这个，假设你想将形
# 式为11/27/2012 的日期字符串改成2012-11-27
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
new = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(new)
# sub() 函数中的第一个参数是被匹配的模式，第二个参数是替换模式。反斜杠数字
# 比如\3 指向前面模式的捕获组号。
# 如果你打算用相同的模式做多次替换，考虑先编译它来提升性能
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
text1 = datepat.sub(r'\3-\1-\2', text)
print(text1)
# 如果除了替换后的结果外，你还想知道有多少替换发生了，可以使用re.subn()来代替
newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext)
print(n)

# 1.6 字符串忽略大小写的搜索替换
# 为了在文本操作时忽略大小写，你需要在使用re 模块的时候给这些操作提供re.IGNORECASE 标志参数
import re
text = 'UPPER PYTHON, lower python, Mixed Python'
res = re.findall('python', text, flags=re.IGNORECASE)
print(res)
new = re.sub('python', 'snake', text, flags=re.IGNORECASE)
print(new)

# 1.7 最短匹配模式
import re
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))
# 在这个例子中，模式r'\"(.*)\"' 的意图是匹配被双引号包含的文本。但是在正
# 则表达式中* 操作符是贪婪的，因此匹配操作会查找最长的可能匹配。于是在第二个
# 例子中搜索text2 的时候返回结果并不是我们想要的。为了修正这个问题，可以在
# 模式中的* 操作符后面加上? 修饰符
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))
# 这样就使得匹配变成非贪婪模式，从而得到最短的匹配
# 这一节展示了在写包含点(.) 字符的正则表达式的时候遇到的一些常见问题。在一
# 个模式字符串中，点(.) 匹配除了换行外的任何字符。然而，如果你将点(.) 号放在开
# 始与结束符(比如引号) 之间的时候，那么匹配操作会查找符合模式的最长可能匹配。
# 这样通常会导致很多中间的被开始与结束符包含的文本被忽略掉，并最终被包含在匹
# 配结果字符串中返回。通过在* 或者+ 这样的操作符后面添加一个? 可以强制匹配算
# 法改成寻找最短的可能匹配。

# 1.8 将Unicode文本标准化
# 问题：处理Unicode 字符串，需要确保所有字符串在底层有相同的表示
# 解决：使用unicodedata 模块先将文本标准化
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
print(s1 == s2)
print(len(s1))
print(len(s2))

import unicodedata
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
print(ascii(t1))
t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t3 == t4)
print(ascii(t3))
# normalize() 第一个参数指定字符串标准化的方式。NFC 表示字符应该是整体组
# 成(比如可能的话就使用单一编码)，而NFD 表示字符应该分解为多个组合字符表示

# 1.9 删除字符串中不需要的字符
# 掉文本字符串开头，结尾或者中间不想要的字符，比如空白
# strip() 方法能用于删除开始或结尾的字符。lstrip() 和rstrip() 分别从左和
# 从右执行删除操作。默认情况下，这些方法会去除空白字符，但是你也可以指定其他字符
# 去掉空格
# 去掉首尾空格
s = ' hello world \n'
print(s.strip())
# 去掉左边空格
print(s.lstrip())
# 去掉右边空格
print(s.rstrip())
# 去掉指定字符
t = '-----hello====='
print(t.strip('-='))
print(t.lstrip('-'))
# 需要注意的是去除操作不会对字符串的中间的文本产生任何影响
s = ' hello      world \n'
print(s.strip())
# 如果你想处理中间的空格，那么你需要求助其他技术。比如使用replace() 方法
# 或者是用正则表达式替换
# 将空格替换成，
print(s.replace(' ', ','))
# 将空格替换成一个空格
import re
str = re.sub('\s+', ' ', s)
print(str)

# 1.10 字符串对齐
# 对于基本的字符串对齐操作，可以使用字符串的ljust() , rjust() 和center()方法,可填充
text = 'Hello World'
# 左对齐，20个字符
print(text.ljust(20))
print(text.ljust(20, '*'))
# 右对齐，20个字符
print(text.rjust(20))
print(text.rjust(20, '*'))
# 中间对齐，20个字符
print(text.center(20))
print(text.center(20, '*'))
# 函数format() 同样可以用来很容易的对齐字符串。你要做的就是使用<,> 或者 ˆ 字符后面紧跟一个指定的宽度
# 左对齐
print(format(text, '<20'))
print(format(text, '*<20'))
# 右对齐
print(format(text, '>20'))
print(format(text, '*>20'))
# 居中
print(format(text, '^20'))
print(format(text, '*^20'))
# 当格式化多个值的时候，这些格式代码也可以被用在format() 方法中
print('{:>10s} {:>10s}'.format('Hello', 'World'))
# format() 函数的一个好处是它不仅适用于字符串。它可以用来格式化任何值，使得它非常的通用
x = 1.2345
print(format(x, '>10'))
print(format(x, '^10.2f'))

# 1.11 合并拼接字符串
# 问题：将几个小的字符串合并为一个大的字符串
# 解决：想要合并的字符串是在一个序列或者iterable 中，那么最快的方式就是使用join() 方法
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
res = ' '.join(parts)
print(res)
res1 = ','.join(parts)
print(res1)
res2 = ''.join(parts)
print(res2)
# 最重要的需要引起注意的是，当我们使用加号(+) 操作符去连接大量的字符串的
# 时候是非常低效率的，因为加号连接会引起内存复制以及垃圾回收操作

# 1.12 字符串中插入变量
# 问题：创建一个内嵌变量的字符串，变量被它的值所表示的字符串替换掉
# 解决：Python 并没有对在字符串中简单替换变量值提供直接的支持。但是通过使用字符
# 串的format() 方法来解决这个问题
s = '{name} has {n} messages.'
print(s.format(name='Guido', n=37))
# 如果要被替换的变量能在变量域中找到，那么你可以结合使用format map()和vars()
name = 'Guido'
n = 37
print(s.format_map(vars()))
# vars() 还有一个有意思的特性就是它也适用于对象实例
class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n
a = Info('Guido',37)
print(s.format_map(vars(a)))
# format 和format map() 的一个缺陷就是它们并不能很好的处理变量缺失的情况

# 1.13 以指定列宽格式化字符串
# 使用textwrap 模块来格式化字符串的输出
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."
import textwrap
# 列宽70
print(textwrap.fill(s, 70))
# 列宽40
print(textwrap.fill(s, 40))
# 列宽40，首行缩进
print(textwrap.fill(s, 40, initial_indent='   '))
# 列宽40，除首行外缩进
print(textwrap.fill(s, 40, subsequent_indent='   '))
# 自动匹配终端大小，使用os.get terminal size() 方法来获取终端的大小尺寸
import os
num = os.get_terminal_size().columns
print(num)
print(textwrap.fill(s, num, subsequent_indent='   '))

# 1.14 字节字符串上的字符串操作
# 问题：字节字符串上执行普通的文本操作(比如移除，搜索和替换)
data = b'Hello World'
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))