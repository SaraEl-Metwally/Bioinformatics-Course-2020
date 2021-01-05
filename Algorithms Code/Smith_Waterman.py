import numpy as np

match = 2#3
mismatch = -1#-3
gap = -2

def match_score(c1, c2):
    if c1 == c2:
        return match
    elif c1 == '-' or c2 == '-':
        return gap
    else:
        return mismatch

def smith_waterman(seq1, seq2):
    m, n = len(seq1), len(seq2)
    score = np.zeros((m+1, n+1),dtype=int)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            diagnal = score[i-1][j-1] + match_score(seq1[i-1], seq2[j-1])
            up = score[i-1][j] + gap
            left = score[i][j-1] + gap
            score[i][j] = max(diagnal, up, left,0)

    print (score)  
    i,j = np.unravel_index(score.argmax(), score.shape)
    align1, align2 = '', ''
    while score[i,j]!=0:
        score_current = score[i][j]
        score_diagnal = score[i-1][j-1]
        score_left = score[i][j-1]
        score_up = score[i-1][j]
        
       

        if score_current == score_diagnal + match_score(seq1[i-1], seq2[j-1]):
            
            a1,a2 = seq1[i-1],seq2[j-1]
            i,j = i-1,j-1
        elif score_current == score_up + gap:
            
            a1,a2 = seq1[i-1],'-'
            i -= 1
        elif score_current == score_left + gap:
           
            a1,a2 = '-',seq2[j-1]
            j -= 1
        
        align1 += a1
        align2 += a2
            

    align1 = align1[::-1]
    align2 = align2[::-1]
    print(align1)
    print(align2)
    
    
    
    
    return; 

if __name__ == '__main__':
   # smith_waterman("GGTTGACTA","TGTTACGG")
     smith_waterman("CACGTGATCAA","AGCATCGGTTG")
    
