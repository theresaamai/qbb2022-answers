##Quantbio Week 6 Homework 

Part One 
34.77% of dCTCF reads are valid interactions. (take 92% of 37.8)
32.2% of ddCTCF reads are valid interactions. (take 88% of 36.6)
The majority of invalid 3C pairs are dangling end pairs that are unligated fragments, so these are reads mapped on the same restriction fragment (since we only see one restriction end site).

Part Two
python plotcode.py
analysis/hic_results/matrix/dCTCF/iced/6400/dCTCF_ontarget_6400_iced.matrix	
analysis/hic_results/matrix/ddCTCF/iced/6400/ddCTCF_ontarget_6400_iced.matrix
analysis/hic_results/matrix/dCTCF/raw/6400/dCTCF_ontarget_6400_abs.bed
output 

python plotcode.py
matrix/dCTCF/iced/6400/dCTCF_ontarget_6400_iced.matrix	
analysis/hic_results/matrix/ddCTCF/iced/6400/ddCTCF_ontarget_6400_iced.matrix
analysis/hic_results/matrix/dCTCF/raw/6400/dCTCF_ontarget_6400_abs.bed
output 

1. No
2. Sequencing depth does not change the interpretation of the TADs
3. The highlighted signal represents nonadjacent TADs interacting. 

Part Three
python plotcode.py matrix/dCTCF_full.6400.matrix matrix/ddCTCF_full.6400.matrix matrix/6400_bins.bed output
