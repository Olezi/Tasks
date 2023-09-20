def pythagorean(ar):
    
    ar.sort()
    
   
    a = ar[0]
    b = ar[1]
    c = ar[2]
    
    if a**2 + b**2 == c**2:
        return True
    else:
        return False


test1 = [5, 3, 4]
test2 = [6, 8, 10]
test3 = [100, 3, 65]

print(pythagorean(test1))  
print(pythagorean(test2))  
print(pythagorean(test3))  
