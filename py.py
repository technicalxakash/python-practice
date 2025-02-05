#print("This is AkashIndians")
#'''or'''

# a=b=c=10
# print(a)

# a=1,2,3,4
# print(a)

# a,b,c=10,20,30
# print(a,b,c)
# print(b)

# akash="akash123"
# print(akash)

# a=10
# print(id(a))
#140736265198296 address
# b=10
# print(id(b))
# c=11
# print(id(c))
#simple and coumpound interset
# p=int(input("enter the  principal amount:" ))
# t=int(input("enter the  time :" ))
# r=int(input("enter the  rate of interset:" ))
# n=int(input("number of times interset is coumponuded per year:" ))

# a=p*(pow((1+r/100),t))

# si=(p*t*r)/100
# print(f'the simple interest is {si}' )
# print(f'the coumpound  interest is {a}' )

#num=int(input("enter a number"))
# if num>10:
#     print("it is correct")
# elif num==10:
#     print("it is equal to number")
# else:
#     print("it is not true")

# if num>1:
#     print("this is outer if")
#     if num>0:
#         print("this is inner if")
#     else:
#         print("this is inner else")
# else:
#     print("this is outer else")
# short hand if and else
# if num>2:print("this is if")
# else:print("it is else")

# a=10
# b=20
# print("this is true")if a<b else print("this is false")

# apple=20
# while apple<40:
#     print(f"this is akash{apple}")
#     apple+=1
# else:
#     print("who are you")

# for i in "python":
#     if i=="h":
#         break
#     print(i)
# for i in "python":
#     if i=="h":
#        continue
#     print(i)
# pass
# if True:
#     pass

#tables from 1 to 1001
# for a in range(1,1001):
#     for b in range(1,11):
#         print(a*b,end=",")
#     print() 

# username autication   
# username="akash"
# password=1234
# username1=input("enter the username")
# password1=input("enter the password")
# if username==username1 and password==password1:
#     print("it is correct")
# else:



#     print("try another")

# list=[1,2,34,55,2,66,77,88]
# print(list[2])

# akash=[]
# akash=list()
# print(type(akash))

# akash=[1,2.2,'python',True]
# akash1=[1,2.2,'python',True]
# print(akash,akash1)

# car=[1,2,3,2,1,23,4,355,423,23,3554556,55,42,42535647354253653,54536,65453]
# print(car[::-1])

# james=[7]
# a=10
# b=99
# while a>b:
#     print("akash")
# else:
#     print(False)

# aa.append(1)
# print(aa)
# print(aa.count(33))
# print(aa.index(3))
# print(len(aa))
# aa.pop(2)
# print(aa)
# aa.remove(2)
# print(aa)
# aa.reverse()
# print(aa)
# aa=[ "Even" if i % 2==0 else 'odd' for i in range (10)]
# print(aa)
# lis=[]
# for i in ["apple","bat","mesh"]:
#     if "a" in i:
#         lis.append(i)
# print(lis)
# aa=[1,2,3,34,66,54,3,33,33,45,45,6,7,8,7]
# for i in range (len(aa)):
#     if aa[i]==33:
#         print(i)

# new=[]
# for i in ["a.in","b.in","c.com"]:
#       if i.endswith("in"):
#             new.append(i)
# print(new)

# a="hi {} hello!{}".format("akash","bye")
# print(a)

# names=["akash","gamesh","kamesh","rahul"]
# for a in names:
#     print("hi hello{}".format(a) )

# a="this is is my book"
# b=a.replace(" is"," are",1)
# print(b)

# d="this is my book"
# a=d.split()
# print(a)
# b=a.replace("is","are")
# print(b)

# a="this are my book"
# b=a.split()
# n=[]
# for i in b:
#     if i=="are":
#         i="is"
#         n.append(i)
#     else:
#         n.append(i)    
# print(n)

