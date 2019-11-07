for i in range(10):
    for row in range(10):
        print('*',end=' ')
    print()

for col in range(5):
    for row in range(col):
        print(' '*4-int(col),'*',end=' ')
    print()