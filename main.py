import test
import datetime
x = datetime.datetime.now()
print(f"Current date time is {x}")
#baisc data types int float str boolean // cating int(),float(),str()
name, age, married, salary = "Santosh GC" , 25 , False, 0.0012354
print(f"My name is {name.upper()}")
print("My age is ",age)
print("Am i married?:",married)
print(f"My annual income is {salary:.2f}")
print("datatype of name , age , married is",type(name),type(age),type(married))
# end = input("End the program")
# toEnd = end or None
# print(end)


def check_name(name,nameList):
    if name in nameList:
        print(f"{name} is a good boy!!")
    else:
        print(f"{name} is khattam keto")
# python collections
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

#list
names = list(("areasus","pannu","kalu","dallu"))
print(f"There are {len(names)} and names are {names}")
check_name("kalu",names)
names[2] = "vodu"
check_name("kalu",names)
languages = []
languages.append("django")
languages.insert(0,"python")
print("concating languages and names")
names.extend(languages)
print(names)
names.remove("python")
names.pop(-1) #or can spicify index
print(names)
del languages[1]
print(languages)
languages.clear() # delets apll elements from list
# print(languages)
# del languages #delets whole list
# print(languages)
#loops in list
for i in range(len(names)):
    print(names[i])
[print(i) for i in names] #list comprehsion
nameList = [name for name in names if "a" in name]
print(f"There are {len(nameList)} and names are {nameList}")

#lambda function  //is an anon function and take any number of args but ahve 1 expression syntax :: lambda args: expression
sum10 = lambda a: a+10  # here sum10 is a function a is arg and a+10 is return value
print(sum10(20))
sumall = lambda a,b,c:a+b+c
print(sumall(1,2,3))
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))