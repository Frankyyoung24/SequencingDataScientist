"""
Programming Homework 1.

First, look fo occurrences of both the forward and the reverse complement of P in T.
Second, make sure the result should be reported only once.
"""


def main():
    virus = readGenome('lambda_virus.fa')
    print ("RC Example 1: %s" % example_rc_1('CCC', 'AAAAAAAAAA'))
    print ("RC Example 2: %s" % example_rc_2('CGCG', 'AAAAAAAAAA'))
    print ("RC Example 3: \n"
           'offset of leftmost occurrence: %d and\n# occurrences: %d' %
           (min(example_rc_3('ATTA', readGenome('phix.fa'))), len(example_rc_3('ATTA', readGenome('phix.fa')))))
    print ("Well done! Examples all passed!")
    print ("Question 1: %s" % len(question_1_4('AGGT', virus)))
    print ("Question 2: %s" % len(question_1_4('TTAA', virus)))
    print ("Question 3: %s" % question_1_4('ACTAAGT', virus)[0])
    print ("Question 4: %s" % question_1_4('AGTCGA', virus)[0])
    print ("2mm Example 1: %s" % example_2mm_1('CTGT', 'AAAAAAAAAA'))
    print ("2mm Example 2: \n"
           'offset of leftmost occurrence: %d and\n# occurrences: %d' %
           (min(example_2mm_2('GATTACA', readGenome('phix.fa'))), len(example_2mm_2('GATTACA', readGenome('phix.fa')))))
    print ("Well done! Examples all passed!")
    print ("Question 5: %s" % len(question_5_6('TTCAAGCC', virus)))
    print ("Question 6: %s" % question_5_6('AGGAGGTT', virus)[0])
    print ("Question 7: %s" % question_7('ERR037900_1.first1000.fastq'))


def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()

    return genome


def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename, 'r') as fh:
        while True:
            fh.readline()  # skip name line
            seq = fh.readline().rstrip()  # read base sequence
            fh.readline()  # skip placeholder line
            qual = fh.readline().rstrip()  # base quality line
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities


def naive(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignment
        match = True
        for j in range(len(p)):  # loop over characters
            if t[i + j] != p[j]:  # compare characters
                match = False
                break
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences


def reverseComplement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t


def naive_with_rc(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        for seq in (p, reverseComplement(p)):
            match = True
            for j in range(len(seq)):  # loop over characters
                if t[i + j] != seq[j]:  # compare characters
                    match = False
                    break
            if match:
                occurrences.append(i)  # all chars matched; record
                break
    return occurrences


def naive_2mm(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):
        match = True
        mismatch = 0
        for j in range(len(p)):
            if t[i + j] != p[j]:
                mismatch += 1
                if mismatch > 2:
                    match = False
                    break
        if match:
            occurrences.append(i)
    return occurrences


def phred33ToQ(qual):
    return ord(qual) - 33


def lowQual(filename):
    seq, qual = readFastq(filename)
    total = [0] * len(qual[0])  # make a list with 0 in the length of qual
    for q in qual:
        for i, phred in enumerate(q):  # useful function
            total[i] = phred33ToQ(phred)
    print(total)

    return total.index(min(total))


def example_rc_1(p, t):
    t = t + 'CCC' + t + 'GGG' + t
    occurrences = naive_with_rc(p, t)
    return occurrences


def example_rc_2(p, t):
    t = t + 'CGCG' + t + 'CGCG' + t
    occurrences = naive_with_rc(p, t)
    return occurrences


def example_rc_3(p, t):
    occurrences = naive_with_rc(p, t)
    return occurrences
    print ('offset of leftmost occurrence: %d' % min(occurrences))
    print('# occurrences: %d' % len(occurrences))


def question_1_4(p, t):
    occurrences = naive_with_rc(p, t)
    return occurrences


def example_2mm_1(p, t):
    t = t + 'CTGT' + t + 'CTTT' + t + 'CGGG' + t
    occurrences = naive_2mm(p, t)
    return occurrences


def example_2mm_2(p, t):
    occurrences = naive_2mm(p, t)
    return occurrences


def question_5_6(p, t):
    occurrences = naive_2mm(p, t)
    return occurrences


def question_7(filename):
    result = lowQual(filename)
    return result

if __name__ == '__main__':
    main()
