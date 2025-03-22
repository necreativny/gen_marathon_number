import sys

import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

import config

font = config.text_font



color = (34, 23, 51)
thickness = 1


drawing = False


############################################
###################### incorect font size recognition
###################### point recognition
###################### ..........
def draw(event, x, y, flags, params):
	global drawing, start_x, start_y, img
	img = cv2.imread(img_name)
	if event == cv2.EVENT_LBUTTONDOWN :
		drawing = True
		start_x,start_y = x,y
	elif event == cv2.EVENT_MOUSEMOVE :
		if drawing:
			cv2.rectangle(img, (start_x, start_y), (x, y), color, thickness)
	elif event == cv2.EVENT_LBUTTONUP :
		corner_point = (
			min(x, start_x),
			min(y, start_y)
		)
		size = (
			abs(x-start_x),
			abs(y-start_y),
		)
		center_point = (
			corner_point[0] + size[0]/2,
			corner_point[1] + size[1]/2
		)
		font_size = find_font_size(font, Image.fromarray(img), size[1]/len(img))
		b = img[corner_point[1], corner_point[0], 0]
		g = img[corner_point[1], corner_point[0], 1]
		r = img[corner_point[1], corner_point[0], 2]
		
		print('rectangle corner point', corner_point)
		print('rectangle center point', center_point)
		print('corner point color', r, g, b)
		print('font size', font_size/2)
		print('\n')
		
		cv2.rectangle(img, (start_x, start_y), (x, y), color, thickness)
		cv2.imwrite(img_name, img)
		drawing = False

def find_font_size(font, image_pil, target_width_ratio):
	text = '1'
	tested_font_size = 100
	tested_font = ImageFont.truetype(font, tested_font_size)
	im = Image.new('RGB', (image_pil.width, image_pil.height))
	draw = ImageDraw.Draw(im)
	textbbox = draw.textbbox((0,0), text, tested_font)
	text_width = textbbox[2]-textbbox[0]
	estimated_font_size = tested_font_size / (text_width / image_pil.width) * target_width_ratio
	return round(estimated_font_size)


img = cv2.imread(sys.argv[1])
img_name = 'draw.py-cv2.png'
cv2.imwrite(img_name, img)

cv2.namedWindow("Window")
cv2.setMouseCallback("Window",draw)

while(True):
	cv2.imshow("Window",img)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break
cv2.destroyAllWindows()
