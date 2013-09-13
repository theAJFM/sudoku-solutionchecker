def solve():
    box = []
    correct = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for count in range(0,9):
        box.append([int(i) for i in input().strip().split(' ')]);

    
    for x in box:
        if(len(set(correct) - set(x))>0):
            return 'NO'

    
    for it in range(0, 9):
        empty = []
        for jt in range(0, 9):
            empty.append(box[jt][it])
        if(len(set(correct) - set(empty))>0):
            return 'NO'

    for it in range(0, 9, 3):
        set1 = []
        set2 = []
        set3 = []
        set1 += box[it][0:3]+box[it+1][0:3]+box[it+2][0:3]
        set2 += box[it][3:6]+box[it+1][3:6]+box[it+2][3:6]
        set3 += box[it][6:9]+box[it+1][6:9]+box[it+2][6:9]
        if(len(set(correct) - set(set1))>0 or len(set(correct) - set(set2))>0 or len(set(correct) - set(set3))>0):
            return 'NO'
        

    return 'YES'
    
            

print(solve())
