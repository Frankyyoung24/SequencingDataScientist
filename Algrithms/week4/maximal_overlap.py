from collections import defaultdict

from overlap import overlap


def pick_maximal_overlap(reads, k):
    reada, readb = None, None
    best_olen = 0
    index = defaultdict(set)
    for read in reads:
        for i in range(len(read) - k + 1):
            index[read[i:i + k]].add(read)

    for r in reads:
        for o in index[r[-k:]]:
            if r != o:
                olen = overlap(r, o, k)
                if olen > best_olen:
                    reada, readb = r, o
                    best_olen = olen

    return reada, readb, best_olen
