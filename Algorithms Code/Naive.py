def naive(t,p):
    assert len(p)<=len(t)
    occ=[]
    for i in range(0,len(t)-len(p)+1):
        match=True
        for j in range(0,len(p)):
                       if t[i+j]!= p[j]:
                           match= False
                           break
        if match:
           occ.append(i)
    return occ           

if __name__=='__main__':
    t="CTTCTGTCTTTTTTCT"
    p="TCT"
    occ=[]
    occ=naive(t,p)
    print(occ)
            
