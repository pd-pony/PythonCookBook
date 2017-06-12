#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : files_and_IO.py
# @Software: PyCharm

# 文件与IO

# 1.1 读写文本数据
# 使用带有rt 模式的open() 函数读取文本文件
with open('test.txt', 'rt') as f:
    data = f.read()
    print(data)

with open('test.txt', 'rt') as f:
    for line in f:
        print(line)
# 写入一个文本文件，使用带有wt 模式的open() 函数，如果之前文
# 件内容存在则清除并覆盖掉
with open('test.txt', 'wt') as f:
    f.write('wit open as f:')
    f.write('hello python')
with open('test.txt', 'rt') as f:
    for line in f:
        print(line)
# 读写文本文件一般来讲是比较简单的。但是也几点是需要注意的。首先，在例子程
# 序中的with 语句给被使用到的文件创建了一个上下文环境，但with 控制块结束时，
# 文件会自动关闭。你也可以不使用with 语句，但是这时候你就必须记得手动关闭文
# 件
f = open('test.txt', 'rt')
data = f.read()
f.close()

# 1.2 打印输出至文件中
# 将print() 函数的输出重定向到一个文件中去
with open('test.txt', 'wt') as f: # 此处可以指定路径d:/work/test.txt等等
    print('Hello World!', file=f)
f = open('test.txt', 'rt')
data = f.read()
print(data)

# 1.3 使用其他分隔符或行终止符打印
# 使用在print() 函数中使用sep 和end 关键字参数，以你想要的方式输出
print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=',')
print('ACME', 50, 91.5, sep=',', end='!!\n')
# 使用end 参数也可以在输出中禁止换行
for i in range(5):
    print(i, end= ' ')

# 1.4 字符串的I/O操作
# 使用操作类文件对象的程序来操作文本或二进制字符串
# 使用io.StringIO() 和io.BytesIO() 类来创建类文件对象操作字符串数据
import io
s = io.StringIO()
print(s.write('Hello World\n'))
print('This is a test', file=s)
print(s.getvalue())
s = io.StringIO('Hello\nWorld\n')
print(s.read(4))
print(s.read())
# io.StringIO 只能用于文本,如果你要操作二进制数据，要使用io.BytesIO 类来代替
s = io.BytesIO()
s.write(b'binary data')
print(s.getvalue())

# 1.5 读写压缩文件
# gzip 和bz2 模块可以很容易的处理这些文件
# 读取文件
import gzip
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()
import bz2
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()
# 写入数据
import gzip
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)
import bz2
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)

# 1.6 文件路径名的操作
# 使用路径名来获取文件名，目录名，绝对路径等等。
import os
path = '/Users/beazley/Data/data.csv'
# 获取文件名及其类型
print(os.path.basename(path))
# 获取路径及文件名
print(os.path.dirname(path))
# 在路径中加入分支
print(os.path.join('tmp', 'data', os.path.basename(path)))
# 扩展路径
path = '~/Data/data.csv'
print(os.path.expanduser(path))

# 1.7 测试文件是否存在
# 使用os.path 模块来测试一个文件或目录是否存在
import os
print(os.path.exists('/etc/passwd'))
print(os.path.exists('~/test'))
print(os.path.isfile('/etc/passwd'))
print(os.path.isdir('/etc/passwd'))
print(os.path.islink('/usr/local/bin/python3'))
# 获取文件大小
print(os.path.getsize('/etc/passwd'))
# 获取文件修改时间
print(os.path.getmtime('/etc/passwd'))

# 1.8 获取文件夹中的文件列表
# 使用os.listdir() 函数来获取某个目录中的文件列表
import os
names = os.listdir('somedir')

# 1.9  创建临时文件和文件夹
# tempfile 模块中有很多的函数可以完成这任务。为了创建一个匿名的临时文件，
# 可以使用tempfile.TemporaryFile
from tempfile import TemporaryFile
with TemporaryFile('w+t') as f:
    # Read/write to the file
    f.write('Hello World\n')
    f.write('Testing\n')
    # Seek back to beginning and read the data
    f.seek(0)
    data = f.read()