# a=[1,2,3,4,5,6,7,8,9]
# b=[2,3,4,5]
# for i in a:
#     if i not in b:
#         print([i])
# a="this is my basket"
# b=a.split()
# c=[]
# for i in b:
#     if i=="is":
#         i="are"
#         c.append(i)
#     else:
#         c.append(i)    
# print(c)
# a={"sno":1,"name":"sunny"}
# for b,c in a.items():
#     print(b,c)

# abc={
#     1:"a",
#     2:"b",
#     3:{1:"aa"}

# }
# print(abc[3][1])

# t1=(1,2,3)
# t2=(4,5,6)
# # s=zip(t1,t2)
# new=[]
# for i,j in zip(t1,t2):
#     new.append(i+j)
# print(tuple(new))

# name="akash"
# password="123"
# username1=input("enter the username1=")
# password1=input("enter the password1=")
# s="""
# 1.credit
# 2.debit
# 3.mini statement
# 4.exit
# """
# amount=1000
# if name==username1 and password==password1:
#         while True:
#             print("successfully login")
#             print(s)
#             option=int(input("enter the option:"))
#             if option==1:
#                 credit_amt=float(input("enter the amount"))
#                 print(amount+credit_amt)
#             elif option==2:
#                 debit_amt=float(input("enter the amount"))
#                 print(amount-debit_amt)
#             elif option==3:
#                 print(amount)
#             elif option==4:
#                 break

#             else:
#                print("try again")

# from datetime import datetime
# name=input("Enter the name ")
# lists="""
# Rice  Rs 20/kg
# wheat Rs 15/kg
# water Rs 20/liter
# sugar Rs 45/kg
# oil   Rs 100/kg
# maggi Rs 50/kg
# Boost Rs 90/each
# """

# items={'rice':20,'wheat':15,'water':20,'sugar':45,'oil':100,"maggi":50,'Boost':90}

# option=int(input("for list of items press 1 "))
# if option==1:
#     print(lists)
# for i in range(len(items)):
# a=100
# b=200

# a=a+b
# b=a-b
# a=a-b
# print(a)
# print(b)

# boy=input("enter the boy name : ")
# girl=input("enter the girl name : ")
# boy_age=int(input("enter boy age : "))
# girl_age=int(input("enter boy age : "))
# age_difference=abs(boy_age - girl_age)
# print(f"{boy} loves {girl} age_difference{age_difference}")

# fname="akash"
# lname="r"
# name=fname + " " +lname
# print(name)

# error="warning! " * 3
# print(error)

# e="Warning!"
# print(e.upper())
# print(e.lower())
# print(e.strip())
# print(e.replace("Warning!  ","a"))
# print(len(e))

# a="akash indians"
# print(a[::-1])

# a=10
# a*=100
# print(a)

# a=10
# b=100

# print(a==b)
# print(a!=b)
# print(a<b)
# print(a>b)

# a=10
# b=20
# print(a<b and b>a)
# print(a<b or b==a)
# print(not(False))

# a="akash"#membership operator 
# print(a not in a)
# print(a  in a)

# def add(a,b):
#     while(b!=0):
#         c= a & b
#         a=a^b
#         b=c<<1
#     return a
# print(add(5,1))
#adding two number without using plus operator
# a=int(input("enter the value of a : "))
# b=int(input("enter the value of b : "))
# while(b!=0):
#         c= a & b
#         a=a^b
#         b=c<<1
# print(a)

# class Moblies:
#     def __init__(self,Mname,Mram,Mprice,Mstorage):
#         self.a=Mname
#         self.b=Mram
#         self.c=Mprice
#         self.d=Mstorage
#     def data(self):
#         print("mobile name : ",self.a)
# Mobj=Moblies("apple","8gb",8000,"32gb")
# Mobj.data()

# import calendar
# year = 2024
# print(calendar.prcal(year))

# import calendar
# year = 2024
# month = 5
# print(calendar.prmonth(year, month))

