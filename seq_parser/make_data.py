
import os # For handeling shell commands.
import sys # For args.

# DEPENDENCIES.
from Bio import SeqIO # Parser for FASTA file format.
from Bio.SeqRecord import SeqRecord # To create a seq record from python lists.
from Bio.Seq import Seq # For generating seq records.

# Input - file directory for superfamily 1,2,3,4,5.
# Returns - list of sequences in that super family file.
def my_parse(sfam_dir):
    
    # Get the actual seq record. Eg:- VLSEALTPVLAASLRANRATTERDVNQLTPRERDILKLIAQGLPNKMIARRLDITESTVKVHVKHMLKKMKLKSRVEAAVWVHQERI.
    seqs = [repr(seq_record.seq) for seq_record in SeqIO.parse(sfam_dir, "fasta")]

    # print("type(seqs): ",type(seqs)).
    # Vectorized print loop.
    # print("seqs are: \n",seqs[:],"\n")
    
    # Gets the record ids within the file. Eg:- >cath|current|1a04A02/129-215.
    identifiers = [seq_record.id for seq_record in SeqIO.parse(sfam_dir, "fasta")]
    
    # print("identifiers[0]",identifiers[0])
    # Gets length of the record.
    rec_lens = [len(seq_record) for seq_record in SeqIO.parse(sfam_dir, "fasta")]
    return seqs, identifiers, rec_lens

# Input should be the parsed sequences,id's,len's returned by the my_parser function.
# Splits the sequence file into train and test files.
def cross_val(seqs,identifiers,rec_lens,mkd_path):
    # print("seqs: \n",seqs)
    # Hard coded for now change later... leaves the 1st sequence out.
    # TO DO :- Randomly shufful the data.
    # Holds all the folders aka seq sf in the traing data directory.
    files = [f for f in os.listdir(mkd_path)]
    for folder_names in files:
        #print("List compression: ",folder_names)
        train_seqs = seqs[1:]
        #print("train_seqs: \n",train_seqs)
        train_identifiers = identifiers[1:] 
        #train_rec_lens = rec_lens[1:]

        # Make the record seq list. Holds records containing id and seq.
        train_record_seqs = []
        print("folder_names: \n",folder_names)
        # For each sequence in the train set.
        for i , tr_seq in enumerate(train_seqs):
            print(i)
            print("tr_seq: \n",tr_seq)
            #print("str(tr_seq): \n",str(tr_seq))
            #print("train_seqs: ",tr_seq)
            # SeqRecord() helps to create a rec in fasta format.
            train_records = SeqRecord(Seq(str(train_seqs[i])),
                                id=train_identifiers[i])
            # Append records created in the list.
            train_record_seqs.append(train_records)

            str_train_records = str(train_records)
            #print("train_records: \n",str_train_records)
            train_records_seq = str_train_records.replace("Seq('","")
            print("train_records_seq \n",train_records_seq)
            train_records_seq_final = train_records_seq.replace("())","")
            print("train_records_seq_final: ",train_records_seq_final)
            
   
        # TO DO:- Create this file in the foler provided as args within it's respective super family.
        # Eg:-"/Users/shehjarsadhu/Desktop/Summer19/HomologyDetectionResearch/Research-Proteins/seq_parser/test1/1.10.10.10/train.fa"
        train = mkd_path + "/" + folder_names + "/"+ "train.fa"
        # Writes to a file in fasta format.
        SeqIO.write(train_record_seqs,train , "fasta") # Take this file name as args later...

        # The 1st seq is the test set.Change later hardcoded for now.
        test_seqs = seqs[0]
        test_identifiers = identifiers[0]
        
        # test_rec_lens = rec_lens[0]

        # print("TEST : \n",test_seqs[:],"\n")
        test_record_seqs = []
        test_records = SeqRecord(Seq(test_seqs[0]),
                                id=test_identifiers[0])
        test_record_seqs.append(test_records)
        
        # TO DO :- Create this file in the foler provided as args within it's respective super family.
        test = mkd_path + "/" + folder_names + "/"+ "test.fa"
        SeqIO.write(test_record_seqs, test , "fasta")

