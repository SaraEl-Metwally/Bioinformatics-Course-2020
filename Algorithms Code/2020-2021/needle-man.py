import numpy as np
def match_score(c1,c2):
    if c1==c2:
        return match
    elif c1=="-" or c2=="-":
        return gap
    else:
        return mismatch

def needle(seq1,seq2):
    m,n=len(seq1),len(seq2)
    scores=np.zeros((m+1,n+1),dtype=int)
    for i in range(0,m+1):
        scores[i][0]=gap*i
    for j in range(0,n+1):
        scores[0][j]=gap*j

    for i in range(1,m+1):
        for j in range(1,n+1):
            diagonal=scores[i-1][j-1]+match_score(seq1[i-1],seq2[j-1])
            up=scores[i-1][j]+gap
            left=scores[i][j-1]+gap
            scores[i][j]=max(diagonal,up,left)

    align1,align2='',''
    i,j=m,n
    while i>0 or j>0:
        score_current=scores[i][j]
        score_diagonal=scores[i-1][j-1]
        score_left=scores[i][j-1]
        score_up=scores[i-1][j]

        if score_current==score_diagonal+match_score(seq1[i-1],seq2[j-1]):
            a1,a2=seq1[i-1],seq2[j-1]
            i,j=i-1,j-1
        elif score_current==score_up+gap:
            a1,a2=seq1[i-1],"-"
            i-=1
        elif score_current==score_left+gap:
            a1,a2="-",seq2[j-1]
            j-=1

        align1+=a1
        align2+=a2
    align1=align1[::-1]
    align2=align2[::-1]

    print(scores)
    print("scores= "+ str(scores[m,n]))
    print(align1)
    print(align2)





match=1
mismatch=-1
gap=-1
seq1="GATTACA"
seq2="GCATGCT"
needle(seq1,seq2)