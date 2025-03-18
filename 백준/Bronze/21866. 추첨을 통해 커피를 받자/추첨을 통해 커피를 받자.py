array = list(map(int,input().split()))
score = [100,100,200,200,300,300,400,400,500]

for i in range(9):
    if array[i] > score[i]:
        print('hacker')
        exit()

if sum(array) >= 100:
    print('draw')
else:
    print('none')