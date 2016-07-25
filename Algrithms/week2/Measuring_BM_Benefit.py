"""
Programming Homework 2.

Based on the given python module "Boyer-Moore preprocessing" and the human chromosome 1.

implement versions of the naive matching and BM algorithms that additionally count return
1) the number of character comparisions performed
2) the number of alignments tried.

Roughly speaking, these measure how much work the two different algorithms are doing.

"""

from bm_preproc import BoyerMoore
from kmer_index import Index
from SubseqIndex import SubseqIndex


def main():
    chr = readGenome("chr1.GRCh38.excerpt.fasta")
    p = 'GGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGG'
    p_bm = BoyerMoore(p)
    print("Question 1: %d" % naive(p, chr)[1])
    print("Question 2: %d" % naive(p, chr)[2])
    print("Question 3: %d" % boyer_moore(p, p_bm, chr)[1])
    p = 'GGCGCGGTGGCTCACGCCTGTAAT'
    print("Question 4: %d" % len(approximate_match(p, chr, 2)[0]))
    print("Question 5: %d" % approximate_match(p, chr, 2)[1])
    print("Question 6: %d" % approximate_match_subseq(p, chr, 2, 3)[1])


def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()
    return genome


def boyer_moore(p, p_bm, t):
    """
    Do Boyer-Moore matching.
    p = pattern, t = text, p_bm = Boyer-Moore object for p
    """
    i = 0
    occurrences = []
    comparisons = 0
    alignments = 0

    while i < len(t) - len(p) + 1:
        alignments += 1
        shift = 1
        mismatched = False

        for j in range(len(p) - 1, -1, -1):
            comparisons += 1

            if not p[j] == t[i + j]:
                skip_bc = p_bm.bad_character_rule(j, t[i + j])
                skip_gs = p_bm.good_suffix_rule(j)
                shift = max(shift, skip_bc, skip_gs)
                mismatched = True
                break

        if not mismatched:
            occurrences.append(i)
            skip_gs = p_bm.match_skip()
            shift = max(shift, skip_gs)

        i += shift

    return occurrences, alignments, comparisons


def naive(p, t):
    occurrences = []
    comparisons = 0
    alignments = 0
    for i in range(len(t) - len(p) + 1):
        alignments += 1
        match = True

        for j in range(len(p)):
            comparisons += 1
            if t[i + j] != p[j]:
                match = False
                break

        if match:
            occurrences.append(i)

    return occurrences, alignments, comparisons


def approximate_match(p, t, n):
    segment_length = int(round(len(p) / (n + 1)))
    all_matches = set()
    p_idx = Index(t, segment_length)
    idx_hits = 0

    for i in range(n + 1):
        start = i * segment_length
        end = min((i + 1) * segment_length, len(p))
        matches = p_idx.query(p[start:end])

        for m in matches:
            idx_hits += 1
            if m < start or m - start + len(p) > len(t):
                continue

            mismatches = 0
            for j in range(0, start):
                if not p[j] == t[m - start + j]:
                    mismatches += 1
                    if mismatches > n:
                        break

            for j in range(end, len(p)):
                if not p[j] == t[m - start + j]:
                    mismatches += 1
                    if mismatches > n:
                        break

            if mismatches <= n:
                all_matches.add(m - start)

    return list(all_matches), idx_hits


def approximate_match_subseq(p, t, n, ival):
    segment_length = int(round(len(p) / (n + 1)))
    all_matches = set()
    p_idx = SubseqIndex(t, segment_length, ival)
    idx_hits = 0
    for i in range(n + 1):
        start = i
        matches = p_idx.query(p[start:])

        for m in matches:
            idx_hits += 1
            if m < start or m - start + len(p) > len(t):
                continue

            mismatches = 0

            for j in range(0, len(p)):
                if not p[j] == t[m - start + j]:
                    mismatches += 1
                    if mismatches > n:
                        break

            if mismatches <= n:
                all_matches.add(m - start)
    return list(all_matches), idx_hits


if __name__ == '__main__':
    main()
