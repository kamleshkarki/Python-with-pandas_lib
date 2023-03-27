from sqlalchemy import create_engine # pip install SQLAlchemy
from sqlalchemy.engine import URL
import pypyodbc # pip install pypyodbc
import pandas as pd # pip install pandas

SERVER_NAME = 'SAKSOFT174PDC'
DATABASE_NAME = 'TimeSheet'
TABLE_NAME = 'Timesheet'

excel_file = 'Timesheets.xlsx'

connection_string = f"""
    DRIVER={{SQL Server}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trusted_Connection=yes;
"""

connection_url = URL.create('mssql+pyodbc', query={'odbc_connect': connection_string})
enigne = create_engine(connection_url, module=pypyodbc)

excel_file = pd.read_excel(excel_file, sheet_name=None)
for sheet_name, df in excel_file.items():
    print(f'Loading worksheet {sheet_name}...')
    # {'fail', 'replace', 'append'}
    df.to_sql('Timesheets', enigne, if_exists='append', index=False)
    #df_data.to_sql('Timesheet', enigne, if_exists='append', index=False)
    