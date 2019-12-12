import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
import pandas as pd

def crafted_rgg(num_vertices):
	num_vertices = int(num_vertices)
	if num_vertices == 50:
		# 50 Vertices
		rangeList = [[0,14], [15,34], [35,36], [37,39], [40,44], [45,46], [47,49]]

		G = nx.fast_gnp_random_graph(rangeList[0][1]-rangeList[0][0]+1, 0.6, seed=None, directed=False)
		G2 = nx.fast_gnp_random_graph(rangeList[1][1]-rangeList[1][0]+1, 0.6, seed=None, directed=False)
		G3 = nx.fast_gnp_random_graph(rangeList[2][1]-rangeList[2][0]+1, 0.9, seed=None, directed=False)
		G4 = nx.fast_gnp_random_graph(rangeList[3][1]-rangeList[3][0]+1, 0.8, seed=None, directed=False)
		G5 = nx.fast_gnp_random_graph(rangeList[4][1]-rangeList[4][0]+1, 0.8, seed=None, directed=False)
		G6 = nx.fast_gnp_random_graph(rangeList[5][1]-rangeList[5][0]+1, 0.8, seed=None, directed=False)
		G7 = nx.fast_gnp_random_graph(rangeList[6][1]-rangeList[6][0]+1, 0.8, seed=None, directed=False)

		union = nx.union(G, G2, rename = ('a', 'b'))
		union2 = nx.union(union, G3, rename = ('b', 'c'))
		union3 = nx.union(union2, G4, rename = ('c', 'd'))
		union4 = nx.union(union3, G5, rename = ('d', 'e'))
		union5 = nx.union(union4, G6, rename = ('e', 'f'))
		union6 = nx.union(union5, G7, rename = ('f', 'g'))

	#	print(list(union6.nodes))

		for i in range(5):
			for j in range(1,7):
				randomVertex1 = random.randint(rangeList[0][0],rangeList[0][1])
				randomVertex2 = random.randint(rangeList[j][0],rangeList[j][1])

				# print("Random Vertex 1", randomVertex1)
				# print("Random Vertex 2", randomVertex2)

				union6.add_edge(list(union6.nodes)[randomVertex1],list(union6.nodes)[randomVertex2])
		for i in range(15):
			randomVertex1 = random.randint(rangeList[0][0], rangeList[0][1])
			randomVertex2 = random.randint(rangeList[1][0], rangeList[1][1])
			union6.add_edge(list(union6.nodes)[randomVertex1], list(union6.nodes)[randomVertex2])
		# nx.draw(union6)
		# plt.show()
		return union6
	elif num_vertices == 100:
		rangeList = [[0,14], [15,34], [35,36], [37,39], [40,44], [45,46], [47,49], [50,64], [65,84], [85,86], [87,89], [90,94], [95,96], [97,99]]

		G = nx.fast_gnp_random_graph(rangeList[0][1]-rangeList[0][0]+1, 0.6, seed=None, directed=False)
		G2 = nx.fast_gnp_random_graph(rangeList[1][1]-rangeList[1][0]+1, 0.6, seed=None, directed=False)
		G3 = nx.fast_gnp_random_graph(rangeList[2][1]-rangeList[2][0]+1, 0.9, seed=None, directed=False)
		G4 = nx.fast_gnp_random_graph(rangeList[3][1]-rangeList[3][0]+1, 0.8, seed=None, directed=False)
		G5 = nx.fast_gnp_random_graph(rangeList[4][1]-rangeList[4][0]+1, 0.8, seed=None, directed=False)
		G6 = nx.fast_gnp_random_graph(rangeList[5][1]-rangeList[5][0]+1, 0.8, seed=None, directed=False)
		G7 = nx.fast_gnp_random_graph(rangeList[6][1]-rangeList[6][0]+1, 0.8, seed=None, directed=False)
		G8 = nx.fast_gnp_random_graph(rangeList[7][1]-rangeList[7][0]+1, 0.5, seed=None, directed=False)
		G9 = nx.fast_gnp_random_graph(rangeList[8][1]-rangeList[8][0]+1, 0.45, seed=None, directed=False)
		G10 = nx.fast_gnp_random_graph(rangeList[9][1]-rangeList[9][0]+1, 0.9, seed=None, directed=False)
		G11 = nx.fast_gnp_random_graph(rangeList[10][1]-rangeList[10][0]+1, 0.8, seed=None, directed=False)
		G12 = nx.fast_gnp_random_graph(rangeList[11][1]-rangeList[11][0]+1, 0.8, seed=None, directed=False)
		G13 = nx.fast_gnp_random_graph(rangeList[12][1]-rangeList[12][0]+1, 0.8, seed=None, directed=False)
		G14 = nx.fast_gnp_random_graph(rangeList[13][1]-rangeList[13][0]+1, 0.8, seed=None, directed=False)

		union = nx.union(G, G2, rename = ('a', 'b'))
		union2 = nx.union(union, G3, rename = ('b', 'c'))
		union3 = nx.union(union2, G4, rename = ('c', 'd'))
		union4 = nx.union(union3, G5, rename = ('d', 'e'))
		union5 = nx.union(union4, G6, rename = ('e', 'f'))
		union6 = nx.union(union5, G7, rename = ('f', 'g'))
		union7 = nx.union(union6, G8, rename = ('g', 'h'))
		union8 = nx.union(union7, G9, rename = ('h', 'i'))
		union9 = nx.union(union8, G10, rename = ('i', 'j'))
		union10 = nx.union(union9, G11, rename = ('j', 'k'))
		union11 = nx.union(union10, G12, rename = ('k', 'l'))
		union12 = nx.union(union11, G13, rename = ('l', 'm'))
		union13 = nx.union(union12, G14, rename = ('m', 'n'))

		#print(list(union13.nodes))

		for i in range(5):
			for j in range(1,14):
				randomVertex1 = random.randint(rangeList[i][0],rangeList[i][1])
				randomVertex2 = random.randint(rangeList[j][0],rangeList[j][1])

				# print("Random Vertex 1", randomVertex1)
				# print("Random Vertex 2", randomVertex2)

				union13.add_edge(list(union13.nodes)[randomVertex1],list(union13.nodes)[randomVertex2])
		for i in range(15):
			randomVertex1 = random.randint(rangeList[0][0], rangeList[0][1])
			randomVertex2 = random.randint(rangeList[1][0], rangeList[1][1])
			union13.add_edge(list(union13.nodes)[randomVertex1], list(union13.nodes)[randomVertex2])

			rVertex1 = random.randint(rangeList[7][0], rangeList[7][1])
			rVertex2 = random.randint(rangeList[8][0], rangeList[8][1])

			union13.add_edge(list(union13.nodes)[rVertex1], list(union13.nodes)[rVertex2])

			randomVertex1 = random.randint(rangeList[7][0], rangeList[7][1])
			randomVertex2 = random.randint(rangeList[1][0], rangeList[1][1])
			union13.add_edge(list(union13.nodes)[randomVertex1], list(union13.nodes)[randomVertex2])

			randomVertex1 = random.randint(rangeList[8][0], rangeList[8][1])
			randomVertex2 = random.randint(rangeList[0][0], rangeList[0][1])
			union13.add_edge(list(union13.nodes)[randomVertex1], list(union13.nodes)[randomVertex2])

			randomVertex1 = random.randint(rangeList[7][0], rangeList[7][1])
			randomVertex2 = random.randint(rangeList[0][0], rangeList[0][1])
			union13.add_edge(list(union13.nodes)[randomVertex1], list(union13.nodes)[randomVertex2])
		# nx.draw(union13)
		# plt.show()
		return union13

	elif num_vertices  == 200:
		rangeList = [[0, 14], [15, 34], [35, 36], [37, 39], [40, 44], [45, 46], [47, 49], [50, 64], [65, 84], [85, 86],
					 [87, 89], [90, 94], [95, 96], [97, 99],
					 [100, 114], [115, 134], [135, 136], [137, 139], [140, 144], [145, 146], [147, 149], [150, 164],
					 [165, 184], [185, 186], [187, 189], [190, 194], [195, 196], [197, 199]]

		G = nx.fast_gnp_random_graph(rangeList[0][1] - rangeList[0][0] + 1, 0.35, seed=None, directed=False)
		G2 = nx.fast_gnp_random_graph(rangeList[1][1] - rangeList[1][0] + 1, 0.35, seed=None, directed=False)
		G3 = nx.fast_gnp_random_graph(rangeList[2][1] - rangeList[2][0] + 1, 0.9, seed=None, directed=False)
		G4 = nx.fast_gnp_random_graph(rangeList[3][1] - rangeList[3][0] + 1, 0.8, seed=None, directed=False)
		G5 = nx.fast_gnp_random_graph(rangeList[4][1] - rangeList[4][0] + 1, 0.8, seed=None, directed=False)
		G6 = nx.fast_gnp_random_graph(rangeList[5][1] - rangeList[5][0] + 1, 0.8, seed=None, directed=False)
		G7 = nx.fast_gnp_random_graph(rangeList[6][1] - rangeList[6][0] + 1, 0.8, seed=None, directed=False)
		G8 = nx.fast_gnp_random_graph(rangeList[7][1] - rangeList[7][0] + 1, 0.4, seed=None, directed=False)
		G9 = nx.fast_gnp_random_graph(rangeList[8][1] - rangeList[8][0] + 1, 0.25, seed=None, directed=False)
		G10 = nx.fast_gnp_random_graph(rangeList[9][1] - rangeList[9][0] + 1, 0.9, seed=None, directed=False)
		G11 = nx.fast_gnp_random_graph(rangeList[10][1] - rangeList[10][0] + 1, 0.8, seed=None, directed=False)
		G12 = nx.fast_gnp_random_graph(rangeList[11][1] - rangeList[11][0] + 1, 0.8, seed=None, directed=False)
		G13 = nx.fast_gnp_random_graph(rangeList[12][1] - rangeList[12][0] + 1, 0.8, seed=None, directed=False)
		G14 = nx.fast_gnp_random_graph(rangeList[13][1] - rangeList[13][0] + 1, 0.8, seed=None, directed=False)
		G15 = nx.fast_gnp_random_graph(rangeList[14][1] - rangeList[14][0] + 1, 0.3, seed=None, directed=False)
		G16 = nx.fast_gnp_random_graph(rangeList[15][1] - rangeList[15][0] + 1, 0.3, seed=None, directed=False)
		G17 = nx.fast_gnp_random_graph(rangeList[16][1] - rangeList[16][0] + 1, 0.9, seed=None, directed=False)
		G18 = nx.fast_gnp_random_graph(rangeList[17][1] - rangeList[17][0] + 1, 0.8, seed=None, directed=False)
		G19 = nx.fast_gnp_random_graph(rangeList[18][1] - rangeList[18][0] + 1, 0.8, seed=None, directed=False)
		G20 = nx.fast_gnp_random_graph(rangeList[19][1] - rangeList[19][0] + 1, 0.8, seed=None, directed=False)
		G21 = nx.fast_gnp_random_graph(rangeList[20][1] - rangeList[20][0] + 1, 0.8, seed=None, directed=False)
		G22 = nx.fast_gnp_random_graph(rangeList[21][1] - rangeList[21][0] + 1, 0.4, seed=None, directed=False)
		G23 = nx.fast_gnp_random_graph(rangeList[22][1] - rangeList[22][0] + 1, 0.25, seed=None, directed=False)
		G24 = nx.fast_gnp_random_graph(rangeList[23][1] - rangeList[23][0] + 1, 0.9, seed=None, directed=False)
		G25 = nx.fast_gnp_random_graph(rangeList[24][1] - rangeList[24][0] + 1, 0.8, seed=None, directed=False)
		G26 = nx.fast_gnp_random_graph(rangeList[25][1] - rangeList[25][0] + 1, 0.8, seed=None, directed=False)
		G27 = nx.fast_gnp_random_graph(rangeList[26][1] - rangeList[26][0] + 1, 0.8, seed=None, directed=False)
		G28 = nx.fast_gnp_random_graph(rangeList[27][1] - rangeList[27][0] + 1, 0.8, seed=None, directed=False)

		union = nx.union(G, G2, rename=('a', 'b'))
		union2 = nx.union(union, G3, rename=('b', 'c'))
		union3 = nx.union(union2, G4, rename=('c', 'd'))
		union4 = nx.union(union3, G5, rename=('d', 'e'))
		union5 = nx.union(union4, G6, rename=('e', 'f'))
		union6 = nx.union(union5, G7, rename=('f', 'g'))
		union7 = nx.union(union6, G8, rename=('g', 'h'))
		union8 = nx.union(union7, G9, rename=('h', 'i'))
		union9 = nx.union(union8, G10, rename=('i', 'j'))
		union10 = nx.union(union9, G11, rename=('j', 'k'))
		union11 = nx.union(union10, G12, rename=('k', 'l'))
		union12 = nx.union(union11, G13, rename=('l', 'm'))
		union13 = nx.union(union12, G14, rename=('m', 'n'))
		union14 = nx.union(union13, G15, rename=('n', 'o'))
		union15 = nx.union(union14, G16, rename=('b', 'c'))
		union16 = nx.union(union15, G17, rename=('c', 'd'))
		union17 = nx.union(union16, G18, rename=('d', 'e'))
		union18 = nx.union(union17, G19, rename=('e', 'f'))
		union19 = nx.union(union18, G20, rename=('f', 'g'))
		union20 = nx.union(union19, G21, rename=('g', 'h'))
		union21 = nx.union(union20, G22, rename=('h', 'i'))
		union22 = nx.union(union21, G23, rename=('i', 'j'))
		union23 = nx.union(union22, G24, rename=('j', 'k'))
		union24 = nx.union(union23, G25, rename=('k', 'l'))
		union25 = nx.union(union24, G26, rename=('l', 'm'))
		union26 = nx.union(union25, G27, rename=('m', 'n'))
		union27 = nx.union(union26, G28, rename=('m', 'n'))

		#print(list(union13.nodes))

		for i in range(5):
			for j in range(1, 28):
				randomVertex1 = random.randint(rangeList[i][0], rangeList[i][1])
				randomVertex2 = random.randint(rangeList[j][0], rangeList[j][1])

				# print("Random Vertex 1", randomVertex1)
				# print("Random Vertex 2", randomVertex2)

				union27.add_edge(list(union27.nodes)[randomVertex1], list(union27.nodes)[randomVertex2])
		for i in range(19):
			randomVertex1 = random.randint(rangeList[0][0], rangeList[0][1])
			randomVertex2 = random.randint(rangeList[1][0], rangeList[1][1])
			union27.add_edge(list(union27.nodes)[randomVertex1], list(union27.nodes)[randomVertex2])

			randomVertex1 = random.randint(rangeList[7][0], rangeList[7][1])
			randomVertex2 = random.randint(rangeList[1][0], rangeList[1][1])
			union27.add_edge(list(union27.nodes)[randomVertex1], list(union27.nodes)[randomVertex2])

			randomVertex1 = random.randint(rangeList[8][0], rangeList[8][1])
			randomVertex2 = random.randint(rangeList[0][0], rangeList[0][1])
			union27.add_edge(list(union27.nodes)[randomVertex1], list(union27.nodes)[randomVertex2])

			randomVertex1 = random.randint(rangeList[7][0], rangeList[7][1])
			randomVertex2 = random.randint(rangeList[0][0], rangeList[0][1])
			union27.add_edge(list(union27.nodes)[randomVertex1], list(union27.nodes)[randomVertex2])

			randomVertex1 = random.randint(rangeList[0][0], rangeList[0][1])
			randomVertex2 = random.randint(rangeList[13][0], rangeList[13][1])
			union27.add_edge(list(union27.nodes)[randomVertex1], list(union27.nodes)[randomVertex2])

			randomVertex1 = random.randint(rangeList[0][0], rangeList[0][1])
			randomVertex2 = random.randint(rangeList[14][0], rangeList[14][1])
			union27.add_edge(list(union27.nodes)[randomVertex1], list(union27.nodes)[randomVertex2])

			randomVertex1 = random.randint(rangeList[0][0], rangeList[0][1])
			randomVertex2 = random.randint(rangeList[20][0], rangeList[20][1])
			union27.add_edge(list(union27.nodes)[randomVertex1], list(union27.nodes)[randomVertex2])

			randomVertex1 = random.randint(rangeList[0][0], rangeList[0][1])
			randomVertex2 = random.randint(rangeList[21][0], rangeList[21][1])
			union27.add_edge(list(union27.nodes)[randomVertex1], list(union27.nodes)[randomVertex2])

			randomVertex1 = random.randint(rangeList[1][0], rangeList[1][1])
			randomVertex2 = random.randint(rangeList[14][0], rangeList[14][1])
			union27.add_edge(list(union27.nodes)[randomVertex1], list(union27.nodes)[randomVertex2])

			randomVertex1 = random.randint(rangeList[1][0], rangeList[1][1])
			randomVertex2 = random.randint(rangeList[20][0], rangeList[20][1])
			union27.add_edge(list(union27.nodes)[randomVertex1], list(union27.nodes)[randomVertex2])

			randomVertex1 = random.randint(rangeList[1][0], rangeList[1][1])
			randomVertex2 = random.randint(rangeList[21][0], rangeList[21][1])
			union27.add_edge(list(union27.nodes)[randomVertex1], list(union27.nodes)[randomVertex2])

			randomVertex1 = random.randint(rangeList[7][0], rangeList[7][1])
			randomVertex2 = random.randint(rangeList[13][0], rangeList[13][1])
			union27.add_edge(list(union27.nodes)[randomVertex1], list(union27.nodes)[randomVertex2])

			randomVertex1 = random.randint(rangeList[7][0], rangeList[7][1])
			randomVertex2 = random.randint(rangeList[14][0], rangeList[14][1])
			union27.add_edge(list(union27.nodes)[randomVertex1], list(union27.nodes)[randomVertex2])

			randomVertex1 = random.randint(rangeList[7][0], rangeList[7][1])
			randomVertex2 = random.randint(rangeList[20][0], rangeList[20][1])
			union27.add_edge(list(union27.nodes)[randomVertex1], list(union27.nodes)[randomVertex2])

			randomVertex1 = random.randint(rangeList[8][0], rangeList[8][1])
			randomVertex2 = random.randint(rangeList[13][0], rangeList[13][1])
			union27.add_edge(list(union27.nodes)[randomVertex1], list(union27.nodes)[randomVertex2])

			randomVertex1 = random.randint(rangeList[8][0], rangeList[8][1])
			randomVertex2 = random.randint(rangeList[14][0], rangeList[14][1])
			union27.add_edge(list(union27.nodes)[randomVertex1], list(union27.nodes)[randomVertex2])

			randomVertex1 = random.randint(rangeList[8][0], rangeList[8][1])
			randomVertex2 = random.randint(rangeList[20][0], rangeList[20][1])
			union27.add_edge(list(union27.nodes)[randomVertex1], list(union27.nodes)[randomVertex2])

			randomVertex1 = random.randint(rangeList[8][0], rangeList[8][1])
			randomVertex2 = random.randint(rangeList[21][0], rangeList[21][1])
			union27.add_edge(list(union27.nodes)[randomVertex1], list(union27.nodes)[randomVertex2])

			randomVertex1 = random.randint(rangeList[13][0], rangeList[13][1])
			randomVertex2 = random.randint(rangeList[14][0], rangeList[14][1])
			union27.add_edge(list(union27.nodes)[randomVertex1], list(union27.nodes)[randomVertex2])

			randomVertex1 = random.randint(rangeList[13][0], rangeList[13][1])
			randomVertex2 = random.randint(rangeList[21][0], rangeList[21][1])
			union27.add_edge(list(union27.nodes)[randomVertex1], list(union27.nodes)[randomVertex2])

			randomVertex1 = random.randint(rangeList[14][0], rangeList[14][1])
			randomVertex2 = random.randint(rangeList[20][0], rangeList[20][1])
			union27.add_edge(list(union27.nodes)[randomVertex1], list(union27.nodes)[randomVertex2])

			randomVertex1 = random.randint(rangeList[14][0], rangeList[14][1])
			randomVertex2 = random.randint(rangeList[21][0], rangeList[21][1])
			union27.add_edge(list(union27.nodes)[randomVertex1], list(union27.nodes)[randomVertex2])

			randomVertex1 = random.randint(rangeList[20][0], rangeList[20][1])
			randomVertex2 = random.randint(rangeList[21][0], rangeList[21][1])
			union27.add_edge(list(union27.nodes)[randomVertex1], list(union27.nodes)[randomVertex2])


		#print(nx.adjacency_matrix(union27))
		# nx.draw(union27)
		# plt.show()
		return union27
	else:
		raise ValueError("num_vertices not one of 50 100 200")
#
# var = input("Enter number of vertices(50, 100 ,200): ")
# crafted_rgg(var)