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

