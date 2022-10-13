#!/usr/bin/env python 

from bdg_loader import load_data
import matplotlib.pyplot as plt

day0 = load_data("scaledday0.bdg") 
day2 = load_data("scaledday2.bdg")
klf = load_data("scaledklf.bdg")
sox2 = load_data("scaledklf.bdg")
print(sox2)

sox_values =sox2["X"]
soxY_values = sox2["Y"]

klf_values = klf["X"]
klfY_values = klf["Y"]

day0_values = day0["X"]
day0Y_values = day0["Y"]

day2_values = day2["X"]
day2Y_values = day2["Y"]

fig, ax = plt.subplots(ncols = 1, nrows = 4)

ax[0].fill_between(sox_values, soxY_values)
ax[1].fill_between(klf_values, klfY_values)
ax[2].fill_between(day0_values, day0Y_values)
ax[3].fill_between(day2_values, day2Y_values)

fig.savefig("figure.png") 
plt.show()