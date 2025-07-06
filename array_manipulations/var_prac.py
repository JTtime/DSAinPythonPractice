x=[2,3,4]

def arr_man(arr):
    

def change_array(y):
    y[0]=90   #pass by reference so it changes original input


change_array(x)
print("x:",x)

#output x: [90, 3, 4]


y=2

def change_variable(x):
    x+=25 #pass by value so it doesn't changes original input

change_variable(y)

print("y:", y)
#output is y: 2