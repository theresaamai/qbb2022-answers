#we want to create a dictionary to store the dbSNP info
#then look up random_snippet in the dbSNP dictionary using their chromosome and position
#we want to match each SNP too a dbSNP ID

#!/usr/bin/env/ python3
import vcfParser #import the package

kgp = vcfParser.parse_vcf('random_snippet.vcf') #to use the parse_vcf function on our random snippet file that we have now stored into kgp
dbSNP = vcfParser.parse_vcf('dbSNP_snippet.vcf') #to use the parse_vcf function on our dbSNP file that is now stored into dbSNP

dbSNP_dict = {} #to create a dictionary
#add information in the dictionary 
#for every SNP in our dbSNP list,
#we want to add that SNP to the dictionary 
#dictionary entry: {key : value}
#for every dictionary entry, key is chromosome+pos, and value is ID 
#keyI: (chrom, pos) -> ("chr21", "901999392")
# ("chr21", "901999392" : 'rs2837299')
no_id_counter = 0
for snp in dbSNP: #loop through the lines in our dbSNP file to add to our dictionary 
    chrom = snp[0]
    pos = snp[1]
    newkey = (chrom, pos)
    newvalue = snp[2]
    dbSNP_dict[newkey] = newvalue
    
#look up random_snippet SNPs in the dbSNP dictionary using their chromosome and position, we wat to match each SNP to a dbSNP ID 

for snp in kgp:
    #get the SNP's chromosome and position
    #look for SNP in dbsnp_dict
    #if SNP is in dictionary, get its ID
    #report the number random_snippet SNPs that dont have an ID 
    chrom = snp[0]
    pos = snp[1]
    query_key = (chrom, pos)
    if query_key in dbSNP_dict: 
        id_of_interest = dbSNP_dict[query_key]
    else: 
        no_id_counter += 1 #increment a counter variable that stores how many SNPs dont have an id 
print(no_id_counter)     
    #is our key in the dictionary, if its in the dictionary, we can extract the associated value 
    #look for SNP in dbsnp_dict, we're going to have to create a qquery key that looks like 
    
    


 