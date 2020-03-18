
# -*- coding: utf-8 -*-：
# -*-coding:gbk-*
# *创建文件，写入数据 * #


from sys import argv

script, filename = argv

print "we are going to erase %r." % filename
print "if you don't want that, hit ctrl-C(^C)."
print "if you do want that, hit ENTER."

raw_input('?')

print "opening the file..."
target = open(filename, 'w')
print "truncating the file. Goodbye!"
target.truncate()   # 清空文件
print "now I'm going to ask you for three lines."
line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write those to the file."
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print "and finally,we close it."
target.close()
