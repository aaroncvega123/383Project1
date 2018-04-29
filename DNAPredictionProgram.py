#from seq1Data import sequences as sq
from sklearn import svm

trait_length = 20
sets_desired = 190

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
    seq_file = open("CLEAN_RAW_H3N2_ALIGNED.fasta", 'r')
    raw_data = seq_file.readlines()
    current_seq = []

    standard_length = 2832
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

                if base == 'a' or base == 'A':
                    current_seq.append(1)
                elif base == 't' or base == 'T':
                    current_seq.append(2)
                elif base == 'c' or base == 'C':
                    current_seq.append(3)
                elif base == 'g' or base == 'G':
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
    clf.fit(trait_sets[:-1], targets[:-1])  


def all_equal_length():
    length = len(sequences[0])
    for seq in sequences:
        print(len(seq))
        if len(seq) != length:
            return False
    return True

def predict_sequence(j):
    ret = []

    seq_length = len(sequences[0])

    for i in range(seq_length):
        trait_set = []
        trait_set.append([])

        for k in range(trait_length):
            base = sequences[sets_desired+j+k][i]
            trait_set[0].append(base)

        ret.append(clf.predict(trait_set)[0])
    
    return ret

def storeCLF(fileName):
    import cPickle
    with open(fileName, 'wb') as fid:
        cPickle.dump(clf, fid)
            
def loadCLF(fileName):
    import cPickle
    with open(fileName, 'rb') as fid:
        ret = cPickle.load(fid)
    return ret


def main():
    """
    Code goes here
    """


    print("Program started...")

    load_data_into_sequences()
    print("Done loading sequences")

    load_sequences_into_traits()
    print("Done loading into traits")

    train_program()
    print("Done training")

    storeCLF('2016_clf.pkl')
    print("Done storing clf")

    predictedSeq = predict_sequence(1)
    print("Done predicting")

    print(predictedSeq)

main()