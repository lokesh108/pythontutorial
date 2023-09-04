# print('I hope everyone is enjoying the python challenge.\nAre You?')
# print('Days\tTopics\tExercises')
# print('Day 1\t5\t5')
# print('Day 2\t6\t20')
# print('Day 3\t5\t23')
# print('Day 4\t1\t35')
# print('This is a backslash symbol "\\"')
# print('In every programming language it starts with \"Hello , World!\"')

# greeeting='Hello World!'
# print(greeeting[::-1])

# f_Name='lokesh'
# print(f_Name.capitalize())
# print(f_Name.lower())
# print(f_Name.upper())
# print(f_Name.title())
# print(f_Name.count('l'))

# #Exercise-D4
# #4.1
# a='Thirty'
# b=' Days'
# c=' Of'
# d=' Python'
# print(a+b+c+d)

# #4.2
a='Coding'
b=' For'
c=' All'
# print(a+b+c)

# #4.3
company=a+b+c

# #4.4
print(company)

# #4.5
# print(len(company))

# #4.6
# print(company.upper())

# #4.7
# print(company.lower())

# #4.8
# print(company.capitalize())
# print(company.title())
# print(company.swapcase())

# #4.9
# print(company.strip('Coding'))

# #4.10
# print(company.index('Coding'))

# #4.11
# print(company.replace('Coding','Python'))
# new=company.replace('Coding','Python')

# #4.12
# print(new.replace('All','Everyone'))

# #4.13
print(company.split(' '))

# #4.14
new_comp="Facebook, Google,Microsoft,Apple,IBM,Oracle,Amazon"
print(new_comp.split(','))

# #4.15
print(company[0])

# #4.16
print(company[-1])

# #4.17
print(company[10])

# #4.18
PFE='PythonForEveryone'
print(PFE[0],PFE[6],PFE[9])

#4.19
print(company[0],company[7],company[11])

# #4.20
print(company.find('C'))

# #4.21
print(company.find('F'))
# #4.22
company_find='Coding For All People'
print(company.rfind('l'))

# #4.23
str_new='You cannot end a sentance with because because becuase is a conjuction'
print(str_new.find('because'))

# #4.24
print(str_new.rfind('because'))

# #4.25***
str_new=str_new.strip('because')
print(str_new)
# #4.26
# #Same as 23

# #4.27***
#4.28
new_str='Coding for All'
print('Coding' in new_str)
#4.29
print(new_str.endswith('coding'))
#4.30***
new_str='1   Coding For All      2'
print(new_str.strip())
#4.31
l1='30DaysOfPython'
l2='thirty_days_of_python'
print(l1.isidentifier())
print(l2.isidentifier())
#4.32
names=['Django','Flask','Bottle','Pyramid','Falcon']
print(' #'.join(names))
#4.33
print('I am enjoying this challenge. \nI just wonder what is next')
#4.34
print('Name\t\tAge\tCountry\t\tCity\nAsabeneh\t250\tFinland\t\tHelsinki')
#4.35
radius=10
area=3.14*radius**2
print(f'The area of a circle with radius {radius} is {area} meter square.')
#4.36
print('8 + 6 = 14\n8 - 6 = 2\n8 * 6 = 48\n8 / 6 = 1.33\n8 % 6 = 2\n8 // 6 = 1\n8 ** 6 = 262144')
