from pandas.core.frame import DataFrame
import pandas as pd
from DbConn import coxn
 
df = pd.read_excel('Timesheets.xlsx', engine = 'openpyxl')
 
try:
   df.to_sql('Time',con=coxn,if_exists='replace')

except:
    pass
    print("Failed!")

else:
    print("saved in the table")
print(df)