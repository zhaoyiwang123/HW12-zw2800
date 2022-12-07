

def FizzBuzz(start, finish):
    
    numvec = np.arange(start,(finish+1))
    objvec = np.array(numvec,dtype = object)
    

    for i in range(start,finish+1):
        if i%15 == 0:
            myEmptyList.append('fizzbuzz')
        elif i%5 == 0:
            myEmptyList.append('buzz')
        elif i%3 == 0:
            myEmptyList.append('fizz')
        else:
            myEmptyList.append(i)
         
        
    return(myEmptyList)
