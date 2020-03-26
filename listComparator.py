#def common_member(a, b): 
      
    #a_set = set(a) 
    #b_set = set(b) 
      
    # check length  
    #if len(a_set.intersection(b_set)) > 0: 
        #return(a_set.intersection(b_set))   
    #else: 
        #return("no common elements") 
      
   
#a = [1, 2, 6, 4, 5] 
#b = [5, 6, 7, 8, 9] 
#list3 =common_member(a,b)
#print(list3)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 21]

c = []

for i in b:
    if i in a:
        c.append(i)

print(c)