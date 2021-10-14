# t="There would have been a time for such a world"
# print(t.find("world"))


def naive(p,t):
    occerance=[]
    for i in range(len(t)-len(p)+1):
        match=True
        for j in range(len(p)):
            if t[i+j]!=p[j]:
                match=False
                break
            if match:
                occerance.append(i)
    return occerance

#خاص بالفانكشن naive calling
# text="AGCTGTTTAGCT"
# pattern="AGC"
# print(naive(pattern,text))

def readGenome(filename):
    genome=' '
    with open(filename,'r')as f:
        for line in f:
            if line[0]!='>':
                genome+=line.rstrip()
    return genome

genome=readGenome(r"E:\faculty\work\bioinformatics\Sections\Fifth week bio\ecoli_rel606.fasta")
#print(genome)


#create random pattern

import random
def generateReads(genome,numReads,readLen):
    reads=[]
    for _ in range(numReads):
        start=random.randint(0,len(genome)-readLen)-1
        reads.append(genome[start:start+readLen])
    return reads

patterns=generateReads(genome,10,100)
numMatched=0
def numMatch():
    numMatched=0
    for p in patterns:
        matches=naive(p,genome)
        if len(matches)>0:
            numMatched+=1
    return numMatched

print(numMatch())