Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'hello'"world"'python'
'helloworldpython'
a="hello""world"'python'
a
'helloworldpython'
type(a)
<class 'str'>
a=23,7.9,'python',(5+8j),'c')
SyntaxError: unmatched ')'
a=23,7.9,'python',(5+8j),'c'
a
(23, 7.9, 'python', (5+8j), 'c')
a
(23, 7.9, 'python', (5+8j), 'c')
a=(5)
b=(5.8)
c=('hello')
type(a)
<class 'int'>
a=(5,)
type(a)
<class 'tuple'>
type(lst)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    type(lst)
NameError: name 'lst' is not defined. Did you mean: 'list'?
lst=[10,20,'window',45,3,8,4]
type(lst)
<class 'list'>
lst.append(15)
lst.append(10)
lst
[10, 20, 'window', 45, 3, 8, 4, 15, 10]
lst.append('python')
lst
[10, 20, 'window', 45, 3, 8, 4, 15, 10, 'python']
lst.clear()
lst
[]
lst=[10,20,'window',45,3,8,4]
lst.count(15)
0
lst.count(25)
0
lst.count('python')
0
lst=[10,20,'window',45,3,8,4]
list.count(15)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    list.count(15)
TypeError: descriptor 'count' for 'list' objects doesn't apply to a 'int' object
lst1=[10,20,'window',45,3,8,4]
lst1.count(15)
0
lst1.count(25)
0
lst1.count('python')
0
len(lst)