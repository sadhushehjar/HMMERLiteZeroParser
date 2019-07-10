
import os # For handeling shell commands.
import sys # For args.

# DEPENDENCIES.
from Bio import SeqIO # Parser for FASTA file format.
from Bio.SeqRecord import SeqRecord # To create a seq record from python lists.
from Bio.Seq import Seq # For generating seq records.

# Input - file directory path for superfamily 1,2,3,4,5.
# Returns - list of sequences in that super family file.
def my_parse(sfam_dir):

    # Get the actual seq record. Eg:- VLSEALTPVLAASLRANRATTERDVNQLTPRERDILKLIAQGLPNKMIARRLDITESTVKVHVKHMLKKMKLKSRVEAAVWVHQERI.
    seqs = [str(seq_record.seq) for seq_record in SeqIO.parse(sfam_dir, "fasta")]
    # print("type(seqs): ",type(seqs)). 
    # Vectorized print loop.
    # print("seqs are: \n",seqs[:],"\n")
    
    # Gets the record ids within the file. Eg:- >cath|current|1a04A02/129-215.
    identifiers = [seq_record.id for seq_record in SeqIO.parse(sfam_dir, "fasta")]
    
    # print("identifiers[0]",identifiers[0])
    # Gets length of the record.
    rec_lens = [len(seq_record) for seq_record in SeqIO.parse(sfam_dir, "fasta")]
    
    #print("seqs are: \n",seqs,"\n")
    return seqs, identifiers, rec_lens

# Input should be the parsed sequences,id's,len's returned by the my_parser function.
# Splits the sequence file into train and test files.
def cross_val(seqs,identifiers,rec_lens,mkd_path,data_path,cath_list_id):

    print("in Cross validates: \n")
    print(cath_list_id)
    #print("seqs: \n",seqs)
   # for idx, f in enumerate(os.listdir(data_path)):
    #print("seqs out: == ",seqs)
    #print("seqs[0]: ==",seqs[0])
    
    # The 1st seq is the test set.Change later hardcoded for now.
    print("seqs!!!!",seqs)
    test_seqs = seqs[0]
    #print("test_seqs: = ",test_seqs)
    test_identifiers = identifiers[0]
    #print(test_identifiers,"\n",test_seqs)
    test_record_seqs = []
    
    test_records = SeqRecord(Seq(test_seqs),
                                id=test_identifiers)
    test_record_seqs.append(test_records)
    test_records_list = []
    print(test_records)
    test_file_paths = []
   
   # print("mkd_path: = ",mkd_path)
   # print("test_records_list:=",test_records_list)
   # print("test_file_paths",test_file_paths)

  #  print(test_record_seqs)
   # for idx ,paths in enumerate(test_file_paths):
    #    SeqIO.write(test_record_seqs[idx], paths , "fasta")


           
# Processes the file name Eg:- cath-superfamily-seqs-1.10.10.10.fa and splits the file into 4 sub parts [cath , superfamily, seqs, 1.10.10.10].
# Then takes the super family id 1.10.10.10 and creates a folder with the named  1.10.10.10.
def process_fname(data_path,mkd_path):
    cath_list_id = []
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
        
        # Proceess ['1.10.10.10'] and makes the final catch id 1.10.10.10.
        cathIdComma = cathId.replace("'","")
        # DEBUG....
        # print("cathId: \n",cathId.replace("'",""))
        cathIdCommaBracket1 = cathIdComma.replace("[","")
        cathId_final = cathIdCommaBracket1.replace("]","")
        #print("cathId_final: \n",cathId_final)
        cath_list_id.append(cathId_final)
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
    cath_list_id.remove('')
    return cath_list_id

def get_sequences(data_path,mkd_path,cath_list_id):

    #Gets the filenmaes of all the sueprfamily files.
    fnames = [filename for filename in os.listdir(data_path)]
    #removes the unnessary .DS_Store file from that list.
    fnames.remove(".DS_Store")
    #print("fnames[:] -- ",fnames[:])
    #DEBUG ...
     #print("fnames",fnames)
    # for every single file nmae in the superfamily file list.
    for idx, i in enumerate(fnames):
        #print("i = ",i)
    #     # Creates a new file path which contains the full file path to the superfamily file/
        n_fnames = data_path+ "/" + i
        
    #     #DEBUG...
        #print("n_fnames",n_fnames)
        
    #     # Calls my_parse function which parses the .fa file format to get the sequences and their id's.
        seqs, identifiers, rec_lens = my_parse(n_fnames)
        #print("seqs in super family",i, "are : = ",seqs[idx:])
        #test_path = mkd_path + "/" + cathId_final + "/" + "test.fa"
        #print("test_path ==",test_path)
    #     # Calls the cross-val function which splits the data into train and test files for all the filenames found in the data directory.
        cross_val(seqs[idx:], seqs[idx:], seqs[idx:],mkd_path,data_path,cath_list_id)
        
    #     #print("File names returned by process_fname(): ",cathId_final)
        #get_sequences(data_path,mkd_path)

def main():
    # Holds Data files.
    data_path = sys.argv[1]
    # Holds newly generated datafiles with train test splits and CATH id's.
    mkd_path = sys.argv[2]
    #DEBUG...
    print("data_path: ",data_path)
    print("mkd_path: ",mkd_path)
    cath_list_id = process_fname(data_path,mkd_path)
    get_sequences(data_path,mkd_path,cath_list_id)
if __name__ == '__main__':
    
    print ('Number of arguments:', len(sys.argv), 'arguments.') 
    #print ('Argument List:', str(sys.argv))
    main()
