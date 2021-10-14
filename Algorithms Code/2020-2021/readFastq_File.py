import matplotlib.pyplot as plt


def readFastq(filename):
    seqs = []
    quals = []
    with open(filename) as fo:
        while True:
            fo.readline()
            seq = fo.readline()
            fo.readline()
            qual = fo.readline()
            if len(seq) == 0:
                break
            seqs.append(seq)
            quals.append(qual)
    return seqs, quals


sequences, qualities = readFastq(
    r"E:\faculty\work\bioinformatics\Sections\fourth_week_bioinformatics\sample.fastq")
print(sequences[:5])
print(qualities[:4])


# def Phred33ToQ(qualities):
#     Q=[]
#     for qual in qualities:
#         for phred in qual:
#             Q.append(ord(i)-33)
#     return Q
#
#
# print(Phred33ToQ(qualities))


def Phred33ToQ(qual):
    return ord(qual)-33
print(Phred33ToQ('R'))


def createHist(qualities):
    hist = [0] * 50
    for qual in qualities:
        for phred in qual:
            q = Phred33ToQ(phred)
            hist[q] += 1

    return hist


h = createHist(qualities)
print(h)

plt.bar(range(len(h)), h)
plt.show()
