#%%

import pandas as pd

#create three DataFrames
df1 = pd.DataFrame({'dataset': ['A', 'B', 'C', 'D', 'E']})
df2 = pd.DataFrame({'dataset': [13, 15, 15, 17, 22, 24, 29, 30]})
df3 = pd.DataFrame({'dataset': [3, 6, 6]})

#create a Pandas Excel writer using XlsxWriter as the engine
writer = pd.ExcelWriter('dataframes.xlsx', engine='xlsxwriter')

#write each DataFrame to a specific sheet
df1.to_excel(writer, sheet_name='first dataset')
df2.to_excel(writer, sheet_name='second dataset')
df3.to_excel(writer, sheet_name='third dataset')

#close the Pandas Excel writer and output the Excel file
writer.save()
# %%
