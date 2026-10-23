#multiplication table
number=int(input("Enter a number: "))
for loop_var in range(1,11):
    product=(number)* loop_var 
    print(f"{number} x{loop_var} = {product}") 
while loop_var <= 10:
    product = (number)* loop_var
    print(f"{number} x {loop_var} = {product}") 