# class Moblies:
#     def __init__(self,Mname,Mram,Mprice,Mstorage):
#         self.a=Mname
#         self.b=Mram
#         self.c=Mprice
#         self.d=Mstorage
#     def data(self):
#         print("mobile name : ",self.a)
# while True:
#     name=input("enter the mobile name : " )
#     ram=input("enter the ram : ")
#     price=input("enter the price : ")
#     storage=input("enter the storage : ")
#     Mobj=Moblies(name,ram,price,storage)
#     Mobj.data()

# class bike:
#     def __init__(self,BName,Bfeatures,Bmillege,Brdtax,Bprice):

#         self.f=BName
#         self.b=Bfeatures
#         self.c=Bmillege
#         self.d=Brdtax
#         self.e=Bprice
#     def data(self):
#         print("Bikename : ",self.f)
# Objbike=bike("jawa","power","excellent",40,45000)
# Objbike.data()


# items = ["a","b","c","d","e","f"]
# print(items)
# items.pop()
# print(items)
# items.pop(0)
# print(items)
# items.append("g")
# print(items)
# items.remove("a")
# print(items)
# items.insert(0,'a')
# print(items)
# items[0]="b"
# print(items)
# print(len(items))

# a="To ,fix ,this ,and, display".split(",")
# print(a)
# a.insert(0,"aa")
# print(a)
# print(a[::-1])
# a.reverse()
# print(a)


# aa=("a","b","c","d","a")
# print(aa.count("a"))
# print(aa)
# print(len(aa))
# print(aa[0])

# bb={"a","b","a"}
# print(bb)
# a={1,2,3,4}
# b={3,4,5,6}
# print(a | b)
# print(a & b)
# print(a-b)
# s={1,2,3,4,5,5}
# s.add(6)
# s.remove(5)
# print(s)
# s.pop()
# print(s)
# print(s[0])

# a=60
# b=85
# print(a*b)
# -*- coding: utf-8 -*-

# birthday={

#     "A":"1-1-1"
# }
# print(birthday)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict.get("a","not having"))
# thisdict["a"]="akash"
# print(thisdict)
# thisdict["year"]=1965
# print(thisdict)
# thisdict.pop("brand")
# print(thisdict)

# a=int(input("enter the number : "))
# if(a%2==0):
#     print(f"{a} is a even number")
# else:
#     print(f"{a} is not a even number")

# string=input("enter the string : ")
# aa=""
# for i in string:
#     aa=i+aa
# print(aa)

# s = "GeeksforGeeks"

# # Initialize an empty string to hold reversed result
# rev = ""

# # Loop through each character in original string
# for i in s:
  
#     # Add current character to front of reversed string
#     rev = i + rev

# print(rev)


# def function(number):
#     if number>1:
#         for i in range(2,number):
#             if number%i==0:
#                 return "not a prime"
#         return "it is prime number"


# print(function(number=int(input("number"))))
  
# number=int(input("number : "))
# if number%2==0:
#     print("it is a even number")
# else:
#     print("is is odd")

# i=1
# while i<5:
#     print(i)
#     i=i+1
# print(i)

# is_faild=True
# i=1
# while is_faild and i<=100:
#     print(f"is try {i}")
#     i=i+1
# print("i gave up")


# is_faild=True
# i=1
# while is_faild :
    
    
#     if i%2!=0:
#         i=i+1
#         continue
#     if i>100:
#         break
# print("i gave up")

# is_faild=True
# i=1
# while is_faild :
#     if i%2!=0:
#         i=i+1
#         continue
#     print(i)
#     i=i+1
#     if i>100:
#         break

# print("i gave up")


# i=1
# while True:
    
#     if i%2!=0:
#        i=i+1
#        continue
#     print(i)
#     i=i+1
#     if i>100:
#         break
# print("ill")

# a=1
# while True:
#     if a%2!=0:
#         a=a+1
#         continue
#     print(a)
#     a=a+1   
#     if a>100:
#         break

