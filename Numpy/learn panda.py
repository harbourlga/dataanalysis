import pandas as pd
from pandas import Series, DataFrame



# Series
mjp = Series([5, 4, 3, 2, 1])
print(mjp)
print(mjp.index)
jeeva = Series([5, 4, 3, 2, 1, -7, -29], index = ['a', 'b', 'c', 'd', 'e', 'f', 'h'])
print('jeeva:{}'.format(jeeva))
print('jeeva["a"]:{}'.format(jeeva['a']))
jeeva['d'] = 9
print(jeeva)
print(jeeva[['a', 'b', 'c']])
print(jeeva[jeeva>0])
print(jeeva*2)



import numpy as np
print('Caculate the mean of jeeva to use numpy function:{}'.format(np.mean(jeeva)))
print('checks whether the index is present in Series or not:{},{}'.format('b' in jeeva, 'z' in jeeva))
player_salary={'Rooney':50000, 'Messi':75000, 'Ronaldo':85000, 'Fabregas':40000, 'Van persie':67000}
new_player = Series(player_salary)
print('converting a dictionary to a series:{}'.format(new_player))
players =['Klose', 'Messi', 'Ronaldo', 'Van persie', 'Ballack']
player_1 = Series(player_salary, index=players)
print('changed the index of the Series. Since, no value was not found for Klose and Ballack, it appears as NAN:{}'.format(player_1))
print('checks for Null values in player_1:{}'.format(pd.isnull(player_1)))
print('checks for null values that are not null:{}'.format(pd.notnull(player_1)))
player_1.name = 'Bundesliga players'
player_1.index.name = 'Player names'
print('name for the index and the Series:{}'.format(player_1))
player_1.index =['Neymar', 'Hulk', 'Pirlo', 'Buffon', 'Anderson']
print("is used to alter the index of Series 'player_1':{}".format(player_1))







#Data  Frame
states = {'State': ['Gujarat', 'Tamil Nadu', 'Andhra', 'Karnataka', 'Kerala'],
          'Population':[36, 44, 67, 89, 34],
          'Language':['Gujarati', 'Tamil', 'Telugu', 'Kannada', 'Malayalam']}
india = DataFrame(states)
print('data frame:{}'.format(india))
india_2 = DataFrame(states, columns = ['State', 'Language', 'Population'])
print('change the sequence of column index:{}'.format(india_2))
new_frame = DataFrame(states, columns=['State', 'Language', 'Population', 'Per Capital Income'], index=['a', 'b', 'c', 'd', 'e'])
print(new_frame)
print(new_frame.columns)
print('retrieveing data like dictionary:{}'.format(new_frame['State']))
print('retrieveing data like series:{}'.format(new_frame.Population))
print('using .ix function to retrive rows:{}'.format(new_frame.ix[3]))

new_frame['Per Capita Income'] = 99
print('the empty per capita income column can be assigned a value:{}'.format(new_frame))
new_frame['Per Capita Income'] = np.arange(5)
print(new_frame)

series = Series([44, 33, 22], index = ['b', 'c', 'd'])
new_frame['Per Capita Income'] = series
#when assigning list or arrays to a column,
# the values lenght should match the length of the DataFrame
print(new_frame)
new_frame['Development'] = new_frame.State == 'Gujarat'
print(new_frame)
del new_frame['Development']
print(new_frame)

new_data = {'Modi': {2010:72, 2012:78, 2014:98}, 'Rahul': {2010:55, 2012:34, 2014:22}}
elections = DataFrame(new_data)  #the outer dict keys are columns and inner dict keys are rows
print(elections)
print(elections.T)


# DataFrame(new_data, index = [2012, 2014, 2016])
ex= {'Gujarat':elections['Modi'][:-1], 'India': elections['Rahul'][:2]}
px =DataFrame(ex)
print(px)
px.index.name = 'year'
px.columns.name = 'politicians'
print(px)
print(px.values)

jeeva = Series([5, 4, 3, 2, 1, -7, -29], index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
index = jeeva.index
print(index)
print(index[1:])
# index[1] = 'f'#you cannot modify an index element. It will generate an error. In other words, they are immutable
# print(index)

print(px)
if 2013 in px.index:
    pass
else:
    print(False)

print(2013 in px.index)





#Reindex
var = Series(['Python', 'Java', 'c', 'c++', 'Php'], index = [5, 4, 3, 2, 1])
print('var:{}'.format(var))
var1 = var.reindex([1, 2, 3, 4, 5]) # reindex creates a new object
print(var1)
var_2 = var.reindex([1, 2, 3, 4, 5, 6, 7]) #introduces new indexes with values Nan
print(var_2)
var_2[6] = 9
print(var_2) #fill value
var_3 = var.reindex([1, 2, 3, 4, 5, 6, 7], fill_value=1) #all Nan full fill value
print(var_3)
gh = Series(['Dhoni', 'Sachin', 'Kohli'], index = [0, 2, 4])
print(gh)
gh_1 = gh.reindex(range(6), method = 'ffill') #ffill is forward fill. It forward fills the values
print(gh_1)
gh_2 = gh.reindex(range(6), method = 'bfill') # bfill, backward fills the values
print(gh_2)

fp = DataFrame(np.arange(9).reshape((3, 3)), index = ['a', 'b', 'c'], columns=['Gujarat', 'Tamil Nadu', 'Kerala'])
print(fp)
print(states)
fp_1 = fp.reindex(['a', 'b', 'c', 'd'], columns = states)
print(fp_1)




#Dropping entries from an axis
er = Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
print(er)
er_1 = er.drop(['b', 'c'])
print(er_1)
states ={'State' :['Gujarat', 'Tamil Nadu', ' Andhra', 'Karnataka', 'Kerala'],
         'Population': [36, 44, 67,89,34],
         'Language' :['Gujarati', 'Tamil', 'Telugu', 'Kannada', 'Malayalam']}
india = DataFrame(states, columns=['State', 'Population', 'Language'])
print(india)

print(india_drop)
india_drop1 = india.drop(['State', 'Population'], axis = 1) # the function dropped population and state columns. Apply the same concept with axis =0
print(india_drop1)

#Selection, Indexing and Filtering
var = Series(['Python', 'Java', 'c', 'c++', 'Php'], index = [5, 4, 3, 2, 1])
print(var)
print(var[5])
print(var[2:4])
print(var[[3, 2, 1]])
print(var[var=='Php'])

india_Selection = india[['Population', 'Language']]
print(india_Selection)
india_Selection = india[india['Population'] > 50]
print(india_Selection)
india_Selection = india[:3]
print(india_Selection)

india = DataFrame(states, columns =['State', 'Population', 'Language'], index =['a', 'b', 'c', 'd', 'e'])
india_Selection = india.ix[['a', 'b'], ['State', 'Language']]
print(india_Selection)

