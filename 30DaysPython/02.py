'''help('Keyword')
help(str)
#dir(str)

#Variables in python
first_name='Lokesh'
last_name='Singh'
country='India'
age=250
is_married=False
skills=['Python','C']
p_info={
    'f_name':'Lokesh',
    'l_name':'Singh',
    'country':'India',
    'city':'BLR',
    age:250
}

print('First name:', first_name)
'''
#Exercise:1
#1:Done
#2
#Day1.2:30 Days of python programming.
#1.3
f_name='Lokesh'
#1.4
l_name='Singh'
#1.5

#1.6
country='India'
#1.7
city='Blr'
#1.8
age=25
#1.9
year=2023
#1.10
is_married=False
#1.11
is_true=True
#1.12
is_light=False
#1.13
name,f_name,l_name,full_name="Lokesh Singh",'Lokesh','Singh','Lokesh Singh'

#Exercise 2
#2.1
print(type(f_name))
#2.2
print(len(f_name))
#2.3
a=len(f_name)
b=len(l_name)
print(a>b)
print(b>a)

#2.4.1
num_one=5
num_two=4
sum=num_one+num_two
print(sum)
#2.4.2
diff=num_one-num_two
#2.4.3
product=num_one*num_two
print(product)
#2.4.4
division=num_one/num_two
print(division)
#2.4.5
remainder=num_one%num_two
print(remainder)
#2.4.6
exp=num_one**num_two
print(exp)
#2.4.7
f_div=num_one//num_two
print(f_div)

#2.5.1
r=30
area_of_circle=3.14*r*r
print(area_of_circle)
#2.5.2
circum_of_circle=2*3.14*r
print(circum_of_circle)
#2.5.3
r=int(input("Enter the radius:"))
print(type(r))

area=3.14*r*r
print(area)
#2.6
f_name=input('Enter first name')
print('Hi',f_name)
l_name=input('Enter Last Name')
print('Hello Mr',l_name)
country=input('Which coutry do you live in')
print('I live in ',country)
age=input('How old are you')
print(f"I'm {age} years old")
#2.7
help('keywords')
