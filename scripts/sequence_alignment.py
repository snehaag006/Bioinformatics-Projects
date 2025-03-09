from Bio import Align

seq1 = "AGTACGCA"
seq2 = "TATGC"

# Create an aligner object
alignments = Align.PairwiseAligner()

# Perform global alignment
alignments = aligner.align(seq1, seq2)

# Print the alignments
for alignment in alignments:
    print(alignment)