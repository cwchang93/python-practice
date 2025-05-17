# x = "0"

# while x != "-1":
#     cl =0
#     for char in x:
#         cl +=1
#     print(cl)
#     x=input("請輸入任意長度數字或-1 結束程式.")

def tables():
    for x in range(3, 16):      # 外層控制每一列
        for y in range(3, 16):  # 內層控制每一個乘數
            print(x * y, end=' ')
        print()


tables()