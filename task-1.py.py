Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # question 2
>>> 5**9
1953125
>>> 3//2
1
>>> 7/3
2.3333333333333335
>>> 6==6
True
>>> a = 20; a+= 30; a%=3; print(a)
2
>>> True * False
0
>>> True & False
False
>>> True and False
False
>>> ((6>3) and (7<4) or (18==3)) and (9>3)
False
>>> True is False
False
>>> False in 'False'
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    False in 'False'
TypeError: 'in <string>' requires string as left operand, not bool
>>> ((True == False) or (False > True)) and (False <= True)
False
>>> # question 3
>>> s1 = "Nice to have it"
>>> s2 = "here"
>>> s1 + s2
'Nice to have ithere'
>>> # question 4
>>> a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a[3][1][2]
['hello']
>>> # question 5
>>> a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a[3][1][2]
['hello']
>>> a.insert(0,"Nice to have it")
>>> a.insert(7,"here")
>>> a
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'here']
# question 6
>>> numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,742, 717, 958,743, 527]
>>> for x in numbers:
    if x == 237:
        print(x)
        break;
    elif x % 2 == 0:
        print(x)

        
386
462
418
344
236
566
978
328
162
758
918
237
>>> # question 7
>>> color_list_1 = set(["White", "Black", "Red"])
>>> color_list_2 = set(["Red", "Green"])

>>> color_list_1.difference(color_list_2)
{'Black', 'White'}
>>> # question 8



>>> #question 9
>>> i=int(input("Enter a number:"))
num= (i+ ((i*10)+i) + ((i*100)+(i*10)+i))
print(num)
Enter a number:4
>>> 
>>> i=int(input("Enter a number:"))
Enter a number:4
>>> num= (i+ ((i*10)+i) + ((i*100)+(i*10)+i))
print(num)
SyntaxError: multiple statements found while compiling a single statement
>>> i=int(input("Enter a number:"))
Enter a number:4
>>> num= (i+ ((i*10)+i) + ((i*100)+(i*10)+i))
>>> print(num)
492
>>> # question 10


>>> # question 11
>>> phrase = input("Input words: ")
Input words: without,hello,bag,world
>>> phrase_list = phrase.split(",")
>>> phrase_list.sort()
>>> print((', ').join(phrase_list))
bag, hello, without, world
>>> # question 13

>>> s = input("Input a string")
Input a string hello world! 123
>>> d=l=0
>>> for c in s:
	if c.isdigit():
		d=d+1
	elif c.isalpha():
		l=l+1
	else:
		pass
>>> print("Letters", l)
Letters 10
>>> print("Digits", d)
Digits 3
