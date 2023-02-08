def make_pair(x,y):
    return lambda n: x if n==0 else y
def first(p):
    return p(0)
def second(p):
    return p(1)

# 12    - 15
# 15    - 18
# 18    - 19
# 19.5  - 23
# 22    - 24

# ввод данных
p1 = make_pair(12,1)
p2 = make_pair(15,1)
p3 = make_pair(18,1)
p4 = make_pair(19.5,1)
p5 = make_pair(22,1)

u1 = make_pair(15,-1)
u2 = make_pair(18,-1)
u3 = make_pair(19,-1)
u4 = make_pair(22,-1)
u5 = make_pair(23,-1)

counter = 1
# first(p) #5
# second(p) #6
# p1 = make_pair('hello',6)
# first(p1) #'hello'
# 1

if counter == 1:
# 1
    if first(u1)>=first(p2) and counter == 1:
        print('охраняется')
        counter = second(p1) + second(u1) + second(p2)
    else:
        print('не охраняется')
        counter = second(p1) + second(u1) + second(p2) + second(u2)
    print(' ',counter)

# 2
    if first(u2)>=first(p3) and counter == 1:
        print('охраняется')
        counter = second(p2) + second(u2) + second(p3)
    else:
        print('не охраняется')
        counter = second(p2) + second(u2) + second(p3) + second(u3)
    print(' ',counter)

# 3
    if first(u3)>=first(p4) and counter == 1:
        print('охраняется')
        counter = second(p3) + second(u3) + second(p4)
    else:
        print('не охраняется')
        counter = second(p3) + second(u3) + second(p4) + second(u4)
    print(' ',counter)

# 4
    if first(u4)>=first(p5) and counter == 1:
        print('охраняется')
        counter = second(p4) + second(u4) + second(p5)
    else:
        print('не охраняется')
        counter = second(p4) + second(u4) + second(p5) + second(u5)
    print(' ',counter)
    print(' ')

    print('итого',counter)
else:
    print('сегодня охранники запутались')

# ответ
# # print(counter)
# if counter == 0:
#     print('сегодня охранники запутались')
# else:
#     print('сегодня охранники молодцы')