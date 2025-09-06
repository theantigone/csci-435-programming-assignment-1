import xml.etree.ElementTree as ET
import re       # using regex to parse bounds

def find_leaf_nodes_with_bounds(xml_file):
	'''parses an xml file and returns the bounds of all leaf nodes'''
	tree = ET.parse(xml_file)
	root = tree.getroot()   # returns the root element of a tree
	leaf_bounds = []

	# looks for any childless node
	for node in root.findall('.//node[not(node)]'):
		bounds_str = node.get('bounds')

		# finds all numbers in the string
		coords = [int(n) for n in re.findall(r'\d+', bounds_str)]

		# safety check to ensure that the bounding box has four coordinates --> (x1, y1, x2, y2)
		if len(coords) == 4:
			# converts the list to a tuple because these coordinates should not change
			leaf_bounds.append(tuple(coords))

	# returns the final list (e.g. [50, 100, 250, 300])
	return leaf_bounds
