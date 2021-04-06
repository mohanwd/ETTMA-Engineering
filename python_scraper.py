from datetime import date
from os import path
import pandas as pd
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

base_url = "https://www.eia.gov/electricity/data/eia923/"
current_date = date.today()
initial_year = 2015
current_year = current_date.year


def download_and_unzip_files(base_url):
    page = requests.get(base_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for td in soup.find_all(lambda tag: tag.name == 'td' and tag.text.strip().endswith('ZIP')):
        link = td.find_next('a')
        my_file = requests.get(base_url + "/" + link['href'])
        file_name = link['href'].rsplit('/', 1)[1]
        for year in range(initial_year, current_year):
            if str(year) in file_name:
                open('c:/raw/' + file_name, 'wb').write(my_file.content)
                with ZipFile('c:/raw/' + file_name, 'r') as extract_zip:
                    extract_zip.extractall("C:\\raw")
            else:
                continue
    return "Files Downloading Completed"


def write_files_to_destination(initial_year, current_year):
    for file_year in range(initial_year, current_year):
        if not path.exists(
                'C:\\raw\\EIA923_Schedules_2_3_4_5_M_12_' + str(file_year) + '_Final_Revision.xlsx') or path.exists(
            'C:\\extracted\\Form923_fuel&Receipts&Costs_' + str(file_year) + '.csv'):
            print("File Not Present in source for " + str(file_year) + " or File exist in destination for " + str(
                file_year) + ".")
            continue
        read_file = pd.read_excel(r'C:\raw\EIA923_Schedules_2_3_4_5_M_12_' + str(file_year) + '_Final_Revision.xlsx',
                                  sheet_name='Page 5 Fuel Receipts and Costs')
        read_file.to_csv(r'C:\extracted\Form923_fuel&Receipts&Costs_' + str(file_year) + '.csv', index=None,
                         header=True)
    return "Files Creation Completed"


print(download_and_unzip_files(base_url))
print(write_files_to_destination(initial_year, current_year))
