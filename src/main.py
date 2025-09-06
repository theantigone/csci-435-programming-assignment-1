from functions.parse_xml import find_leaf_nodes_with_bounds
from functions.draw_image import annotate_image

import sys

def main():
	# checks if there are two arguments after "main.py"
	args = sys.argv[2:]

	if not args:
		print('Usage: python main.py <xml_file> <png_file>')
		sys.exit(1)

	# parses the xml file
	bounds_list = find_leaf_nodes_with_bounds(sys.argv[1])

	# saves the location in the "processed" directory
	image_file = sys.argv[2]
	output_file = '../data/processed/'

	# draws image_file and saves it to output_file
	annotate_image(image_file, output_file, bounds_list)

if __name__ == '__main__':
	main()
