def boyer_moore(p, p_bm, t):
    """
    Do Boyer-Moore matching.
    p = pattern, t = text, p_bm = Boyer-Moore object for p (index)
    """
    i = 0  # track where we are in the text
    occurrences = []  # the index that p match t
    while i < len(t) - len(p) + 1:
        # loop though all the positions in t where p should start
        shift = 1
        mismatched = False
        for j in range(len(p) - 1, -1, -1):
            # the 3rd word '-1' means we're going backwards
            if not p[j] == t[i + j]:  # when we have a mismatch
                # calculate the bad character rule and good suffix rule to see
                # how many bases we can skip
                skip_bc = p_bm.bad_character_rule(j, t[i + j])
                skip_gs = p_bm.good_suffix_rule(j)
                # calculate the max shift bases.
                shift = max(shift, skip_bc, skip_gs)
                mismatched = True
                break
        if not mismatched:  # if there is no mismatch.
            occurrences.append(i)
            # if there is no mismatch we don't need to use the
            # bad_character_rule
            skip_gs = p_bm.match_skip()
            shift = max(shift, skip_gs)
        i += shift  # add the value of shift to i

    return occurrences
