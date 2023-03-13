import pandas as pd
import matplotlib.pyplot as plt

df =  pd.read_csv('assets/CFPB Housing Data.csv')

CENSUS = df['Census Tract']
LOAN = df['Loan Amount']

plt.scatter(CENSUS, LOAN)

plt.xlabel("Census Tract")
plt.ylabel("Loan Amount")

plt.show()
#print(df.head)
