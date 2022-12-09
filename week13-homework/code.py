#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

#part one writing my function 
def wright_fisher(pop_size ,af):
    af_list = []
    fixed = False
    while fixed == False:
        output = np.random.binomial(pop_size, af)
        af = output/pop_size 
        af_list.append(af)
        if af == 1 or af == 0: 
            fixed = True
    return(af_list)

results = wright_fisher(1000, 0.2)  
# print(results)

#part two plotting a function 
def plot(results):
    generation = np.arange(len(results))
    fig, ax = plt.subplots()
    ax.plot(generation, results)
    plt.xlabel("generation")
    plt.ylabel("allele frequency")
    plt.savefig("lineplot.png")
    # plt.show()

my_plot = plot(results)

#part three 
num_gens = []
for iteration in range(1000):
    output = wright_fisher(100, 0.5)
    gens_to_fix = len(output)
    num_gens.append(gens_to_fix)
print(num_gens)

fig, ax = plt.subplots()
ax.hist(num_gens)
plt.xlabel("number generation")
plt.ylabel("number of simulations")
plt.savefig("histogram.png")
# plt.show()

#part four
sizes = [100,1000,10000, 100000, 1000000, 10000000]
all_num_gens = []
for i in sizes:
    output = wright_fisher(i, 0.5)
    gens_to_fix = len(output)
    all_num_gens.append(gens_to_fix)
# print(all_num_gens)

fig, ax = plt.subplots()
ax.plot(sizes, all_num_gens)
plt.xlabel("population sizes")
#log scale the x axis
plt.xscale("log")
# ax.set_xticks(range(len(sizes)))
# ax.set_xticklabels(sizes)
plt.savefig("ex4_lineplot.png")
# plt.show()

# part five
allele_freq = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
second_num_gens = []
for i in allele_freq:
    num_gens = []
    for iteration in range(100):
        output = wright_fisher(100, i)
        gens_to_fix = len(output)
        num_gens.append(gens_to_fix)
    second_num_gens.append(num_gens)
print(second_num_gens)

fig, ax = plt.subplots()
ax.boxplot(second_num_gens, labels = allele_freq)
plt.xlabel("allele frequencies")
#log scale the x axis
plt.savefig("boxplot_allele_freq.png")