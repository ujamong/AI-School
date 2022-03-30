#1차원 배열
members = ['egoing', 'duru']
# for XXX in XXX:
#     code
for member in members:
    print('member', member)

#2차원배열
members2 = [
    ['egoing', 'seoul', 'programmer'],
    ['duru', 'daegu', 'dba']

]

# 배열의 첫번째 리스트의 첫번째 원소
print(members2[0][0])

for member in members2:
    print(member[0], member[1])

egoing = ['egoing', 'seoul', 'progrmmer']

#딕셔너리로 바꾸기
#egoing1 = ['egoing', 'seoul', 'programmer']
egoing2 = {'name' : 'egoing', 'city' : 'seoul', 'job' : 'programmer'} #사전형
print(egoing2['city'])
for name in egoing2:
    # print(name)
    print(egoing2[name])

members3 = [
    {'name':'egoing', 'city':'seoul', 'job':'programmer'},
    {'name':'duru', 'city':'daegu', 'job':'dba'}
]
for member in members3:
    #print(member)

    #이름만 가지고 오고 싶다
    print(member['name'])