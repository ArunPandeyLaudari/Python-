a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
c=int(input('Enter the value of c'))

if a>b:
    if a>c:
        print(f'{a} is larger element')
    else:
        print(f'{c} is larger element')
elif b>c:
    print(f'{b} is larger element')
else:
    print(f'{c} is larger element')