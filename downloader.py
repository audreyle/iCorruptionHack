"""
Check the FEC website to find if a new filing has been posted.
If there is a new filing store it in /data folder with new date.

http://www.fec.gov/finance/disclosure/ftpdet.shtml

indiv16.zip 
oth16.zip
"""

from app import root
import subprocess

def get_file():
    '''
    Get file from URL
    '''

    urls = ['ftp://ftp.fec.gov/FEC/2016/indiv16.zip']

    v = subprocess.call(['sh', root+'/download.sh'])
    
    print v

def already_downloaded(file):
    '''
    Return true if we already have this version of the file
    (check date and file hash). False otherwise
    '''
    pass

def save(file):
    '''
    Assign proper namin and save file in the appropriate folder.
    '''

def download():
    '''Grabs the latest.'''
    my_file = get_file()

    if already_downloaded(my_file):
        print "Didn't save"
    else:
        save(my_file)


get_file()
