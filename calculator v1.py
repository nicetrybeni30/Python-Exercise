#Let's create a mini project "Calculator"

#select operator
operator = input("Operator:")
firstnumber = int(input("First number: "))
secondnumber = int(input("Second number: "))
x = firstnumber
y = secondnumber
total_sum = x + y
z = total_sum


if operator == "addition":
    print(x + y)
elif operator == "subtraction":
    print(x-y)
elif operator == "division":
    print(x/y)
else:
    print(x*y)




