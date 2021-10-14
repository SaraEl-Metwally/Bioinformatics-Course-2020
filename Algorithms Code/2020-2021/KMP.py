def computeLPSArray(pattern):
    lps=[0]*len(pattern)
    j=0
    i=1
    while i<len(pattern):
        if pattern[i]==pattern[j]:
            j+=1
            lps[i]=j
            i+=1
        else:
            if j!=0:
                j=lps[j-1]
            else:
                lps[i]=0
                i+=1
    return lps


def KMP(pattern,text):
    M=len(pattern)
    N=len(text)

    j=0
    i=0

    lps=computeLPSArray(pattern)
    while i <N:
        if pattern[j]==text[i]:
            i+=1
            j+=1
        if j==M:
            print("pattern is founded at index "+str(i-j))
            j=lps[j-1]
        elif i<N and pattern[j]!=text[i]:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1





text = "ABABDABACDS"
pattern = "ABABCABAB"
print(computeLPSArray(pattern))
KMP(pattern,text)





