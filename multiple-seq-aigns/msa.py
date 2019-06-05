import os # For handeling shell commands.
import sys # For args.

# DEPENDENCIES.
from Bio import SeqIO # Parser for FASTA file format.
from Bio.SeqRecord import SeqRecord # To create a seq record from python lists.
from Bio.Seq import Seq # For generating seq records.
from Bio.Align.Applications import MuscleCommandline # for MSA
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
        
        # Proceess ['1.10.10.10'] and makes the final catch id 1.10.10.10 .
        cathIdComma = cathId.replace("'","")
        # DEBUG....
        # print("cathId: \n",cathId.replace("'",""))
        cathIdCommaBracket1 = cathIdComma.replace("[","")
        cathId_final = cathIdCommaBracket1.replace("]","")
        print("cathId_final: \n",cathId_final)
        cath_list_id.append(cathId_final)
    
    cath_list_id.remove('')
    print("cath_list_id: \n",cath_list_id)
    return cath_list_id

def msa(cath_list_id,mkd_path,data_path):
    os.mkdir(mkd_path)
    file_names = []
    for f in os.listdir(data_path):
        print("file names : \n",f)
        f_name = data_path + "/" + f
        file_names.append(f_name)
    for i,ids in enumerate(cath_list_id):
        input_msa_path = file_names[i]
        print("input_msa_path: \n",input_msa_path)
        output_msa_path = mkd_path + "/"+ ids + ".fa"
        print("output_msa_path: \n",output_msa_path)
        os.system('/Users/shehjarsadhu/Desktop/muscle3.8.31_i86darwin32 -in %s -out %s' % (input_msa_path,output_msa_path) )

        #cline = MuscleCommandline(input=input_msa_path, out=output_msa_path)
def main():
    # Holds Data files.
    data_path = sys.argv[1]
    # Holds newly generated datafiles with train test splits and CATH id's.
    mkd_path = sys.argv[2]
    print("data_path: ",data_path)
    print("msa's_path: ",mkd_path)
    cath_list_id = process_fname(data_path,mkd_path)
    msa(cath_list_id,mkd_path,data_path)
if __name__ == '__main__':
    
    print ('Number of arguments:', len(sys.argv), 'arguments.') 
    print ('Argument List:', str(sys.argv))
    main()
