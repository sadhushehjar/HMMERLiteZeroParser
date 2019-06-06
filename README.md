# HMMERLiteZero Parser
## Program 1: cath-seq-parser (make_data.py) :-
### Dependencies:- 

  Biopython - https://biopython.org/
  
  You can download the Biopython framework here.
  [Download page](http://biopython.org/DIST/docs/install/Installation.pdf)


### Inputs:-

** All files are assumed to be FASTA formated.

  1. File directory path for all super families:- Eg :-
  ``` /Users/shehjarsadhu/Desktop/Summer19/HomologyDetectionResearch/Research-Proteins/seq_parser/dummy-seq-by-sf```
  2. File directory path for train set file which will be generated.:- Eg:-
``` /Users/shehjarsadhu/Desktop/Summer19/HomologyDetectionResearch/Research-Proteins/seq_parser/test1```

### Outputs:- --- Needs Fixing---
  ** Both files are FASTA formatted.
  
  1. train.fa - file contains set of sequences to train on.
  2. test.fa - file contains set of sequence to test on.
### Running the program

Example :- 

``` python
python3 make_data.py /Users/shehjarsadhu/Desktop/Summer19/HomologyDetectionResearch/Research-Proteins/seq_parser/dummy-seq-by-sf /Users/shehjarsadhu/Desktop/Summer19/HomologyDetectionResearch/Research-Proteins/seq_parser/test1 
```

Here test1 directory will be created by the program where all the train/test sequences belonging to the respective super family will be stored. 

## Program 2: multiple-seq-aigns-hmm (msa.py):-

This program runs MSA tool MUSCLE   [MUSCLE user guide](http://www.drive5.com/muscle/muscle_userguide3.8.pdf) on 10 [CATH](http://www.cathdb.info/) sequences selected randomly and the passes the generated MSA to hmm build from 
HMMER. [HMMER user guide](http://eddylab.org/software/hmmer3/3.1b2/Userguide.pdf) 

### Running the program

There are three inuputs to this program

1. Folder path to dataset on which MSA will be performed :- Eg:- ```/Users/shehjarsadhu/Desktop/Summer19/HomologyDetectionResearch/Research-Proteins/multiple-seq-aigns/msa-data```
2. Folder path to where you want to store the Aligned sequences :- Eg:-
```/Users/shehjarsadhu/Desktop/Summer19/HomologyDetectionResearch/Research-Proteins/multiple-seq-aigns/test_msa```
3.Folder path to where the ```hmm build``` command will output the files :- Eg:-
```/Users/shehjarsadhu/Desktop/Summer19/HomologyDetectionResearch/Research-Proteins/multiple-seq-aigns/hmmbuild-files```


```python
python3 msa.py /Users/shehjarsadhu/Desktop/Summer19/HomologyDetectionResearch/Research-Proteins/multiple-seq-aigns/msa-data /Users/shehjarsadhu/Desktop/Summer19/HomologyDetectionResearch/Research-Proteins/multiple-seq-aigns/test_msa /Users/shehjarsadhu/Desktop/Summer19/HomologyDetectionResearch/Research-Proteins/multiple-seq-aigns/hmmbuild-files
```

## List of guides:-

1. [HMMER user guide](http://eddylab.org/software/hmmer3/3.1b2/Userguide.pdf)
2. [Biopython](http://biopython.org/DIST/docs/tutorial/Tutorial.pdf)
3. [MUSCLE user guide](http://www.drive5.com/muscle/muscle_userguide3.8.pdf)
