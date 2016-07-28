"""
Greddy shortest-common-superstring merge.
Repeat until no edges (overplas of length >= k) remain.
"""

from maximal_overlap import pick_maximal_overlap


def greedy_scs(reads, k):  # 'k' means the minimum overlaps.
    read_a, read_b, olen = pick_maximal_overlap(reads, k)
    while olen > 0:
        reads.remove(read_a)
        reads.remove(read_b)
        reads.append(read_a + read_b[olen:])
        read_a, read_b, olen = pick_maximal_overlap(reads, k)
    return ''.join(reads)
