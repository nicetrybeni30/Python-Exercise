def fibonacci(n):
    a, b = 0, 1
    total_sum = a 
    for x in range(n-1):
        print(a, end = " ")
        a, b = b, a + b
        total_sum += a
    return total_sum

terms = int(input("Enter number: "))
total = fibonacci(terms)
print(total)