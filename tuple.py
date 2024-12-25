x = [10,20,30,40,50,60]
y = []
for i in range (6):
    if 1 % 2 ==1:
        y.append(x[i])
print(y)
x = [10,20,30,40,50]
y = []
for i in range(5):
    if x[i] % 4==0:
        y.append(x[i])
print(y)
x = [10,20,30,40,50]
y =[]
for i in x:
    x= i+5
    y.append(i+5)
print(y)
x = [1,2,3,4,5,6]
y = []
for i in x:
    x = i**3
    y.append(i**3)
print(y)
x = [23,13,40,55,17]
for i in x:
    x = i-3
    y.append(i-3)
print(y)
x = [11,2,31,47,15,6]
y = []
for i in range(len(x)):
    if i%2==1:
        y.append(x[i])
print(y)
x = [11,2,31,47,15,6]
y = []
for i in range(len(x)):
    if i%2==0:
        y.append(x[i])
print(y)
x = ['hi','python','we','write','python','we','say','hi','python']
y = {}
for i in x:
    if i in y.keys():
        y[i] = y[i]+1
    else:
        y [i] = 1
print(y)
x = [('a',10),('b',20),('c',30),('d',40)]
y = ()
for i,j in x:
    print(j)
x = ['a','b','c','d']
y = [10,20,30,40]
di ={}
for i in range(len(x)):
    di [x[i]]= y[i]
print(di)
x = ['a','b','c','d']
y = [10,20,30,40]
z = [(x[i],y[i])for i in range(len(x))]
print(z)
x = [('hi','noun'),('good','adj'),('run','verb'),('bad','adj'),('good','adj')]
pos = 0
negative = 0
neutral = 0
for i,j in x:
    if i == 'good':
        pos +=1
    elif i == 'bad':
        negative +=1
    else:
        neutral+=1
if pos>=negative and pos>=neutral:
    print("sentiment is positive")
elif negative>neutral:
    print("sentiment is negative")
else:
    print("sentiment is neutral")
x = 10
y = 20
def function_one():
    x=100
    print(x+y)
def function_two():
    y=50
    print(x+y)
function_one()
function_two()
print(x+y)
x = 10
def f1():
    x = 20
    print(x)
    print(globals() ['x'])
f1()
x = 10
y = 20
def f1():
    y=30
    print(x)
    print(y)
    print(globals()['x'])
    print(globals()['y'])
f1()
tu = ()
tu = input("enter the name:")
for i in range(5):
