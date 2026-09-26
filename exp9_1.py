import pandas as pd
data=[10,20,30]
label=['a','b','c']
series=pd.Series(data,index=label)
print("Pandas Series:")
print(series)
print("Values at label 'b':",series['b'])