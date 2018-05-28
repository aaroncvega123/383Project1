#from seq1Data import sequences as sq
from sklearn import svm
import os.path

#trait_length = 170
#sets_desired = 20

trait_sets = []
targets = []
sequences = [] #should be 2D list with all sequences

clf = svm.SVC(gamma=0.001, C=100.)

states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado', 'Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho', 'Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana', 'Maine', 'Maryland','Massachusetts','Michigan','Minnesota','Mississippi', 'Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South  Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']


"""
Should load all DNA sequences into 'sequences' as numbers.
    _ = 0    
    A = 1
    T = 2
    C = 3
    G = 4
"""
def load_data_into_sequences(fileName):
    """
    Will read from fasta file and fill sequences
    """
    seq_file = open(fileName, 'r')
    raw_data = seq_file.readlines()
    current_seq = []

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
    print(trait_length)
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
    clf = svm.SVC(gamma=0.001, C=100.)
    clf.fit(trait_sets[:-1], targets[:-1])  
    return clf


def all_equal_length():
    length = len(sequences[0])
    for seq in sequences:
        print(len(seq))
        if len(seq) != length:
            return False
    return True

def predict_sequence(j, clf):
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
    import _pickle as cPickle
    with open(fileName, 'wb') as fid:
        cPickle.dump(clf, fid)
            
def loadCLF(fileName):
    import _pickle as cPickle
    with open(fileName, 'rb') as fid:
        ret = cPickle.load(fid)
    return ret

def seqToFile(seq, f):
    for number in seq:
        base = '-'
        if number == 1:
            base = 'A'
        elif number == 2:
            base = 'T'
        elif number == 3:
            base = 'C'
        elif number == 4:
            base = 'G'
        f.write(base)
    f.close()

def fastaFileLength(f):
    count = 0
    for line in f.readlines():
        if line[0] == '>':
            count = count + 1
    return count

def fastaFileMaxSeqLength(f):
    maxLength = 0
    current_seq = ""

    for line in f.readlines():
        if line[0] != '>':
            current_seq = current_seq + line
        else:
            if len(current_seq) > maxLength:
                maxLength = len(current_seq)
            current_seq = ""

    return maxLength
            
trait_length = 170
sets_desired = 20
standard_length = 4000

skippable = [['2015','Alabama']]

def main():
    """
    Code goes here
    """
    global trait_sets
    global targets

    years = ['2015', '2016', '2017']
    for year in years:
        for state in states:
            block = [year, state]
            if block in skippable:
                continue

            global trait_length
            global standard_length

            inputFileName = year + "_"
            inputFileName = inputFileName + state + "_H3N2_Strains.fasta"
            
            f = open(inputFileName, "r")
            lengthOfFile = fastaFileLength(f)
            trait_length = lengthOfFile/2
            if trait_length > 170:
                trait_length = 170

            f = open(inputFileName, "r")
            standard_length = fastaFileMaxSeqLength(f)
            print(standard_length)

            trait_sets = []
            targets = []

            f = open(inputFileName, "r")
            outputFileName = year + "_" + state + "_result.txt"

            if os.path.isfile(outputFileName):
                if os.stat(outputFileName).st_size != 0:
                    print(outputFileName + " skipped")
                    continue

            try:
                outputFile = open(outputFileName, "w")
                load_data_into_sequences(inputFileName)
                print("Done loading \"" + inputFileName + "\"" )
                load_sequences_into_traits()
                print("Done loading into traits")
                clf = train_program()
                print("Done training")
                seqToFile(predict_sequence(1,clf), outputFile)
                print("Done writing to \"" + outputFileName + "\"")                
            except Exception as inst:
                print("Error: " + str(inst))

main()

