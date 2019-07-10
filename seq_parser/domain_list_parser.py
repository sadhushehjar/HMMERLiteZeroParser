
import os # For handeling shell commands.
import sys # For args.
import json

import numpy as np
import pandas as pd

from new_make_data import process_fname

def read_file():
        df = pd.read_csv("/Users/shehjarsadhu/Desktop/cath-domain-list.txt",sep='\s+',header = None,engine='python')
        print(df.head())
        print(df.shape)  #(434857, 12).
        numpy_df = df.values
        print(numpy_df)
        return numpy_df

def my_domainList_parser(numpy_df):
    # Domain name cath id list.
    cathid_list_dn = []
    # cathid_list_dn = a = np.zeros((434857, 4)) #np.array([])
    # Get all the cath ids in the dataframed object.
    for idx,i in enumerate(numpy_df[:]):
        #for each row steals the cath is which are in columns 1-4.
        cathid_db = numpy_df[idx,1:5]
        #print(cathid_db)
     #   print(np.array2string(cathid_db))
        cathid_list_dn.append(cathid_db)
        #cathid_list_dn =  np.append([cathid_db])
   # print(cathid_list_dn)
    return cathid_list_dn

def write_to_json(cathid_list_dn):
        
        data_path = "/Users/shehjarsadhu/Desktop/seq-by-superfamily"
        mkd_path = "/Users/shehjarsadhu/Desktop/Summer19/HomologyDetectionResearch/Research-Proteins/seq_parser/test1"
        
        cath_list_id = process_fname(data_path,mkd_path)
        domain_list = np.array(cathid_list_dn,dtype=int)
        
        print("domain_list = ",domain_list[:])

        domain_list_unique,indices,counts = np.unique(domain_list,axis=0,return_inverse=True,return_counts=True)
        for i in domain_list_unique:
                print("i type == ",type(i))
                for j in cathid_list_dn:
                        print(i)
                        print(j)
                        print("j type == ",type(j))
                        if (i==j).all():
                                print("Hello")
                print("i == ",i)
        print("Length == ",len(counts))
        for i in counts:
                print("counts == ",i)
                for j in range(i):
                        idx = []
                        print("j == ",j)
                        idx.append(j)
        print("domain_list_unique = ",domain_list_unique[:])
        datastore = {}
        datastore["sf-S35"] = {}
        datastore["sf-S60"] = {}
        datastore["sf-S95"] = {}
        datastore["sf-S100"] = {}
        for i in cath_list_id:
                datastore["sf-S35"][i] = [1,2,3]
        filename = "/Users/shehjarsadhu/Desktop/Summer19/HomologyDetectionResearch/Research-Proteins/seq_parser/data_db.json"
        # If the file name exists, write a JSON string into the file.
        if filename:
                # Writing JSON data
                with open(filename, 'w') as f:
                        json.dump(datastore, f,indent=4)
def main():
        numpy_df = read_file()
        cathid_list_dn = my_domainList_parser(numpy_df)
        write_to_json(cathid_list_dn)

if __name__ == '__main__':
    print ('Number of arguments:', len(sys.argv), 'arguments.') 
    #print ('Argument List:', str(sys.argv))
    main()
