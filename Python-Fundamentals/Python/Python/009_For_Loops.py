


"""
for each element in a collection:
    do  stuff

"""

my_string = " Cup of Coffee"

for i in my_string:
    
    print(i.upper(), end=" ")
    

my_list = [1,2,3,4,5,6,7,8,9]

for i in my_list:
    i_squared = i ** 2
    print(i,i_squared)
    
for i in my_list:
   print(i,i ** 2)    
   
for i in my_list:
    print(i, "Loop Finished", type(i))
    
    
my_list = ["a", "b", "c"]

for idx, i in enumerate(my_list):
     print(idx, i)
     
for i in range(0,21):
    if i % 3 == 0:
        continue
    print(i)