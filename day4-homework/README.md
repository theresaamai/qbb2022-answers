#QBB2022- Day 4 Homework Exercise Submission
Exercise A 
We use numpy.arange to make an array of evenly spaced values. Based on the manual page, 0.55 and 1.05 are the start and end numbers of the array, and 0.05 is the step between these numbers.  We observe an array that starts at 0.55 and ends at 1 with every number between that at a step of 0.05. 

In our exercise the purpose of numpy.around() is to specify the number of decimals we are using, where we are staring at 0.55, ending at 1.05, using 0.05 as a step between these numbers. 
Based on the manual page, the numpy around function is used to evenly round to the given number of decimals. Since we input decimals =2, in this exercise we are rounding all the numbers to 2 decimal places. When we do this, the numbers in our array are still all 2 decimal places, but we want to do this so that when people reproduce our code, they will get the same numbers everytime. 

[:: -1] This reverses the string that is input to the array. Now the order of our array is in the reverse order. 

Exercise B
power_mat = numpy.zeros([len(prob_heads),len(n_toss)])
for i, p in enumerate(prob_heads):
    for j, n in enumerate(n_toss):
        #simulate_coin_toss(n, p)
        # CALCULATE THE POWER ON THIS LINE
        power = run_experiment(p, n)
        power_mat[i,j] = power
        #pvals.append(perform_hypothesis_test(n_success, n_toss))
print(power_mat)

Exercise C
Power increases with probability and number of tosses. 
 
Exercise D
The study wants to know if certain alleles are inherited more than other alleles if you expected them to be inherited seperately. 

In our study, we wanted to know if we increase the probability of getting heads and increase the number of tosses, what is the effect? In the published study, they wanted to know if they increase the number of sperm with transmission rate, what is the effect? 

Differences: the x-axis is in log-scale, so although they have the same trend, this shows us the impact of correcting multiple tests. Also the published study repeated the simulation 1000x. 

Prob_heads from our simulation corresponds to the transmission rate axis.
n_tosses from our simulation corresponds to the number of sperm axis. 

Both simulations use a binomial test because they want to ask if the observed test result differs from what was expected. 