# for i in range(1,10):
#     if i==8:
#         break
#     print(i)


# a=['b',"c","d"]
# for z in a:
#     print(z)

# name="akash"
# for z in enumerate(name):
#     print(z)

# x=3
# y=4
# sum=0
# for i in range(0,y):
#     sum=sum+x
#     print(sum)

# for i in range(2,110):
#     for j in range(1,11):

#       print(f"{i}X{j}={i*j}")

# l=[1,2,3,4,5,6]
# total=0
# for i in l:
#     total=total+i
# print(total)

# list=[1,2,3,4,5,6,7]
# n_list=[]
# for i in list:
#     n_list.append(i*2)
#     print(n_list)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for i in thisdict.items():
#     print(i)

# student_marks={"akash":90,"hitish":98,"indains":97}
# for student,marks in student_marks.items():
#     print(f"{student}___{marks}")

# this_dict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict={}
# for chara,details in enumerate(thisdict):
#     print(thisdict[chara]---thisdict[details])

# student=["akash","hitish","indains","raj"]
# marks=[90,99,89,87]
# student_marks={}
# for i in range(len(student)):
#     student_marks[student[i]]=marks[i]
# print(student_marks)

# l=[ items for items in range(1,11)]
# dl = [items**2 for items in l if items%2==0]
# print(dl)

# this_dict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# d={ i:len(i) for i in this_dict}
# print(d)

# city_population={

#     "banglore":100,
#     "mysore": 96,
#     "hassan":80,
#     "hubbali":90,
#     "bidar":50
# }

# dl={ city:pop for city,pop in city_population.items() if pop>50}
# print(dl)

# a="akash is a indian"
# s=a.split()
# print(s)

#a=input("enter the number : ").split()
# b=[b for b in input("enter the number : ").split()]
# print(b)
# i=0
# while i<=10:
#     print(i , end="  ")
#     i+=1

# for i in range(2,11):
#     for j in range(1,11):
#         print(f"{i}X{j}={i*j}")

# a=10
# b=20
#b,a=a,b
# a=a+b
# b=a-b
# a=a-b
# a=a^b
# b=a^b
# a=a^b
# print(a)
# print(b)

# s=input("sentence : ")
# print(s.upper())
# print(s.lower())
# print(s.replace(" ","_"))

# a=int(input())
# b=int(input())


# if (a>10 and b>10):
#     print("a and b is lower")
# else:
#     print("a and b is greater")

# print(a<5 or b<5)
# print(not(a>5))

# l=[1,2,3,4,5]
# l.insert(3,4)
# print(l)

# t1=(1,2,3,4,5)
#print(t[1:3])
# t2=(4,5,6,7,8)
# print(t1+t2)

#city_population={

#     "banglore":100,
#     "mysore": 96,
#     "hassan":80,
#     "hubbali":90,
#     "bidar":50
# }

# city_population["durga"]=85
# city_population["bidar"]=75
# print(city_population)
# del city_population["bidar"]
# print(city_population)

# seats=8
# while seats>0:
#     print("book one seat")
#     seats=seats-1
#     print(f"Reaming seats are , {seats}")
# print("all seats are booked")
# import time
# count=10
# while count>0:
#    print(count)
#    time.sleep(1)
#    count=count-1
# print("happy new year")
# total=0
# for i in range(1,11):
#      total=total+i
# print(total)
# count=10
# while count:
#     print(count)
#     count=count-1
# print("ha")

# n=(10*11)/2
# print(n)
# sum=0
# for i in range(11,20):
#       sum=sum+i
# print(sum)

# volwes="aeiou"

# stringg="my name is akash"
# count=0
# for string in volwes:
#     count=count+1
# print(count)

# d={
# "idli":1,
# "dosa":2,
# "palav":3,
# "bhat":4,
# "masala dosa":4
# }
# total=0
# for key,value in d.items():
#     total=total+value
# print(total)
# d.values()
# print(sum(list(d.values())))
# l=[ num**2 for num in range(1,11)]
# print(l)

