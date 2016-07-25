def approximate_match(p, t, n):  # n means the max mismatch allowed
    # figure out the length of these segment
    segment_length = int(round(len(p) / (n + 1)))
    all_matches = set()
    for i in range(n + 1):
        start = i * segment_length  # start position
        end = (i + 1) * segment_length  # end position
        # use BM script to create the pattern_bm
        p_bm = BoyerMoore(p[start:end], alphabet='ACGT')
        # use BM algorithm to caculate the match positions
        matches = boyer_moore(p[start:end], p_bm, t)

        for m in matches:
            # look the left and right to check all the mismatches
            if m < start or m - start + len(p) > len(t):
                continue

            mismatches = 0
            for j in range(0, start):  # the first part of above funcion "if m < start"
                if not p[j] == t[m - start + j]:
                    mismatches += 1
                    if mismatches > n:
                        break

            # the second part of above funciton "m - start + len(p) > len(t)"
            for j in range(end, len(p)):
                if not p[j] == t[m - start + j]:
                    mismatches += 1
                    if mismatches > n:
                        break

            if mismatches <= n:
                # "m-start" means the begging of p
                all_matches.add(m - start)

    return list(all_matches)
