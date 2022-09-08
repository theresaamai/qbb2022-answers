#!/usr/bin/env python

#import bed parser function 
import untitled
import statistics

#load in bed file
bed = untitled.parse_bed("hg38_gencodev41_chr21.bed")
print(bed)

#Find the median number of exons for genes in the BED file you copied under the instructions
#0. intialize list of exon numbers 
number_of_exons = []
#1. loop through every item in bed (which is a list)
for i in range(len(bed)):
    number_of_exons.append(bed[i][9]) #2.pull out column 10 from that item (column 10 = count of exons within gene)
#3. add the exon count to a list that stores the number of exons per gene
#4. when done with for loop, our list will be filled with exon numbers 
number_of_exons.sort()
#5. sort the list 
#6. find the middle value of the list 
    #option a. use 'median' function from statistics package conda install statistics, import statistics 
    #option b. mylist[len(mylist) / 2]
print(statistics.median(number_of_exons))
