I=input().split()#入力受け取る
fc=int(I[0])#cool timeとfcに分けるなぜこの変数名にしたか分からん
ct=int(I[1])
I=input().split()#二列目の入力とる
for c in range(fc):#fc回実行する何回目の実行かcに入れる
    if c!=0:
        if int(I[c-1])==int(I[c]):
            print(I[c])
            break
