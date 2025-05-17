def power(a, b):
  return a**b


base = input("請輸入底數:")

exp = input("請輸入指數:")

res = power(base, exp)    

def testFn():
  for num in range(10):
    print('num', num)
  print('hi')