# rows=int(input("enter the number of rows : "))

# matrix=[]
# for i in range(rows):
#     x=[int(num) for num in input(f"enter the row {i+1}").split()]
#     matrix.append(x)
# print(matrix)

# def sum(a,b):
#     print(a+b)
# sum(5,3)
# def great():
#     print("hellolmcfnvinfvinivnsvn")
# great()
# def marriage(boy , girl):#parameters
#     print(f"{ boy}married {girl}")
# marriage("akash ","akas")#positional arguments

# def tables(num):
#     for i in range(1,11):
#       print(f"{num}X{i}={i*num}")
# tables(5)

"""
There are five types of arguments in Python:
Positional arguments
These are the traditional arguments that are passed to a function in a specific order, based on their position in the function definition. 
Keyword arguments
These arguments are key-value pairs that allow the caller to declare the argument name together with values. 
Default arguments
These arguments help to deal with the absence of values. 
Arbitrary positional arguments
These arguments are used when a function can accept a variable number of positional arguments. 
Arbitrary keyword arguments
These arguments are used when a function can accept a variable number of keyword arguments. 
"""


# def sum(*a):
#     print(a)
# sum(1,2,3,4,5,6)

# def add(*numbers):
#     return sum(numbers)
# print(add(1,2,3,4,5,6))

# def students(**details):
#     print(type(details))
#     for key,value in details.items():
#         print(f"{key}:{value}")
# students(name="akash",age=21,course="cs")

# add = lambda a,b : a+b
# print(add(1,2))

# mul = lambda a,b : a*b
# print(mul(2,3))

# d = [{7058: 'sravan',
#  7059: 'jyothika', 
#  7072: 'harsha',
#   7075: 'deepika'}] 

# ]

# def greet():
#     print("Hello")
#     greet()
# greet()

# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(4))



# for i in range(0,4):
#     print(i*i)
# n=int(input())
# i=0
# while i<=n:
#     print(i*i)
#     i=i+1
# def is_leap(year):
#     leap = False
#     if year % 4!=0:
#         return false
#         break
#     else:
#         if year % 100 !=0:
#             return false
#         if year % 400==0:
#             return true
#         else:
#             return false
#     # Write your logic here
    
#     return leap

# year = int(input())

# def is_leap(year):
#     leap = False
#     if (year % 4==0)and (year % 100 != 0 or year % 400 == 0 ):
#         return True
#     else:
#         return False
#     # Write your logic here
    
#     return leap

# year = int(input())
# print(is_leap(year))
# if __name__ == '__main__':
#     n = int(input())
#     for i in range(1,n+1):
#         print(i,end='')

# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     result=[]
#     for i in range(x+1):
#         for j in range(y+1):
#             for k in range(z+1):                
#                 result.append([i,j,k])
#     print(result)

# if __name__ == '__main__':
#     n = int(input())
#     l = map(int, input().split())
    
#     s=set(l)
#     ll=list(s)
#     ll.sort()
#     g=ll[-s]
#     print(g)

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     avg_marks=(sum(student_marks[query_name])/3)
#     print("{:.2f}".format(avg_marks))

# import string
 
# # initializing string
# test_str = "abbabba"
 
# # printing original string
# print("The original string is : " + str(test_str))
 
# # Using translate() + maketrans()
# # Replace multiple characters at once
# res = test_str.translate(string.maketrans("ab", "ba"))
 
# # printing result
# print("The string after replacement of positions : " + res)



# # define the input string
# str1 = "abbabba"
# # printing original string
# print("The original string is : " + str(str1))

# # use a list comprehension to iterate through the string and replace each character
# # if the character is 'a', replace it with 'b'
# # if the character is 'b', replace it with 'a'
# # if the character is anything else, leave it unchanged
# new_str = ''.join(['a' if char == 'b' else 'b' if char == 'a' else char for char in str1])

