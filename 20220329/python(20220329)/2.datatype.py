# Number
print(1)
print(1.1)
print(1+1)
print(2-1)
print(2*2)
print(6/2)
print(pow(3,2))
print(3**2)

import random
print(random.random())

# String
print('Hello')
print("Hello")
print('''
    여러줄타이핑가능
    Hello
    World
''')
print("""
    여러줄타이핑가능
    Hello
    World
""")

print(len('hello'))
print('Hell World'.replace('Hell', 'Hello'))

# List
member = ['egoing', 'duru', 'taeho']
print(member[0])
print(len(member))

import random
print(random.choice(member))

score = [100,200,300]
print(sum(score))

# from dataclasses import replace  ?? 이런건 없었음..