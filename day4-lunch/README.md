#QBB2022- Day 4 - Lunch Exercises Submission
Exercise 1:
exons.chr21.bed.vcf
    + Covering 1107407 bp
processed_pseudogene.chr21.bed.vcf
    + Covering 956640 bp
protein_coding.chr21.bed.vcf
    + Covering 13780687 bp

This code gives us the same plot. 
strategy #1: visually open the plot and compare 
strategy #2: compare the text files using a module called filecmp
strategy #3: compare the text files using the command diff 

gene_type: miRNA, lncRNA, protein coding. It is interesting that we are able to look at the various types of genes. I thought it was interesting that there are miRNA's because the field of miRNA is still evolving to understand the function of miRNA's and how they regulate gene expression. It's also interesting that this file identified lncRNA's and these are interesting because they are known to be involved in regulating gene expression through epigenetic and chromatin remodeling mechanisms. I also thought it was great that protein coding genes were identified! 

Exercise #2: 
To make the plot logscale, use plt.yscale('log')
To make subplots share the same y axis, use fig, ax = plt.subplots(2, 1, sharey=True)
To make the plot have a title, use plt.title('My title')

To create the lncRNA.chr21.bed.vcf.png plot - I needed to go into subset_regions.sh and change the code to search for lncRNA. Rerun the do_all.sh script, which will now give me the lncRNA.chr21.bed.vcf file, and I can now plot it with the plot_vcf_ac.py 

The trend that we see makes sense, very few individuals have a high frequency of allele changes, and this decreases as there are more individuals. 

Exercise #3:
 SYNOPSIS
     bxlab/cmdb-plot-vcfs -- ... the do_all.sh script takes specific information from bed and vcf files , puts it together, sorts this information, and plots it for you. 

 USAGE
     bash do_all.sh <bed file> <vcf file> ...

     <bed file>  create a bed file for features of interest
	 <vcf file > subset .vcf for each feature

 DEPENDENCIES 
 In order for us to use this code, we need to import mathplotlib.pyplot for us to install the python package that will allow us to make the plots. 
 
 DESCRIPTION
     1. Create .bed files for features of interest
         - Run subset_regions.sh Bash script
         - Use grep to search for the region of interest (for ex. we can grep to search for gene types, such as lncRNA, protein coding, etc.)
 OUTPUT 
 A new vcf file that combines specific information input by the user from the bed file, to the given vcf file. 