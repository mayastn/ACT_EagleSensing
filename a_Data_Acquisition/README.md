# a_Data_Acquisition

## Necessary packages
* sentinelhub
* sentinelsat
* parmap
* requests
* fire

## Command Line Interface for downloading
### From Amazon Web Services
    
    python download_amz.py DOWNLOAD_DIR FILE_PATH ACCOUNTS_FILE [START_DATE] [END_DATE] [EXCLUDE_DATE]

Or:
    
    download_amz.py --download_dir DOWNLOAD_DIR --file-path FILE_PATH --accounts-file ACCOUNTS_FILE [--start-date START_DATE] [--end-date END_DATE] [--exclude-date EXCLUDE_DATE]
     
Help:

    python download_amz.py -- --help

### From Sentinel Data Hub

    python download_hub.py DOWNLOAD_DIR FILE_PATH ACCOUNTS_FILE [START_DATE] [END_DATE] [DOWNLOADS_PER_ACCOUNT] [MAX_DOWNLOADS]

Or:

    python download_hub.py --download_dir DOWNLOAD_DIR --file-path FILE_PATH --accounts-file ACCOUNTS_FILE [--start-date START_DATE] [--end-date END_DATE] [--downloads-per-account DOWNLOADS_PER_ACCOUNT]

For help:

    python download_hub.py -- --help
    
## Inputs
* DOWNLOAD_DIR - relative (in relation with script directory) or absolute. Dir where the files will be downloaded in a new folder with an unique timestamp.
* FILE_PATH - relative (in relation with script directory) or absolute, between "". Should be in GeoTiff format, gives the spatial search extent.
* ACCOUNTS_FILE - relative (in relation with script directory) or absolute, between "". Should be a text file with each account in each line. The username and login in each line should be separated by a space.
* START_DATE - YYYYMMDD, NOW-XDAYS, defaults to NOW-30DAYS.
* END_DATE - YYYYMMDD, NOW-XDAYS, defaults to NOW.
Example of command:

      python download_hub.py 'Data/' 'ACT_EagleSensing/Source_Data/Phillipines/RGBtile.tif' 'ACT_EagleSensing/a_Data_Acquisition/Data/accounts_hub.txt' '20160102' '20160120'

## Modules
* **download_amz.py**
    * Downloads tiles captured in a given time interval that intersect with a provided raster, from AWS.
    * Contains the following parameters:
        * download_dir
        * file_path
        * accounts_file 
        * start_date (in format YYYYMMDD, NOW-3DAYS will work)
        * end_date (in format YYYYMMDD, NOW will work)
        * exclude_date (in this format - datetime.datetime(2016,12,6))
    * Creates a directory in download_dir with timestamp (in format amzDayDaynumberMonthYearHourMinuteSecond)
    * This option is not able to download tiles from before 6/12/2016. This is due to an update in the Product Structure Definition of Sentinel tiles.
* **download_hub.py**
    * Downloads tiles captured in a given time interval that intersect with a provided raster, from Sentinel Data Hub.
    * Contains the following parameters:
        * download_dir
        * file_path
        * accounts_file 
        * start_date (in format YYYYMMDD, NOW-3DAYS will work)
        * end_date (in format YYYYMMDD, NOW will work)
        * downloads_per_account (default is 1, maximum allowed is 2)
        * max_downloads (default = 10)
    * Creates a directory in download_dir with timestamp (in format hubDayDaynumberMonthYearHourMinuteSecond)
    * It is able to download files from before 6/12/2016, but beware, since the downloaded directories are very long and surpass the MS Windows directory character limit.
* get_extent.py
    * Gets the extent of a raster file and saves it into GeoJSON.
    * Handles differente CRS and provides JSON object in WGS84.
* accounts_hub.py
    * Gets Sentinel Hub user credentials out of a text file (accounts_hub.txt in this case) into a dictionary for use in the download process.
    * Credentials contain: username & password
* get_products_aoi.py
    * Gets a list of product names matching a given time interval that intersect with a provided raster. Also, provides credentials object.
    * contains get_products_aoi function: 
         * Creates an ordered dictionary of products that intersect with the extent of a raster file in a provided date interval.


