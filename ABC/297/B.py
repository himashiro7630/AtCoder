S=input()
c=0
x=0
R1=0
for char in S:
    c+=1
    if char == "B":
        if x==0:
            x=c
        else:
            y=c
    elif char == "R":
        if R1==0:
            R1=c
        else:
            R2=char
    elif char=="K":
        K=c
if R1 < K and R2 > K:
    if x%2==0:
        x=0
    else:
        x=1
    if y%2==0:
        y=0
    else:
        y=1
    if x != y:
        print("Yes")
    else:
        print("No")
else:
    print("No")