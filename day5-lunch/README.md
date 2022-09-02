#QBB2022 - Day 5 Lunch Exercise Submission
Exercise 1. 
cut - d "," -f 5-6 aau1043_dnm.csv | sort | uniq -c  > all_dnm #here i am cutting out the probID, then sorting them by mother and father, then putting the counts of the de novo mutations by mother and father, which i named all_dnm 

grep mother all_dnm > mother_dnm_uncut #from my all_dnm file, I searched for mother which now gives me all the ones for mother 

cut -d "," -f 1 mother_dnm_uncut >mother_dnm_cut #here i am now cutting it so I can just get the proband ID's with the counts of de novo mutations 

grep father all_dnm > father_dnm_uncut #doing the same as above but now for father

cut -d "," -f 1 father_dnm_uncut > father_dnm_cut #doing the same as above but now for father

join -1 2 -2 2 mother_dnm_cut father_dnm_cut > father_mother_joined #now i am joining the two mother and father files together 

cat aau1043_parental_age.csv | tr ',' ' ' > commaremoved_parental_age #i am now replacing commas with a space so that i can join the parental age file with the dnm file 

sort commaremoved_parental_age >sorted_parentalage_ #now i need to sort the files so that the proband IDs match so that i can join them together 

join father_mother_joined sorted_parentalage > joined_final #now i am FINALLY joining the age and de novo mutation files together 