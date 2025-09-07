from functions.parse_xml import find_leaf_nodes_with_bounds
from functions.draw_image import annotate_image

import os

def process_all_files(input_dir, output_dir):
	'''finds all XML files in the input directory, processes them, and saves the annotated images to the output directory'''

	# creates the output directory if it does not exist
	if not os.path.exists(output_dir):
		os.makedirs(output_dir)

	# loop through every file in the input directory
	for filename in os.listdir(input_dir):
		
		# looks for XML files
		if filename.endswith('.xml'):

			# appends the file name to the input directory, constructing the full path of the file
			xml_path = os.path.join(input_dir, filename)

			# gets the base name without the extension
			# e.g., "com.giphy.messenger-2.xml" --> "com.giphy.messenger-2"
			base_name = os.path.splitext(filename)[0]

			# creates the path for the original PNG screenshot
			original_png_path = os.path.join(input_dir, base_name + '.png')

			# creates the path for the annotated PNG screenshot
			output_png_path = os.path.join(output_dir, base_name + '.png')

			print(f'Processing {filename}...')
			
			# get the coordinates from the XML file
			bounds = find_leaf_nodes_with_bounds(xml_path)

			# draw the boxes and save the new image
			annotate_image(original_png_path, output_png_path, bounds)