# # print the new string
# print("The string after replacement of positions : " +new_str)
# #This code is contributed by Jyothi pinjala.
# new_str = ''
# str1="apples"
# for char in str1:
#     if char == 'p':
#         new_str += 'a'
#     elif char == 'a':
#         new_str += 'p'
#     else:
#         new_str += char
# print(new_str)

# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Example

# The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

# alpha
# beta
# Input Format

# The first line contains an integer, , the number of students.
# The  subsequent lines describe each student over  lines.
# - The first line contains a student's name.
# - The second line contains their grade.

# Constraints

# There will always be one or more students having the second lowest grade.
# Output Format

# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

# Sample Input 0

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0

# Berry
# Harry
# Explanation 0

# There are  students in this class whose names and grades are assembled to build the following list:

# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
#solution 
# if __name__ == '__main__':
#     records=[]
#     s=set()
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
       
#         records.append([name,score])
#         s.add(score)
#     sls=sorted(s)[1]
#     sln=[]
#     for name,score in records:
#         if score==sls:
#             sln.append(name)
#     for name in sorted(sln):
#         print(name)
            
# number=float(input("enter the number : "))
# if number>0:
#     print(f"{number} is negative")
# elif number<0:
#     print(f"{number} is positive")
# else:
#     print(f"{number} is equal to 0")

# inp=list("varnu")
# inp[3],inp[4]=inp[4],inp[3]
# new="".join(inp)
# print(new)

# num=int(input("enter the number : "))
# if num%2==0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")

# year=int(input("enter the year : "))
# if year%4==0:
#     if year%100==0:
#        if year%400==0:
#         print(f"{year} is a leap year")
#        else:
#         print(f"{year} is not a leap year")
#     else:
#        print(f"{year} is not a leap year")
# else:
#     print(f"{year} is not a leap year")


# year=int(input("enter the year : "))
# if year%4==0 and year%100!=0 or year%400==0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# for i in range(1,101,2):
#     print(i)



# num = input("Enter the number: ")

# try:
#     num = int(num)  # Convert input to an integer
#     if num <= 1:
#         print(f"{num} is not a prime number")
#     else:
#         is_prime = True  # Assume the number is prime initially
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break  # Exit the loop as we found a divisor
#         if is_prime:
#             print(f"{num} is a prime number")
#         else:
#             print(f"{num} is not a prime number")
# except ValueError:
#      print("Invalid input! Please enter a valid integer.")

# num=int(input("enter the number : "))

# if num <= 1:
#     print(f"{num} is not a prime number")
# else:
#    for i in range(2, int(num**0.5) + 1):
#      if num % i == 0:
#             print(f"{num} is a prime number")
#      else:  
#         print(f"{num} is a prime number")      

# data = 50
# try:
#     data = data/0
# except ZeroDivisionError:
#     print('Cannot divide by 0 ', end = '')
# else:
#     print('Division successful ', end = '')

# try:
#     data = data/5
# except:
#     print('Inside except block ', end = '')
# else:
#     print('GFG', end = '')


# data = 50
# try:
#     data = data/10
# except ZeroDivisionError:
#     print('Cannot divide by 0 ', end = '')
# finally:
#     print('GeeksforGeeks ', end = '')
# else:
#     print('Division successful ', end = '')

# value = [1, 2, 3, 4]
# data = 0
# try:
#     data = value[3]
# except IndexError:
#     print('GFG IndexError  ', end = '')
# except:
#     print('GeeksforGeeks IndexError  ', end = '')
# finally:
#     print('Geeks IndexError  ', end = '')

# data = 10
# try:
#     data = data/0
# except ZeroDivisionError:
#     print('GFG ZeroDivisionError  ', end = '')
# finally:
#     print('Geeks ZeroDivisionError  ')
# n=int(input())

# def fact_number(n):
#     return n*fact_number(n-1)
# print(fact_number(n))

