#!/usr/bin/env python

import numpy
from scipy.stats import binomtest
from statsmodels.stats.multitest import multipletests
import matplotlib.pyplot as plt
import seaborn as sns; sns.set_theme()

def simulate_coin_toss(n_tosses, prob_heads = 0.5, seed=None):
    '''
    Input: n_tosses, an integer, number of coin tosses to simulate
           prob_heads, a float, the probability the coin toss will return heads; default is 0.5, meaning a fair coin
           seed, an integer, the random seed that will be used in the simulation
    Output: results_arr, an array of 1's and 0's with 1's representing heads and 0's representing tails
    Resources: https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html
    '''
    #function#1: made a function to simulate coin tosses and this returns an array of results 
    if seed is not None:
        numpy.random.seed(seed)
    results_arr = numpy.random.choice([0,1], size=n_tosses, p = [1-prob_heads, prob_heads]) 
    return (results_arr)

#print(numpy.sum(simulate_coin_toss(10, seed = 4)))

    
def perform_hypothesis_test(n_heads, n_tosses):
    binom_result = binomtest(n_heads, n_tosses)
    pval = binom_result.pvalue #grabbing the pvalue attribute from the binom_result instance
    return(pval)
    
    
#print(perform_hypothesis_test(2,5))

    #function#2: made a function to calculate p-vals
def correct_pvalues(pvals):
    corrected_pvalues = multipletests(pvals, method='bonferroni')
    return(corrected_pvalues[1])
#print(corrected_pvalues([0.005, 0.04, 0.03, 0.003, 0.00001]))

def interpret_pvalues(pvals):
    interpreted = numpy.array(pvals) < 0.05 
    return(interpreted) #an array of trues and falses
    
#print(interpret_pvalues([0.06, 0.5, 0.05, 0.03]))

def compute_power(n_rejected_correctly, n_tests):
    power = n_rejected_correctly / n_tests
    return(power)
    

def run_experiment(prob_heads, n_toss, n_iters = 100, seed = 389, correct_the_pvalues = False):
    '''
    Input: prob_heads, a float, the probability of a simulated coin toss returning heads
           n_toss, an integer, the number of coin tosses to simulate
           n_iters, an integer, the number of iterations for each simulation. default is 100
           seed, an integer, the random seed that you will set for the whole simulation experiment. default is 389
           correct_the_pvalues, a boolean, whether or not to perform multiple hypothesis testing correction
    Output: power, a float, the power of the experiment
    '''
    numpy.random.seed(seed)
    pvals = []
    for k in range(n_iters):
        results_arr = simulate_coin_toss(n_toss, prob_heads = prob_heads)
        n_success = numpy.sum(results_arr)
        pvals.append(perform_hypothesis_test(n_success, n_toss))
    if correct_the_pvalues:
        pvals = correct_pvalues(pvals)
    pvals_translated_to_bools = interpret_pvalues(pvals)
    power = compute_power(numpy.sum(pvals_translated_to_bools), n_iters)
    return(power)
prob_heads = numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1]
n_toss = numpy.array([10, 50, 100, 250, 500, 1000])
power_mat = numpy.zeros([len(prob_heads),len(n_toss)])
for i, p in enumerate(prob_heads):
    for j, n in enumerate(n_toss):
        #simulate_coin_toss(n, p)
        # CALCULATE THE POWER ON THIS LINE
        power = run_experiment(p, n)
        power_mat[i,j] = power
        #pvals.append(perform_hypothesis_test(n_success, n_toss))
print(power_mat)
# power1 = run_experiment(0.6, 500, correct_the_pvalues = True)
# power2 = run_experiment(0.95, 10, correct_the_pvalues = True)
# power2b = run_experiment(0.95, 10)

fig, ax = plt.subplots()
sns.color_palette("viridis_r", as_cmap=True)
ax = sns.heatmap(power_mat, vmin=0, vmax=1, xticklabels='auto', yticklabels='auto', ax = None)
ax.set_xlabel("n_tosses")
ax.set_ylabel("probability of heads")
ax.set_title("Heatmap to visualize Power")
fig.savefig("heatmap.png")
plt.show()
