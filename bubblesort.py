def bubble(a):

    n = len(a)
    temp = 0
    for i in range(n):
        for j in range(i-n-1):
            if(a[j+1] > a[j]):
                  temp = a[j]
                  a[j] = a[j+1]
                  a[j+1]= temp


a = [1,5,4,6,7,8]



for i in a:
    print(i)
