"""
What is the length of the longest ORF appearing in reading frame 2 of any of the sequences?
"""

string = open("dna2.fasta").readlines()

sequences = []
seq = ""

for s in string:
	if not s.startswith('>'):
		s = s.replace(" ", "")
		s = s.replace("\n", "")
		seq = seq + s
	else:
		sequences.append(seq)
		seq = ""
		
#add tht last seq
sequences.append(seq)

sequences = sequences[1:]

# Find the reading frame 2
def find_rf_2(sequence):
	#Find all ATG indexs
	start_position = 1
	start_indexs = []
	stop_indexs = []
	
	for i in range(1, len(sequence), 3):
		if sequence[i:i+3] == "ATG":
			start_indexs.append(i)
			
	for i in range(1, len(sequence), 3):
		stops = ["TAA", "TAG", "TGA"]
		if sequence[i:i+3] in stops:
			stop_indexs.append(i)
			
	orf = []
	mark = 0
	for i in range(0, len(start_indexs)):
		for j in range(0, len(stop_indexs)):
			if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
				orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
				mark = stop_indexs[j] + 3
				break
	return orf
	
n = 1
lengths = []
for i in sequences:
	orfs = find_rf_2(i)
	for j in orfs:
		lengths.append(len(j))
		
print(max(lengths))
	