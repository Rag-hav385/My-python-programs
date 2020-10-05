def binary(a , x):
    first_pos = 0
    last_pos = len(a)-1
    flag = 0
    
    while(first_pos < last_pos and flag == 0):
        mid = (first_pos + last_pos)//2
        if(a[mid] == x):
            print("found")
            flag = 1
        else:
            if(x < a[mid] ):
                last_pos = a[mid] - 1
            else:
                if(x > a[mid]):
                    first_pos = a[mid] + 1


a=[]
for i in range(1,501):
    a.append(i)

binary(a,50)
    