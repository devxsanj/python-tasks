def sumEvenNumbers():
    sum = 0
    x = range(1,69)
    for s in x:
        if s % 2 == 0:
            sum += 1
    return sum
    
    
print("Sum of even numbers are: ", sumEvenNumbers())