l = list(map(int,input().split(" ")))
for i in range(1,len(l)+2):
    if i not in l :
        print(i)