#from seq1Data import sequences as sq
from sklearn import svm

trait_length = 20
sets_desired = 80

trait_sets = []
targets = []
sequences = [] #should be 2D list with all sequences

clf = svm.SVC(gamma=0.001, C=100.)


"""
Should load all DNA sequences into 'sequences' as numbers.
    _ = 0    
    A = 1
    T = 2
    C = 3
    G = 4
"""
def load_data_into_sequences():
    """
    Will read from fasta file and fill sequences
    """
    seq_file = open("aligned_fasta_H3N2A_23APR2018.aln", 'r')
    raw_data = seq_file.readlines()
    current_seq = []

    standard_length = 1737
    #print(standard_length)

    for line in raw_data:
        if line[0] == '>':
            if len(current_seq) > 0:

                while len(current_seq) < standard_length:
                    current_seq.append(0)
                #print(len(current_seq))
                sequences.append(current_seq)  

            current_seq = []
        else:
            for base in line:

                if base == 'a':
                    current_seq.append(1)
                elif base == 't':
                    current_seq.append(2)
                elif base == 'c':
                    current_seq.append(3)
                elif base == 'g':
                    current_seq.append(4)
                elif base == '-':
                    current_seq.append(0)

            

    


"""
Each list inside trait_sets will include a set of bases,
vertically extracted sequences.

Example:    If we have these sequences:

            AATC
            TATG
            ATAC
            TTTG

            the first trait set will be [1, 2, 1] with a
            target of 2 (see load_data_into_sequences for
            letter to number mapping)
"""

def load_sequences_into_traits():
    #assuming all sequences have equal size
    seq_length = len(sequences[0])

    for i in range(seq_length):
        for j in range(sets_desired):
            trait_set = []
            for k in range(trait_length):

                base = sequences[j+k][i]

                trait_set.append(base)

            trait_sets.append(trait_set)
            targets.append(sequences[j + trait_length][i])


def set_sequences_from_seq1Data():
    return 1

def train_program():
    clf.fit(trait_sets, targets)  

"""
def all_equal_length():
    length = len(sequences[0])
    for seq in sequences:
        print(len(seq))
        if len(seq) != length:
            return False
    return True
"""

def main():
    """
    Code goes here
    """
    
    load_data_into_sequences()
    load_sequences_into_traits()
    train_program()
    print("Done training")
    #print(len(targets))

main()