# num = int(input("Enter the number: "))
# def fact_number(num):
#     if num==0:
#         return 1
#     else:
#         return num*fact_number(num-1)
# print(fact_number(num))

# new_str = ''
# str1="apples"
# for char in str1:
#     if char == 'p':
#         new_str += 'a'
#     elif char == 'a':
#         new_str += 'p'
#     else:
#         new_str += char
# print(new_str)

#fib
# a=0
# b=1
# for c in range (0,10):
#     c=a+b
#     a=b
#     b=c
#     print(c)
# def fib(n):
#     if n==0:
#         return 0
#     elif n==1 or n==2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# n=int(input("Enter the number : "))
# for n in range(n):
#     print(fib(n))

# str=input("enter the str : ")
# st=str[::-1]
# if str==st:
#     print(f"{str} is a palindrome")
# else:
#     print(f" {str} it is not palindrome")


# l=1,2,3,4,5
# print(l[0]+l[1])

# l1=[1,2,3,4]
# l2=[1,2,3,4]
# l3=[]
# for i in range(0,4):
#     l3.append(l1[i]+l2[i])
# print(l3)

# my_list = [i for i in range(1, 10)]

# class Solution(object):
#   def twoSum(self, nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     return []

    # Simple Python program to find sum of series
# with cubes of first n natural numbers

# Returns the sum of series 
# def sumOfSeries(n):
#     sum = 0
#     for i in range(1, n + 1):
#         sum += i * i*i
        
#     return sum


# # Driver Function
# n = 5
# print(sumOfSeries(n))

# Code Contributed by Mohit Gupta_OMG <(0_o)>


#Merge Two Sorted Lists
# def merge_sorted_lists(list1, list2):
#     i = j = 0
#     merged = []
#     while i < len(list1) and j < len(list2):
#         if list1[i] < list2[j]:
#             merged.append(list1[i])
#             i += 1
#         else:
#             merged.append(list2[j])
#             j += 1
#     merged.extend(list1[i:])
#     merged.extend(list2[j:])
#     return merged


# def are_anagrams(str1, str2):
#     return sorted(str1) == sorted(str2)


#Check if Two Strings are Anagrams
# # Example usage:
# print(are_anagrams("listen", "silent"))  # Output: True
# print(are_anagrams("hello", "world"))    # Output: False



#Find the Second Largest Number in a List
# def second_largest(nums):
#     unique_nums = list(set(nums))  # Remove duplicates
#     unique_nums.sort()
#     return unique_nums[-2]

# # Example usage:
# print(second_largest([1, 2, 3, 4, 4]))  # Output: 3


# num1=input("enter the numbers : ")
# num2=input("enter the numbers : ")
# num3=input("enter the numbers : ")

# if num1>num2 and num1>num3:
#     print(num1)
# elif num2>num1 and num2>num3:
#     print(num2)
# else:
#     print(num3)
# print("above is greater numbers")


# l=input().split(",")
# print(max(l))

# def get_permutation(string,i=0):
#     if i==len(string):
#         print("".join(string))
#     for j in range(i,len(string)):
#         words=[c for c in string]
#         words[i],words[j]=words[j],words[i]
#         get_permutation(words,i+1)
# get_permutation('run')


# from itertools import permutations 
 
 
# # Get all permutations of [1, 2, 3] 
# perm = permutations([1, 2, 3]) 
 
# # Print the obtained permutations 
# for i in perm: 
#     print (i) 

# from itertools import permutations

# perm=permutations([1,2,3],2)

# for i in perm:
#     print(i)



# from itertools import combinations
# combi=combinations([1,2,3],2)

# for i in combi:
#     print(i)

# from itertools import permutations

# perm=permutations(["r","u","n"])

# for i in list(perm):
#     print(i)


# from itertools import permutations
# string='abc'
# perm=list(permutations(string))
# perm=[ ''.join(permutations) for permutations in perm]
# print(perm)

# for i in range(1,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#             print(i)

