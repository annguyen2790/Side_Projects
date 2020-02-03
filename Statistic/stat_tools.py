import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# the keyword 'as' creates an alias of an object, in this case the object is pandas library and numpy. Furthermore,
# alias served as shortcut in programming, reducing the amount of typing the full name of an object

df = pd.read_csv('cars.csv')
print(df.head(10)) #passed in an integer in head() method to display first 10 rows


column_list = list(df.columns)
print(column_list)
print(df[0:5])
print(df[0:5].dtypes)
#dtypes gives the types of each columns

print(df[['Car', 'MPG']][0:10])
#get the first ten rows

print(df[df['MPG'] >  40]) #get all MPG greater than 40

print(df.ix[[0,1,5], 0:5]) #last five row using index notation


#Two ways of printing 5 last rows in df
print(df.tail(5)) #From StackOverflow https://stackoverflow.com/questions/14663004/how-to-get-the-last-n-rows-of-a-pandas-dataframe
print(df[-5:])
print(df[df['Cylinders'] == 3]['Car'])


plt.figure(figsize=(6,2))


plt.plot(df['Horsepower'])

print(df[df['Origin'] == 'US'])


df1 = df[df['Origin'] == 'US']
plt.plot(df1['Horsepower'])


# Get the data frame where stores only car origin is in US. Copy it into another dataframe and plot it



fig = plt.figure(figsize=(7,3))
plt.hist(df['MPG'], bins=30)



plt.hist(df['Cylinders'], bins=8)




print(df)




t = pd.crosstab(index=df['Cylinders'], columns = 'counts')



print(t)




g = pd.crosstab(index=df['MPG'], columns = 'counts')
print(g)




o = pd.crosstab(index = df['Origin'], columns = 'counts')




print(o)





print(type(o))




o['Percentage'] = (o/o.sum())*100
print(o)



plt.figure(figsize =(7,2))
plt.barh(t.index, t['counts'])


#Control the width of the bar by changing the first argument in the figsize = (1, 2) and make the bar thinner by changing
#the second argument in the figsize(1,2)



plt.figure(figsize =(5,2))
plt.axis("equal")
plt.pie(t['counts'], labels = t.index, startangle = 90)





df.boxplot(column = 'MPG', by = 'Model')



#The line in the middle of the box is the median of cars' mile per gallon in certain model. For instance, the median MPG of a
#car in the 70 model is around 16, and the highest is a little below 30 and the lowest is 0, which is not possible.The first quartile
#represent in the lower part of the box is the median of the lower bound of the data set and third quartile is the median of 
#the higher part of the data set from the median.




df.boxplot(column = 'Horsepower', by = 'Cylinders')



k = pd.crosstab(df['Model'], columns = 'count')



print(k)


#Here I made another boxplot with column being horsepower comparing with number of cylinders. In the car data set, there is a
#linear realtionship between number of cylinders and horserpower. When there is more cylinders, the greater the median horserpower
#become.
plt.figure(figsize = (7, 5))
plt.scatter(df['MPG'], df['Weight']);


plt.figure(figsize = (5, 3))
plt.scatter(df['MPG'], df['Weight'], df['Cylinders']*10, df['Horsepower'])



#From this graph, The x-axis represented the range of MPG, and y-axis represented weight of the cars .Each circle represent a car; the size of each circle 
#represent the number of cylinders. The color represented the horsepower with yellow being very high and deep blue to black being low

plt.figure(figsize = (7,5))
plt.scatter(df['Acceleration'], df['Weight'], df['Horsepower'], df['Model'])
pd.plotting.scatter_matrix(df, figsize = (15, 15))




