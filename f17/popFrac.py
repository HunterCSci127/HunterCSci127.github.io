#fraction of pop

import matplotlib.pyplot as plt

import pandas as pd
pop = pd.read_csv('nycHistPop.csv', skiprows=5)

boro = input('Enter borough name: ')
outFile = input('Enter output name: ')
pop['Fraction'] = pop[boro]/pop['Total']

pop.plot(x = 'Year', y = 'Fraction')
fig = plt.gcf()
fig.savefig(outFile)


plt.show()



