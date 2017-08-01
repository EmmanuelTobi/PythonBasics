#a function to return a list that has its first element as count of postive numbers and 
#and second element as sum of negative element
def manipulate_data(nl):

    p = []

#loop to check the input list has positive values and put into the empty list of p
    
    for i in range(0, len(nl)):
        
        if (nl[i]) == abs(nl[i]):
             
            p.append(nl[i])
             
            a = len(p) 


    q = []

#loop to check the input list has positive values and put into empty list of q

    for j in range(0, len(nl)):

        if (nl[j] * 1) != abs(nl[j]):
            
            q.append(nl[j])
#to calculate all the negative values in the list q          
            s = 0
            
            for k in q:
                s = s + k
        
    mdata = [a, s]

    return mdata

print manipulate_data([1,5,5,9,7,3,0,4,-17,1,6,-9,0,1,7,-1,3,-3])