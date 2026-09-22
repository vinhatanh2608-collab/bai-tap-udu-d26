import random
n = random.randint(1,10)
while 1:
    x = int(input())
    if x == n:
        print("True")
        break
    else:
        if x < n :
            print("nho hon")
        elif x > n:
            print("lon hon")