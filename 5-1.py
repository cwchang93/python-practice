input1 = 'apple pen'
input2 = 'pineapple pen'
input_str = 'pen'

lst1 = input1.split()
lst2 = input2.split()
str_input = input_str

if str_input in lst1 or str_input in lst2:
    print(True)
else: 
    print(False)
