import sqlalchemy as sa
from sqlalchemy import create_engine
import urllib
import pyodbc
 
conn = urllib.parse.quote_plus(
    'Data Source Name=MssqlDataSource;'
    'Driver={SQL Server};'
    'Server=PUTSERVERNAME;'
    'Database=TimeSheets;'
    'Trusted_connection=yes;'
)
 
try:
    coxn = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(conn))
    print("Passed")
 
except:
    print("failed!")
