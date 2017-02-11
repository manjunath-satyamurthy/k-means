from random import randint
from PIL import Image, ImageDraw
import pickle, math

width , height = 1024, 768
white = (255, 255, 255)
black = (0, 0, 0)

base = Image.new('RGB', (width, height), white)
draw =ImageDraw.Draw(base)

number_of_clusters = randint(10, 20)
cluster_cords = [] 

for _ in range(number_of_clusters):
	cluster_radius = randint(35, 80)
	cluster_elements = randint(200, 280)
	xc, yc = randint(192, 832), randint(144, 624)
	for _ in range(cluster_elements):
		x, y = randint(192, 832), randint(144, 624)
		distance = math.sqrt((x - xc)**2 + (y - yc)**2)

		if distance <= cluster_radius:
			draw.rectangle([x, y, x+8, y+8], fill=black)
			cluster_cords.append((x, y))
			base.save('un_clustered.png')

cluster_co_ords_file = open("unclustered_points","wb")
pickle.dump(cluster_cords, cluster_co_ords_file)
cluster_co_ords_file.close()
