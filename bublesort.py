a = [12,4,6,145,6,6,6,6,6,8,17,-3]
ai = 0
for i in range(len(a)-1):
    for i in range(len(a)-i-1):
        if a[i] > a[i+1]:
            ai = a[i]
            a[i] = a[i+1]
            a[i+1]= ai
print(a)
