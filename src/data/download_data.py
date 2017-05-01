# -*- coding: utf-8 -*-
import os
from os.path import splitext
import yaml
import click
import urllib.request
import xlrd
import csv

BAG_FILE_LOCATIONS = 'references/bag_kennzahlen_files.yaml'


###############################################################################
###   change_file_extenstion
###    :param filename:	filename to be modified
###    :param ext:  	new extension. Example ".csv"
###    :return:			the filename with the new extenstion
###
###############################################################################
def change_file_extenstion(filename, ext):
	return splitext(filename)[0] + ext

###############################################################################
###   convert_to_csv
###    :param filename:  path and filename with the excel sheet
###    :param worksheet:  name of the worksheet in excel to be exported
###
###############################################################################
def convert_to_csv(filename,worksheet):

	with xlrd.open_workbook(filename) as wb:
		sh = wb.sheet_by_index(worksheet)  # or wb.sheet_by_name('name_of_the_sheet_here')
		with open(change_file_extenstion(filename, '.csv'), 'w') as f:
			c = csv.writer(f)
			for r in range(sh.nrows):
				c.writerow(sh.row_values(r))


###############################################################################
###   load_files_from_file
###    :param filename:  path and filename with the information for each file (yaml)
###    :return:          dictionary with key = filename and value = url
###
###############################################################################
def load_files_from_file(filename):
	return yaml.load(open(filename))

###############################################################################
###   M A I N
###############################################################################
@click.command()
@click.argument('target_filepath', type=click.Path(exists=True), default="data/raw")
def main(target_filepath):	
	downloads = load_files_from_file(BAG_FILE_LOCATIONS)
	for year, dataset in downloads.items():

		print("downloading file %s from %s" % (dataset['filename'],dataset['url']))
		fullpath = os.path.join(target_filepath, dataset['filename'])
		urllib.request.urlretrieve(dataset['url'], fullpath)

		print("converting file %s to csv" % (dataset['filename']))
		convert_to_csv(fullpath, dataset['worksheet'])

# start the script if executed directly
if __name__ == '__main__':
    main()