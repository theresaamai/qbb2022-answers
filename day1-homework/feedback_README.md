Question 1: It looks like the fix you did (adding -v to awk) worked! There was one more fix that you should have had to make, which was removing the $ from the for $nuc in A C G T, but given that you have the right output, I'm guessing you did. Just remember to comment all of your changes.

Question 2: Definitely not obvious what defines a promoter. State 1 definitely makes sense, but one could also argue that states 2,3,10,11,12 are also potentially indicators of promoters (nothing you have to fix here, just making a comment)

Question 3: Looks good! One minor comment re: your explanation of the awk command: You said that command "ignores the headers, and prints out columns 1, tells us the size of the chromosome based on the positions stated from $2-1 and makes it as a new variable which will now be stored in variants.bed". It definitely ignores the header, but then it prints `column 1, column 2 minus 1, then column 2`, then stores that to the output. What are column 1 and column2 in the input? Given that, what's the format of the output? Otherwise, your analysis and your fixes are spot on.

Great work!
