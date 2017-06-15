# a_Data_Acquisition
# download_hub.py
# Downloads tiles captured in a given time interval that intersect with a provided raster, from Sentinel Data Hub.
# Sources: https://github.com/olivierhagolle/Sentinel-download

# connect to the API:  pip install sentinelsat
from sentinelsat.sentinel import SentinelAPI
import sys
import time
import os

sys.path.insert(0, 'a_Data_Acquisition')
from get_products_aoi import get_products_aoi
from accounts_hub import account

def download_amz(file_path,
                 accounts_file,
                 start_date = 'NOW-30DAYS',
                 end_date = 'NOW'):

    # Creates directory for download files
    owd = os.getcwd()  # original working directory (owd)
    new_dir = 'Data/hub%s' % time.strftime('%a%d%b%Y%H%M')
    os.mkdir(new_dir)

    # Credential management
    credentials = account(accounts_file)

    #for account in credentials:
    #    account += [0]
    # Try to add concurrent downloads

    api = SentinelAPI(credentials['rodr_almatos'][0], credentials['rodr_almatos'][1],'https://scihub.copernicus.eu/dhus')

    product = get_products_aoi(file_path, accounts_file,start_date=start_date,end_date=end_date)

    api.download_all(product)

    os.chdir(owd)

if __name__ == '__main__':
    download_amz('../Source_Data/Phillipines/RGBtile.tif','Data/accounts_hub.txt')







# amount of iterations
def enumerate(list, start=0):
    n = start
    for element in list:
        yield n, element
        n += 1
        print(idx)

# or
for idx, val in enumerate(ints):
    print(idx, val)