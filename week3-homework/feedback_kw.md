# Week 3 Variant Calling -- Feedback

1 + 1 + 1 + 0.75 + 1 + 1 + 1 + 1 + 1 + 1 = 9.75 points out of 10 possible points

1. Index genome

  * --> +1

2. align reads

  * very good! --> +1

3. sort bam files and index sorted bam files (0.5 points each)

  * nice! --> +1

4. variant call with freebayes

  * want to use the `-p` argument to specify the ploidy of the yeast (1)
  * --> +0.75

5. filter variants

  * nice use of the pipe! --> +1

6. decompose complex haplotypes

  * great! --> +1

7. variant effect prediction

  * good! --> +1

8. python plotting script

  * --> +1

9. 4 panel plot (0.25 points each panel)

  * the tick labels aren't readable for the two right subplots, and titles would be useful for all 4 subpanels to distinguish them. I see these titles in your code with `set_title`, just not on the plot
  * for the tick labels you could try to rotate them, you can also try a `plt.tight_layout()`, but it also looks like there are just too many labels there. I again see that you tried rotation in your code, just not on the plot.

10. 1000 line vcf

  * --> +1
