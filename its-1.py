#1

# def year_to_roc():
#     year = input("Please enter year: ")
#     print('y',type(year))

#     roc = eval(year) - 1911
#     print('eval yr',type(eval(year)))
#     print('roc',type('roc'))

#     msg = "中華民國"+ str(roc) + "年" 
#     print(msg)

# year_to_roc();


# def q3():
#     v1 = 35
#     v2 = 8
#     v3 = 3.0
#     ans = (v1% V2 * 100) // 2.0 ** v3 - V2
#     print(ans)

# q3();

def func1(x, y):
    return x/y
 
a = input("請輸入第一個數字:")
b = input("請輸入第二個數字:")
result = func1(a, b)
print("兩數相除等於", result)