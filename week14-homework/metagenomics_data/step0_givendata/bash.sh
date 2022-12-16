#!/bin/bash

#for one bin file
# getting the names of all the contigs in the bile file of interest
# contigs=$(grep ">" bins_dir/bin.6.fa | cut -f 2 -d ">")
#
# #loop through all the contigs
# for id in $contigs
# do
# 	#pull out the kraken classification for that contig ID and put it into a file for that bin
# 	grep $id ~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/assembly.kraken >> bin6.kraken
# done
#
# #convert the kraken file into kronatools format
# ~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/code.py bin6.kraken bin6

#run ktImportText on all your krona files 
ktImportText -q bin1_krona.txt bin2_krona.txt bin3_krona.txt bin4_krona.txt bin5_krona.txt bin6_krona.txt -o bins.html