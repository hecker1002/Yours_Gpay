
''' This file contains the MEtadata setip( name , version , apckages) to put a STAMP/LOGO on the Lcoal PKG 
so as to treat them LIEK OFFICIAL PYTHON MODULES , 
and these are subsidiary of -e . (editable home dir ) in reuqirement.txt file rrquire this prokect location and 
and metadata ( setup.py file )
'''
from setuptools import setup , find_packages 

setup( name ="my_gpay_project" , version="0.1.0" , packages =find_packages() )