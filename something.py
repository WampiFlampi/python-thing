import webbrowser as wb

def getInt():
    try:
       return int(input('Enter an integer: '))
    except:
        print('<Error, not an integer>')
        return getInt()

name = input('Enter your name: ')
print('Hi, ' + name + '!\n')

#some other input
i = (abs(getInt()) % 10) + 1

#do something with other input

try:
    for _ in range(i):
        wb.open('http://bit.ly/424bcSp', new=1)
except:
    print('Failed')

