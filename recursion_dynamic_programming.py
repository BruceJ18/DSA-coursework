# ---------- longest common subsequence portion
seq1 = 'serendipitous'
seq2 = 'precipitation'
def longest_common_subseq(seq1, seq2, idx1=0, idx2=0):
    if idx1 == len(seq1) or idx2 == len(seq2):
        return 0
    elif seq1[idx1] == seq2[idx2]:
        return 1 + longest_common_subseq(seq1, seq2, idx1+1, idx2+1)
    else:
        option1 = longest_common_subseq(seq1, seq2, idx1+1, idx2)
        option2 = longest_common_subseq(seq1, seq2, idx1, idx2+1)
        return max(option1, option2)

print(longest_common_subseq(seq1, seq2))
