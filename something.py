def getInt():
    try:
       return int(input('Enter an integer: '))
    except:
        print('<Error, not an integer>')
        return getInt()

name = input('Enter your name: ')
print("Hi, " + name + "!\n")

#some other input
a = abs(getInt()) + 50
b = abs(getInt()) + 50

#do something with other input

print('Number loading...')

i = 0
for k in range(0, a):
    for s in range(0, b * k):
       for l in range(0, s * k):
           i += l
print(i)

