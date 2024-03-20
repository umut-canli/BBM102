import sys
x = int(sys.argv[1])
n = int(sys.argv[2])
def calculator(x,n):
    number=x**n
    result = str(x) + '^' + str(n) + ' = ' + str(number)
    while number > 9:
        a=0
        List = [int(digit) for digit in str(number)]
        for i in List:
            a += i
        result += ' = ' + '+'.join(str(number)) + ' = ' + str(a)
        number = a
    print("Output:",result)

calculator(x,n)

