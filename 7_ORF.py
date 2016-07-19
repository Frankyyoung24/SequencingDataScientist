"""
What is the length of the longest forward ORF that appears in the sequence with the identifier gi|142022655|gb|EQ086233.1|16?
"""
string = open("dna2.fasta").readlines()

# Find the sequence with the identifier gi|142022655|gb|EQ086233.1|16

seq = ""
identifier = 0

for i in range(0, len(string)):
    if "gi|142022655|gb|EQ086233.1|16" in string[i]:
        identifier = i

for s in string[identifier+1:]:
    if not s.startswith('>'):
        s = s.replace(" ", "")
        s = s.replace("\n", "")
        seq = seq + s
    else:
        break

# Find ORF 1
def find_orf_1(sequence):
    # Find all ATG indexs
    start_position = 0
    start_indexs = []
    stop_indexs = []

    for i in range(0, len(sequence), 3):
        if sequence[i:i+3] == "ATG":
            start_indexs.append(i)

    # Find all stop codon indexs
    for i in range(0, len(sequence), 3):
        stops = ["TAG", "TAA", "TGA"]
        if sequence[i:i+3] in stops:
            stop_indexs.append(i)

    orf = []
    mark = 0
    start_position = {}

    for i in range(0, len(start_indexs)):
        for j in range(0, len(stop_indexs)):
            if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
                orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
                start_position[len(sequence[start_indexs[i]:stop_indexs[j]+3])] = start_indexs[i]
                mark = stop_indexs[j]+3
                break

    return orf

# Find ORF 2
def find_orf_2(sequence):
    # Find all ATG indexs
    start_position = 1
    start_indexs = []
    stop_indexs = []

    for i in range(1, len(sequence), 3):
        if sequence[i:i+3] == "ATG":
            start_indexs.append(i)

    # Find all stop codon indexs
    for i in range(1, len(sequence), 3):
        stops = ["TAG", "TAA", "TGA"]
        if sequence[i:i+3] in stops:
            stop_indexs.append(i)

    orf = []
    mark = 0
    start_position = {}

    for i in range(0, len(start_indexs)):
        for j in range(0, len(stop_indexs)):
            if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
                orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
                start_position[len(sequence[start_indexs[i]:stop_indexs[j]+3])] = start_indexs[i]
                mark = stop_indexs[j]+3
                break

    return orf

# Find ORF 3
def find_orf_3(sequence):
    # Find all ATG indexs
    start_position = 2
    start_indexs = []
    stop_indexs = []

    for i in range(2, len(sequence), 3):
        if sequence[i:i+3] == "ATG":
            start_indexs.append(i)

    # Find all stop codon indexs
    for i in range(2, len(sequence), 3):
        stops = ["TAG", "TAA", "TGA"]
        if sequence[i:i+3] in stops:
            stop_indexs.append(i)

    orf = []
    mark = 0
    start_position = {}

    for i in range(0, len(start_indexs)):
        for j in range(0, len(stop_indexs)):
            if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
                orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
                start_position[len(sequence[start_indexs[i]:stop_indexs[j]+3])] = start_indexs[i]
                mark = stop_indexs[j]+3
                break

    return orf

lengths = []
orfs = find_orf_1(seq) + find_orf_2(seq) + find_orf_3(seq)
for o in orfs:
    lengths.append(len(o))

print(max(lengths))
