"""
Programming Homework 4
"""


import itertools as it

from Greedy_Algorithm import greedy_scs
from overlap import overlap


def main():
    ss = ['ABC', 'BCA', 'CAB']
    print ("Test 1: %s" % scs(ss)[0])
    ss = ['CCT', 'CTT', 'TGC', 'TGG', 'GAT', 'ATT']
    print("Qusetion 1: %s" % len(scs(ss)[0]))
    ss = ['ABC', 'BCA', 'CAB']
    print ("Example 1: %s" % scs(ss)[1])
    ss = ['GAT', 'TAG', 'TCG', 'TGC', 'AAT', 'ATA']
    print ("Example 2: %s" % scs(ss)[1])
    ss = ['CCT', 'CTT', 'TGC', 'TGG', 'GAT', 'ATT']
    print("Qusetion 2: %s" % len(scs(ss)[1]))
    seq, qual = readFastq('ads1_week4_reads.fq')
    print("Qusetion 3: %s" % assemble_reads(seq)[0])
    print("Qusetion 4: %s" % assemble_reads(seq)[1])


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


def scs(ss):
    """ Returns shortest common superstring of given
        strings, which must be the same length """
    shortest_sup = None
    lst_sup = []
    lst_shortest = []

    for ssperm in it.permutations(ss):
        sup = ssperm[0]  # superstring starts as first string
        for i in range(len(ss) - 1):
            # overlap adjacent strings A and B in the permutation
            olen = overlap(ssperm[i], ssperm[i + 1], min_length=1)
            # add non-overlapping portion of B to superstring
            sup += ssperm[i + 1][olen:]

        lst_sup.append(sup)

        if shortest_sup is None or len(sup) < len(shortest_sup):
            shortest_sup = sup  # found shorter superstring

    for i in lst_sup:
        if len(i) == len(shortest_sup):
            lst_shortest.append(i)

    return shortest_sup, sorted(lst_shortest)


def assemble_reads(reads):
    for k in range(100, 1, -1):
        genome = greedy_scs(reads, k)
        if len(genome) == 15894:
            a = genome.count('A')
            t = genome.count('T')
    return a, t, genome

if __name__ == '__main__':
    main()
