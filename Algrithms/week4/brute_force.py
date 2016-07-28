import itertools as it

from overlap import overlap


def scs(ss):  # ss means the set of strings
    shortest_sup = None
    # the permutations function is very useful
    for ssperm in it.permutations(ss):
        sup = ssperm[0]
        for i in range(len(ss) - 1):
            olen = overlap(ssperm[i], ssperm[i + 1], min_length=1)
            # add the suffix from the overlap length to the end
            sup += ssperm[i + 1][olen:]
    if shortest_sup is None or len(sup) < len(shortest_sup):
        shortest_sup = sup

    return shortest_sup
