
from Bio import SeqIO # parser for FASTA file format.
from Bio.SeqRecord import SeqRecord # to create a seq record from python lists.
from Bio.Seq import Seq #for generating seq records.
import time
import os   # for cmd stuff..
import sys  # for cmd args.

# Input- file directory for superfamily 1,2,3,4,5.
# Returns - list of sequences.
def my_parse(sfam_dir):
    # Stores the total number of records in the particular file.
    total = 0
    # Get the seq record.
    seqs = [repr(seq_record.seq) for seq_record in SeqIO.parse(sfam_dir, "fasta")]
    # print("type(seqs): ",type(seqs))
    # Vectorized print loop.
    #print("seqs \n",seqs[0],"\n")
    # Gets the rec id.
    identifiers = [seq_record.id for seq_record in SeqIO.parse(sfam_dir, "fasta")]
    #print("identifiers[0]",identifiers[0])
    # Get len of the record.
    rec_lens = [len(seq_record) for seq_record in SeqIO.parse(sfam_dir, "fasta")]
    return seqs, identifiers, rec_lens

#Input should be the parsed sequences.
def cross_val(seqs,identifiers,rec_lens):

    # Hard coded for now change later... leaves the 1st sequence out.
    train_seqs = seqs[1:]
    train_identifiers = identifiers[1:]
    train_rec_lens = rec_lens[1:]

    # Make the record seq list. Holds records containing id and seq.
    train_record_seqs = []

    # For each sequence in the train set.
    for i , tr_seq in enumerate(train_seqs):
        # SeqRecord() helps to create a rec in fasta format.
        train_records = SeqRecord(Seq(train_seqs[i]),
                            id=train_identifiers[i])
        # Append records created in the list.
        train_record_seqs.append(train_records)
    # Writes to a file in fasta format.
    SeqIO.write(train_record_seqs, "train.faa", "fasta") # Take this file name as args later...

    # The 1st seq is the test set.Change later hardcoded for now.
    test_seqs = seqs[0]
    test_identifiers = identifiers[0]
    test_rec_lens = rec_lens[0]
    #print("TEST : \n",test_seqs[:],"\n")
    test_record_seqs = []
    test_records = SeqRecord(Seq(test_seqs[0]),
                            id=test_identifiers[0])
    test_record_seqs.append(test_records)
    SeqIO.write(test_record_seqs, "test.faa", "fasta")

def main():
    # Get all the dirs for the CATH data file. Hard coded for now get it as cmd args.
    # Total number of sequences = 111976.
    superfamily1_dir = sys.argv[1] #"/Users/shehjarsadhu/Desktop/Spring19/CSC522Bioinformatics/CATH/latest-releases/sequence-data/cath-domain-seqs-S100-v4_2_0.fa"

    # Will need later......
    #superfamily2_dir = sys.argv[2] "/Users/shehjarsadhu/Desktop/Spring19/CSC522Bioinformatics/CATH/latest-releases/sequence-data/cath-domain-seqs-S35.fa"
    #superfamily3_dir = "/Users/shehjarsadhu/Desktop/Spring19/CSC522Bioinformatics/CATH/latest-releases/sequence-data/cath-domain-seqs-S60.fa"
    #superfamily4_dir = "/Users/shehjarsadhu/Desktop/Spring19/CSC522Bioinformatics/CATH/latest-releases/sequence-data/cath-domain-seqs-S95.fa"
    #superfamily5_dir = "/Users/shehjarsadhu/Desktop/Spring19/CSC522Bioinformatics/CATH/latest-releases/sequence-data/cath-domain-seqs.fa"

    seqs, identifiers, rec_lens = my_parse(superfamily1_dir)
    cross_val(seqs, identifiers, rec_lens)

if __name__ == '__main__':
    start = time. time()
    main()
    end = time. time()
    print("Total time it took by the program: ",end - start)
