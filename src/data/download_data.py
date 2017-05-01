# -*- coding: utf-8 -*-
import os
import click
import urllib.request

BAG_FILE_LOCATIONS = 'references/bag_kennzahlen_files.txt'

###############################################################################
###   load_files_from_file
###    :param filename:  path and filename with the names and locations 
###						 to be downloaded
###    :return:          dictionary with key = filename and value = url
###
###############################################################################

def load_files_from_file(filename):
	myvars = {}
	with open(filename) as myfile:
		for line in myfile:
			name, var = line.partition("=")[::2]
			myvars[name.strip()] = var.strip()
	return myvars

###############################################################################
###   M A I N
###############################################################################
@click.command()
@click.argument('target_filepath', type=click.Path(exists=True), default="data/raw")
def main(target_filepath):	
	downloads = load_files_from_file(BAG_FILE_LOCATIONS)
	for filename ,url in downloads.items():
		print("downloading file %s from %s" % (filename,url))
		fullpath = os.path.join(target_filepath, filename)
		urllib.request.urlretrieve(url, fullpath)


# start the script if executed directly
if __name__ == '__main__':
    main()