# if __name__ == '__main__':
#     N = int(input())
#     list=[]
#     for i in range(N):
#         comma=input().split()
#         cmd=comma[0]
#         if cmd=="insert":
#             i, e = int(comma[1]), int(comma[2])
#             list.insert(i, e)
#         elif cmd == "print":
#             print(list)
#         elif cmd == "remove":
#             e = int(comma[1])
#             list.remove(e)
#         elif cmd == "append":
#             e = int(comma[1])
#             list.append(e)
#         elif cmd == "sort":
#             list.sort()
#         elif cmd == "pop":
#             list.pop()
#         elif cmd == "reverse":
#             list.reverse()

# number=int(input("enter the number"))
# if number>1:
#    for i in range(2,number):
    
#         if number%i==0:
#             print(f"{i} not prime")
#         else:
#             print("prime")

# for i in range(1,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

# Armstrong numbers
# number=input("enter the number : ")
# sum=0
# for i in number:
#     sum+=int(i)**3
# if sum==int(number):
#     print(f"{number} is armstrong number")
# else:
#     print(f"{number} is  not armstrong number")


#oops
# class human:                         #class
#     def __init__(self,name):          
#         self.name=name         #attribute


#     def walk(self):              #method
#         print(f"{self.name} is walking")


# alice=human("alice")                 #object

# alice.walk()


# class mobile:
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price

#     def cost(self):
#         print(f"{self.brand} is the mobile brand")
#         print(f"{self.price} is the mobile price")

# sumsung=mobile("sumsung","1000")

# sumsung.cost()

#sorting same elements in an array        
# arr1=[1,2,3,4]
# arr2=[1,6,3,5]
# arr3=[]
# for i in arr1:
#     for j in arr2:
#         if i==j:
#             arr3.append(i)
# print(arr3)

#sorting same elements in an array without using append
# arr1=[1,2,3,4]
# arr2=[1,6,3,5]
# arr3=list(set(arr1).intersection(set(arr2)))
# print(arr3)

# arr1=[1,2,3,4]
# arr2=[1,6,3,5]
# arr3=list(set(arr1).union(set((arr2))))
# print(arr3)


# arr1=[1,2,3,4]
# arr2=[1,6,3,5]
# arr3=[i for i in arr1 if i in arr2]
# print(arr3)


#oops
# class human:                         #class
#     def __init__(self,name,age=-1):  #optional parameter age value there is nothing it will take -1        
#         self.name=name   
#         self.age=age      #attribute


#     def walk(self):              #method
#         print(f"{self.name} is walking his age is {self.age}")


# a=human("alice",22)  
# b=human("akash")               #object

# human.walk(a)
# human.walk(b)

#opps=it is programming style and not a specific lanaguage built on the concept of object , it uses object to represnt data and methods

#1)abstarction=used to hide the complex internal operations of object , exposes only the essential parts for interaction

# l=[1,2,3,4]
# l.append(5) # it is abstraction hiddening of information
# print(l)

#2)encapsulation=wrapping of data and methods in a single unit

# class Database:
#     def __init__(self):
#         # self.storage={} #public attribute
#         # self._storage ={}#protected
#         #self.__storage ={}#private

#     def write(self,key,value):
#         self.storage[key]=value

#     def read(self,key):
#         if key in self.storage:
#             print(self.storage[key])
#         else:
#             print("db item not available")

# db=Database()
# db.write("sub","100k")
# db.write("subbbbb","200k")

# db.read("sub")
# print(db.storage)  #not private here printing all 



#private
# class Database:
#     def __init__(self):

#         self.__storage ={}#private

#     def write(self,key,value):
#         self.__storage[key]=value

#     def read(self,key):
#         if key in self.__storage:
#             print(self.__storage[key])
#         else:
#             print("db item not available")

# db=Database()
# db.write("sub","100k")
# db.write("subbbbb","200k")

# db.read("sub")
 #it will not give full storage

 




