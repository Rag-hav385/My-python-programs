less_deposit = 0.10
more_deposit = 0.25

less = int(input("no of containers less than 1 l"))
more = int(input("no. of containers more than 1l"))

amnt = less_deposit*less + more_deposit*more

print(  amnt)