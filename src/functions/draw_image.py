from PIL import Image, ImageDraw

def annotate_image(image_path, output_path, bounds_list):
	'''draws rectangles on an image based on a list of bounds'''

	# opens the original screenshot
	with Image.open(image_path) as img:
		draw = ImageDraw.Draw(img)

		for bounds in bounds_list:
			# the bounds are (x1, y1, x2, y2)
			# draws a yellow rectangle with width of 5
			draw.rectangle(bounds, outline='yellow', width=5)

	# save the new annotated image
	img.save(output_path)

	print(f'Saved annotated image to {output_path}')
