def sort_two_seqs(a:'',b):
    ''' sort two sequences and return them as lists \
        a is first sequence and both lists are sorted in the same order as a\
            uto length of a'''

    seq1,seq2 = zip(*sorted(zip(a, b)))
    return list(seq1),list(seq2)


b1 = [i for i in range(10)]
a1 = range(30,2,-1)

a1_sorted, b1_sorted = sort_two_seqs(a1, b1)

print('original a1 series:',a1,'sorted a1 series',a1_sorted)
print('original b1 series:',b1,'sorted b1 series',b1_sorted)
