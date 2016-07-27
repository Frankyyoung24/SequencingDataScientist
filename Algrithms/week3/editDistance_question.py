"""
1. Rows of the dynamic programming matrix are labeled with the bases from P
   and columns with bases from T
2. Elements in the first Row are set to 0
3. Elements in the first column are set to 0, 1, 2..., as for edit distance
4. Other elements are set in the same way as elements of a standard edit distance matrix
5. The minimal value in the bottom row is the edit distance of the closet match between P and T

Parse the human chromosome 1. Adapt the editDistance function.
"""
from collections import defaultdict

from overlap import overlap


def main():
    chr = readGenome('chr1.GRCh38.excerpt.fasta')
    p = 'GCTGATCGATCGTACG'
    print("Question 1: %d" % editDistance(p, chr))
    p = 'GATTTACCAGATTGAG'
    print("Question 2: %d" % editDistance(p, chr))
    seq, qual = readFastq('ERR266411_1.for_asm.fastq')
    edge, suffix = overlap_graph(seq, 30)
    print("Question 3: ", edge)
    print("Qusetion 4: ", suffix)


def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()
    return genome


def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename, 'r') as fh:
        while True:
            fh.readline()
            seq = fh.readline().rstrip()
            fh.readline()
            qual = fh.readline().rstrip()
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities


def editDistance(x, y):
    D = []
    for i in range(len(x) + 1):
        D.append([0] * (len(y) + 1))
    # Initialize first row and column of matrix
    for i in range(len(x) + 1):
        D[i][0] = i
    for i in range(len(y) + 1):
        D[0][i] = 0
    # Fill in the rest of the matrix
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            distHor = D[i][j - 1] + 1
            distVer = D[i - 1][j] + 1
            if x[i - 1] == y[j - 1]:
                distDiag = D[i - 1][j - 1]
            else:
                distDiag = D[i - 1][j - 1] + 1

            D[i][j] = min(distHor, distVer, distDiag)
    # Edit distance is the vcalue in the bottom right corner of the matrix
    # return D[-1][-1]
    return min(D[-1])


def overlap_graph(reads, k):
    # make index
    index = defaultdict(set)  # remember the defaultdict function
    for read in reads:
        for i in range(len(read) - k + 1):
            index[read[i:i + k]].add(read)

    # make praph
    graph = defaultdict(set)
    for r in reads:
        for o in index[r[-k:]]:
            if r != o:
                if overlap(r, o, k):
                    graph[r].add(o)

    edges = 0
    for read in graph:
        edges += len(graph[read])

    return (edges, len(graph))

if __name__ == '__main__':
    main()
