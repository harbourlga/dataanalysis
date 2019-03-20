import pandas as pd
from pandas import Series, DataFrame
new = Series([6,4, 3, 2], index=['c', 'd', 'e', 'f'])
print(new)
new_dataframe = DataFrame(columns=['shoe', 'years'], index=['a', 'b', 'c', 'd'])
print(new_dataframe)
new_dataframe['shoe'] = new
print(new_dataframe)