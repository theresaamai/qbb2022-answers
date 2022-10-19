# Week 1 Genome Assembly -- Feedback

1 + 0.5 + 1 + 1 + 0.5 + 0.5 + 0.75 + 1 + 0.75 + 1 = _ points out of 10 possible points

1. Question 1.1, 1.4 how many reads (0.5 pts each)

  * good --> +1

2. Question 1.2, 1.4 simulation script(s)

  * For the 15x coverage, you should repeat the simulation, not just the plotting, increasing the number of reads for which you simulate locations. --> +0.5

3. Question 1.2, 1.4 plotting script(s)

  * good --> +1

4. Question 1.2, 1.4 histograms with overlaid Poisson distributions (0.5 pts each)

  * In the histograms, you plot the same data twice since the simulation isn't repeated. You correctly overlay different Poisson expectations. --> +1


5. Question 1.3, 1.4 how much of genome not sequenced/comparison to Poisson expectations (0.5 pts each, 0.25 for answer and 0.25 for code)

  * The second histogram isn't matching Poisson expectations for a lambda of 15 since it's plotting 5x simulation data, not 15x simulation data.
  * Can you get a number of how many genomic locations you would expect to have 0 coverage according to the Poisson distribution?
  * --> +0.5

6. Question 2 De novo assembly (0.5 pts each, 0.25 for answer and 0.25 for code)

  * number of contigs --> +0.25, how did you get this?
  * total length of contigs --> +0.25, how did you get this?

7. Question 2 De novo assembly cont (0.5 pts each, 0.25 for answer and 0.25 for code)

  * size of largest contig --> +0.25, how did you get this?
  * contig n50 size --> +0.5, your answer is correct, but should be reported as a number. Also not clear how you arrived at this answer.

8. whole genome alignment (0.33 pts each, 0.33/2 for answer and 0.33/2 for code)

  * average identity --> +0.33
  * length of longest alignment --> +0.33
  * how many insertions and deletions in assembly --> +0.33

9. decoding the insertion (0.5 pts each, 0.25 for answer and 0.25 for code)

  * position of insertion in assembly --> +0.25, how do you know this?
  * length of novel insertion --> +0.5

10. decoding the insertion cont (0.5 pts each, 0.25 for answer and 0.25 for code)

  * DNA sequence of encoded message --> +0.5
  * secret message --> +0.5
