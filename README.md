# HMMERLiteZero Parser
## cath-seq-parser
### Dependencies:- 

  Biopython - https://biopython.org/

### Inputs:-

** All files are assumed to be FASTA formated.

  1. File directory path for all super families.
  2. File directory path for train set file which will be generated.

### Outputs:- --- Needs Fixing---
  ** Both files are FASTA formatted.
  
  1. train.fa - file contains set of sequences to train on.
  2. test.fa - file contains set of sequence to test on.
### Running the program

Example :- 

```python3 make_data.py /Users/shehjarsadhu/Desktop/Summer19/HomologyDetectionResearch/Research-Proteins/seq_parser/dummy-seq-by-sf /Users/shehjarsadhu/Desktop/Summer19/HomologyDetectionResearch/Research-Proteins/seq_parser/test1```

Here test1 directory will be created by the program where all the train/test sequences belonging to the respective super family will be stored. 

## multiple-seq-aigns-hmm

This program runs MSA tool MUSCLE  on 10 CATH sequences selected randomly and the passes the generated MSA to hmm build from HUMMER. 
