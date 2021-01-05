def parse_fastq(fh):
    reads=[]
    while True:
        header=fh.readline()
        if(len(header)==0):
            break
        seq=fh.readline().rstrip()
        fh.readline()
        qual=fh.readline().rstrip()
        reads.append((seq,qual))
    return reads


if __name__=='__main__':
    fname="/Users/sarael-metwally/Documents/Bioinformatics/SP1.fq"
    f=open(fname,'r')
    reads=[]
    reads=parse_fastq(f)
    print(reads[1])
    print(len(reads))
    f.close()
    
