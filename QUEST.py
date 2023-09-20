def pythagorean(arr):
    
    arr.sort()
    
   
    a = arr[0]
    b = arr[1]
    c = arr[2]
    
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
