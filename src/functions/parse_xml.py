import re
from bs4 import BeautifulSoup

def find_leaf_nodes_with_bounds(xml_file):
	'''parses a potentially malformed XML file using BeautifulSoup, and returns the bounds of all leaf nodes'''

	# opens and reads the file's contents
	with open(xml_file, 'r', encoding='utf-8') as f:
		content = f.read()

	# parses the file (XML) content
	soup = BeautifulSoup(content, 'xml')

	# creates a list that will store the leaves' coordinates later on
	leaf_bounds = []

	# retrieves a list of every "<node>" tag in the file
	all_nodes = soup.find_all('node')

	for node in all_nodes:

		# finds all leaves (nodes without children)
		if not node.find('node'):

			# checks if the node has a 'bounds' attribute (the coordinates as a string type) 
			if node.has_attr('bounds'):

				bounds_str = node['bounds']
				
				# finds all sequences of one or more digits, then returns a list of numbers
				# e.g., [50, 100, 250, 300]
				coords = [int(n) for n in re.findall(r'\d+', bounds_str)]

				# checks if the bounding box has exactly 4 coordinates
				# e.g., (x1, y1, x2, y2)
				if len(coords) == 4:
					leaf_bounds.append(tuple(coords))	

	return leaf_bounds
