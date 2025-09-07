from functions.parse_xml import find_leaf_nodes_with_bounds
from functions.draw_image import annotate_image
from functions.handle_filenames import process_all_files

import sys

def main():
	# checks if there are two arguments after "main.py"
#	args = sys.argv[2:]
#
#	if not args:
#		print('Usage: python main.py <xml_file> <png_file>')
#		sys.exit(1)

	process_all_files('data/raw/Programming-Assignment-Data/Programming-Assignment-Data', 'data/processed')

if __name__ == '__main__':
	main()
