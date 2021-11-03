#Q 1
#Pandas is used for analyzing, cleaning, exploring, and manipulating data
#"Pandas" references "Panel Data" and "Python Data Analysis"

#Q 2
#Pandas allows us to analyze big data and make conclusions based on statistical theiroies
#Can clean messy data sets which is very important in data science

#Q 3
import pandas as pd
from pandas.io.formats.format import DataFrameFormatter
mydataset = {'cars': ['BMW', 'Volvo', 'Ford'], 'passings': [3, 7, 2]}
myvar = pd.DataFrame(mydataset)
print(myvar)
print(pd.__version__)

#Q 4
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
print(myvar[0])

#Q 4.1
myvar = pd.Series(a, index = ['x', 'y', 'z'])
print(myvar)
print(myvar['y'])

#Q 5
calories = {'day1': 420, 'day2':380, 'day3':390}
myvar = pd.Series(calories, index = ['day1', 'day2'])
print(myvar)

#Q 6
data = {'calories': [420, 380, 390], 'duration': [50, 40, 45]}
df = pd.DataFrame(data)
print(df)
print(df.loc[0])
print(df.loc[[0,1]])

#Q 7
df = pd.read_csv('data.csv')
print(df.to_string())
print(df)

print(df.head())
print(df.tail())
print(df.info())

#Q 8
df = pd.read_csv('data.csv')
new_df = df.dropna()
print(new_df.to_string())

#Q 8.1
df = pd.read_csv('data.csv')
df.fillna(130, inplace = True)

#Q 8.2
df = pd.read_csv('data.csv')
df['Calories'].fillna(130, inplace = True)

#Q 8.3
df = pd.read_csv('data.csv')
x = df['Calories'].mean()
df['Calories'].fillna(x, inplace = True)

x = df['Calories'].median()
df['Calories'].fillna(x, inplace = True)

x = df['Calories'].mode()[0]
df['Calories'].fillna(x, inplace = True)

#Q 8.4
df = pd.read_csv('data.csv')
print(df.duplicated())

#Q 9
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')
df.plot()
plt.show()