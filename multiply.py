def tables():
    for x in range(3,16):
        for y in range(3,16):
            print(x,'*',y,'=',x*y, end=' ')
        print()

tables()