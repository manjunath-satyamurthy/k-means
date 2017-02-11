import pickle, math, time
from PIL import Image, ImageDraw
from random import randint

k = int(raw_input("Enter the value for k (number of centroids)\n"))

unclustered_points = pickle.load(open("unclustered_points", "rb"))
centroids = []
previous_centroids = []

for _ in range(k):
	random_colour = (randint(0, 255), randint(0, 255), randint(0, 255))
	xa, xb = randint(192, 832), randint(192, 832)
	ya, yb = randint(144, 624), randint(144, 624)
	centroids.append((randint(192, 832), randint(144, 624), random_colour))
def initialize_image():
	base = Image.open('un_clustered.png')
	base.save("clustered.png")
	draw =ImageDraw.Draw(base)
	# time.sleep(0.1)
	return draw, base


while previous_centroids != centroids:
	draw, base = initialize_image()
	clusters = {}
	for point in unclustered_points:
		min_dist = None
		cluster_class = None
		class_str = ''
		for centroid in centroids:
			x_y = str(centroid[0])+'_'+str(centroid[1])
			if x_y not in clusters.keys():
				clusters[x_y] = {}
				clusters[x_y]['points'] = []
				clusters[x_y]['colour'] = centroid[2]

			distance = math.sqrt((centroid[0] - point[0])**2 + (centroid[1] - point[1])**2)
			if distance < min_dist or not min_dist:
				min_dist = distance
				cluster_class = centroid

		class_str = str(cluster_class[0])+'_'+str(cluster_class[1])
		clusters[class_str]['points'].append(point)
		
		draw.rectangle([point[0], point[1], point[0]+8, point[1]+8], fill=cluster_class[2])

	for centroid in centroids:
		x, y  = centroid[0], centroid[1]
		x1, y1 = x+20, y+20
		draw.ellipse([x, y, x1, y1], fill=centroid[2])
	print centroids
	print
	print
	# time.sleep(0.1)
	previous_centroids = centroids
	new_centroids = []

	for x_y in clusters.keys():
		clustered_points = clusters[x_y]['points']
		x, y = x_y.split('_')
		mean_x, mean_y = int(x), int(y)
		if len(clustered_points) > 0:		
			for point in clustered_points:
				mean_x += point[0]
				mean_y += point[1]
			mean_x = mean_x/len(clustered_points)
			mean_y = mean_y/len(clustered_points)

		new_centroids.append((mean_x, mean_y, clusters[x_y]['colour']))

	centroids = new_centroids
	del draw
base.save("clustered.png")