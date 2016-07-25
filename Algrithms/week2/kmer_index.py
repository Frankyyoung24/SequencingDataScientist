import bisect


class Index(object):

    def __init__(self, t, k):  # pass it in a text t and a kmer length k
        """Create index from all substrings of size 'length'"""
        self.k = k  # k-mer length(k)
        self.index = []  # a list for the index
        # loop text t and take every kmer of length k in that text and add them
        # to the index along with their offset
        for i in range(len(t) - k + 1):  # for each k-mer
            # add a tuple with two associated values
            self.index.append((t[i:i + k], i))  # add (k-mer, offset) pair
        self.index.sort()  # alphabetize for k-mer

    def query(self, p):  # p is the pattern that we're going to match against the text
        """Return index hits for first k-mer of p"""
        # find the first k bases of p to look them up in the table
        kmer = p[:self.k]  # query the first k-mer
        # find the first position in the list where this kmer accurs.
        # sends all the indices in the list are greater than negative one. remember it is the tuple
        # assure that we always get the first occurrence of the list.
        i = bisect.bisect_left(self.index, (kmer, -1))  # binary k-mer
        hits = []  # where this kmer accurs
        while i < len(self.index):  # collect matching index entries
            if self.index[i][0] != kmer:
                break
            hits.append(self.index[i][1])
            i += 1
        return hits

    # def queryIndex(p, t, index):
        # k = index.k  # get the length of k from that index
        # offsets = []
        # the query function return the possible places where p could start
        # The query function return a list where the first k bases of p matches
        # the first k bases of t
        # but we still have to check that the rest of p matches t in that
        # location
        # for i in index.query(p):
        # if p[k:] == t[i + k:i + len(p)]:
        # offsets.append(i)
        # return offsets
