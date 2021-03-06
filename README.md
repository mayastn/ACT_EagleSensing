# ACT_EagleSensing

## Command Line Tool

Program to download and process Sentinel-2A L1C  products into L3 products and storing intermediate L2A products.

    $ bash main.sh -a A -p P -x X -s S -e E -d D -r R -l L

    (-h  Shows this help text)
    -a  Specify the path to dummy accounts (txt) to login to the platforms
    -p  Specify the platform (ama for amazon, esa for esa's scihub)
    -x  Specify the path of the extent dataset (i.e. Plantation GeoTiff)
    -s  Specify a start date (yyyymmdd)
    -e  Specify an end date (yyyymmdd)
    -d  Specify the directory path where the images will be stored (has to exist)
    -r  Specify the resolution for the atmospheric correction (in m)
    -l  Specify the atmospheric corrected L2A product directory (has to exist)

Example:

    $ bash main.sh -a a_Data_Acquisition/Data/accounts_hub.txt -p ama -x RGBmerge.tif -s 20170101 -e 20170201 -d Data -r 60 -l Results

## Project description
EagleSensing wants to explore Sentinel-2 integration into their platform that currently provides (large) plantation holders with airborne sensed imagery and its derived products. Sentinel-2 images are free of charge and the temporal resolution is high. Moreover, Sentinel-2's high spatial resolution for a satellite can be useful for a wide range of applications. Therefore, Sentinel-2 integration can benefit EagleSensing by: increasing monitoring frequency (very useful for existing clients); reaching small plantation holders with a limited budget and it assists EagleSensing in tackling the increase i technological competition in the GI sector by diversifying the product range.

However, for inclusion into EagleSensing's platform, a processing chain is needed to acquire and process data up to L2A product ready to be used for further development. This wish led to the scripting bundle created during the Geo-Information MSc course, Academic Consultancy Training in 2017. This scripting bundle includes five components: software and package installation, data acquisition, atmospheric correction, cloud detection and mosaicing. While the installation components should be run as a setting up procedure in a new machine, the data acquisition, atmospheric correction and mosaicing have been combined in one main script. The cloud detection component is more exploratory and has ample room for further development.
### Scripts header

- Component name
- Name of script/module
- Brief description of content
- Sources, if any

For example:

     a_Data_Aquisition
     get_passwords.py
     Gets the passwords for Sentinel Hub from a text file.
     Source: https://gis.stackexchange.com/a/57837 

### Components

1. ACT_EagleSensing
    1. a_Data_Acquisition
    1. b_Atmospheric_Correction
    1. c_Cloud_Detection
    1. d_Mosaicing
    1. z_Install_Software
    
 ### Documentation
 
 For each component an .MD file (like this one) a short description and additional info is given about the component operation.
 If additional documents are required (for instance Latex report) they should be linked via a OneDrive link/Overleaf doc.
 Additionally, technical documentation was also developed and it can be accesed through this link: https://www.overleaf.com/read/gtqpbsyzfxpz
