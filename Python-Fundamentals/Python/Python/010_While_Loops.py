

"""
While some condition is true:
    do someyhing
    test if the condition is still true
    
    
"""


i = 1
while i <= 5:
    print(i)
    i +=1
    
i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1