# Processes the file name Eg:- cath-superfamily-seqs-1.10.10.10.fa and splits the file into 4 sub parts [cath , superfamily, seqs, 1.10.10.10].
# Then takes the super family id 1.10.10.10 and creates a folder with the named  1.10.10.10.
def process_fname(data_path,mkd_path):
    
    # For all files in the main datadirectory.
    for f in os.listdir(data_path):
        
        # Split the filename and extention. This creates a tuple if filename and it's extention.
        # Eg:- (cath-superfamily-seqs-1.10.10.10 , fa)
        f_name, file_ext = os.path.splitext(f)
        # Split the file name with a "-". Will split into ['cath', 'superfamily', 'seqs', '1.10.10.10'].
        new_fname_list = f_name.split("-")
        # DEBUG....
        # print("new_fname_list \n",new_fname_list)

        # Stores CATH ID seperately. Always the last element(Index - 3 element 4) in the new_fname_list.
        cathId  = str(new_fname_list[3:4])
        #print("cathId: \n",cathId) 
        
        # Proceess ['1.10.10.10'] and makes the final catch id 1.10.10.10 .
        cathIdComma = cathId.replace("'","")
        # DEBUG....
        # print("cathId: \n",cathId.replace("'",""))
        cathIdCommaBracket1 = cathIdComma.replace("[","")
        cathId_final = cathIdCommaBracket1.replace("]","")
        print("cathId_final: \n",cathId_final)
        #print("CATHid_list: ",CATHid_list)
        # If the cathId is not empty only then create the files. Did this because of  ['.DS_Store'].
        if cathId_final:
            # DEBUG...
            #print("cathId_final inside if: \n",cathId_final) 
            # print("cathId: ",cathId)
            
            # Make a new directory for holding new data. If cannont create directory thro os error.
            try:
                os.makedirs(mkd_path)
            except OSError:  
                print ("Creation of the directory %s failed" % mkd_path)
            else:
                print ("Successfully created the directory %s" % mkd_path)

            # Then create a file path for all the files within that folder AKA Superfamily train test split data..................????
            pathToData = mkd_path + "/" + cathId_final
            print(pathToData)
            os.mkdir(pathToData)
            
            #cathId_final_list = [cathId_finals for cathId_finals in cathId_final]
            #print(cathId_final_list,"cathId_final_list")
    #CATHid_list = [cathId_final]
    #print("CATHid_list: \n",CATHid_list)

def get_sequences(data_path,mkd_path):

    #Gets the filenmaes of all the sueprfamily files.
    fnames = [filename for filename in os.listdir(data_path)]

    #removes the unnessary .DS_Store file from that list.
    fnames.remove(".DS_Store")
    #DEBUG ...
     #print("fnames",fnames)
    # for every single file nmae in the superfamily file list.
    for i in fnames:
        # Creates a new file path which contains the full file path to the superfamily file/
        n_fnames = data_path+ "/" + i
        #DEBUG...
        #print("n_fnames",n_fnames)
        # Calls my_parse function which parses the .fa file format to get the sequences and their id's.
        seqs, identifiers, rec_lens = my_parse(n_fnames)
        # Calls the cross-val function which splits the data into train and test files for all the filenames found in the data directory.
        cross_val(seqs, identifiers, rec_lens,mkd_path)

def main():
    # Holds Data files.
    data_path = sys.argv[1]
    # Holds newly generated datafiles with train test splits and CATH id's.
    mkd_path = sys.argv[2]
    
    print("data_path: ",data_path)
    print("mkd_path: ",mkd_path)
    process_fname(data_path,mkd_path)
    #print("File names returned by process_fname(): ",cathId_final)
    get_sequences(data_path,mkd_path)


if __name__ == '__main__':
    
    #   print ('Number of arguments:', len(sys.argv), 'arguments.') 
    #  print ('Argument List:', str(sys.argv))
    main()
