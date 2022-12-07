
def getBondDuration(y, face, couponRate, m, ppy = 1):
    
    y1 = y
    m1 = list(range(1,(m+1)))
    m2 = m
    pvm = []
    wpvm = []
    cf = couponRate*face
    pvcf = []
    pvcfsum = 0
    wcf = []
    wcfsum = 0
    duration = 0 
    
    if ppy == 2:
        m1 = list(range(1,(2*m+1)))
        y1 = y/2
        cf = cf*0.5
        m2 = m*2
       
    pvm = [(1+y1)**(-i) for i in m1]
    wpvm = [i*(1+y1)**(-i) for i in m1]
    
    pvcf = [cf*i for i in pvm]
    pvcf.append(face*(1+y1)**(-m2))
    pvcfsum = sum(pvcf) 
    wcf = [cf*i for i in wpvm]
    wcf.append(face*m2*(1+y1)**(-m2))
    wcfsum = sum(wcf)
    
    duration = wcfsum/pvcfsum
          
    return(duration)




    

    
    
    
    
   
