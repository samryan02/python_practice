from datetime import datetime
startTime = datetime.now()

i = 0
for i in range(1, 1000000):
    num = True
    j = 2
    
    for j in range(2, i-1):
        if i%j == 0:
            num = False
            break
        j = j+1
    if num == True:
        print(i)
    i = i+1

print(datetime.now() - startTime)