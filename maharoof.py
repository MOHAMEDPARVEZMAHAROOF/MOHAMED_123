a = int(input("ENTER YOUR LUCKY NUMBER :" ))
b = int(input("ENTER YOUR LUCKY NUMBER :"))
c = int(input("ENTER YOUR LUCKY NUMBER :" ))
d = int(input("ENTER YOUR LUCKY NUMBER :"))
e = int(input("ENTER YOUR LUCKY NUMBER :" ))
f = int(input("ENTER YOUR LUCKY NUMBER :"))
g = int(input("ENTER YOUR LUCKY NUMBER :" ))
h = int(input("ENTER YOUR LUCKY NUMBER :"))
cout = 0
for lottery in range(1, 100):
    if (lottery == a ):
        cout = cout + 1
    elif(lottery == b):
        cout = cout + 1
    elif(lottery == c):
        cout = cout + 1
    elif(lottery == d):
        cout = cout + 1
    elif(lottery == e):
        cout = cout + 1
    elif(lottery == f):
        cout = cout + 1
    elif(lottery == h):
        cout = cout + 1
    if(cout == 61):
        print("YOU WIN")
    else:
        cout = 0
        print("YOU LOSE")