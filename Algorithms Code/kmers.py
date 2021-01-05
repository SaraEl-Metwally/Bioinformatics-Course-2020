   def kmers(seq,k):
    for i in range (len(seq)-k+1):
        yield seq[i:i+k]


if __name__=='__main__':
    for km in kmers("GACTGTA",3):
        print(km)
