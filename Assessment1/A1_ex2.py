#The CSV file holds the share price information of N companies. 
# This information is for each month of years ranging from 1990 onwards. 
# The output gives out the month with highest share value for each company.

import pandas as pd
df = pd.read_csv('Data.csv')
maxValueA = df['CompanyA'].max()
maxValueB = df['CompanyB'].max()
maxValueC = df['CompanyC'].max()
print('Max Share Price for Company A', maxValueA)
print('Max Share Price for Company B', maxValueB)
print('Max Share Price for Company C', maxValueC)

