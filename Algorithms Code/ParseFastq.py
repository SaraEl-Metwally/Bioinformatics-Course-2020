import matplotlib.pyplot as plt
def parse_fastq(fh):
    reads=[]
    quals=[]
    while True:
        header=fh.readline()
        if(len(header)==0):
            break
        seq=fh.readline().rstrip()
        fh.readline()
        qual=fh.readline().rstrip()
        reads.append(seq)
        quals.append(qual)
    return reads,quals

def phred33toQ(qual):
    return ord(qual)-33
def createHist(qualities):
    hist=[0]*50
    for qual in qualities:
        for phred in qual:
            q=phred33toQ(phred)
            hist[q]+=1

    return hist           

if __name__=='__main__':
    fname="/Users/sarael-metwally/Documents/Bioinformatics/SP1.fq"
    f=open(fname,'r')
    reads,quals=parse_fastq(f)
    h=createHist(quals)
    #print(h)
    plt.bar(range(len(h)),h)
    plt.show()
    f.close()
    
