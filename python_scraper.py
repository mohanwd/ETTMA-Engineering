import pandas as pd
from datetime import date
from os import path

current_date = date.today()
initial_year = 2015
current_year = current_date.year

for year in range(initial_year, current_year):
    if not path.exists('C:\\raw\\EIA923_Schedules_2_3_4_5_M_12_' + str(year) + '_Final_Revision.xlsx') or path.exists('C:\\extracted\\Form923_fuel&Receipts&Costs_' + str(year) + '.csv'):
        print("File Not Present in source for "+str(year)+" or File exist in destination for "+str(year)+".")
        continue
    read_file = pd.read_excel(r'C:\raw\EIA923_Schedules_2_3_4_5_M_12_' + str(year) + '_Final_Revision.xlsx',
                              sheet_name='Page 5 Fuel Receipts and Costs')
    read_file.to_csv(r'C:\extracted\Form923_fuel&Receipts&Costs_' + str(year) + '.csv', index=None, header=True)
