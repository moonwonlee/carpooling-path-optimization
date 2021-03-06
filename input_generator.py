# Input generator (node_size.in) using the unioned graph generated by rgg.py
# Also make an phase1 output which is dropping all TAs at the starting point (node_size.text).
import math
import student_utils as su
import numpy as np
import networkx as nx
# For graph visualizer
import matplotlib.pyplot as plt
import random
import pandas as pd
import pycountry as pc
import rgg as rgg
import utils

"""
======================================================================
   Input Generator
======================================================================
"""


# Add 1st, 2nd, 3rd, 4th, 5th line in .in file
def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)


# Give position to each vertex in G
def assign_nodes_pos_names(graph, pos_max_range):
    country_short_names = list(pc.countries)
    list_locations = ""
    print(list(graph.nodes))
    for i in list(graph.nodes):
        x = np.random.randint(0, pos_max_range)
        y = np.random.randint(0, pos_max_range)
        graph.nodes[i]['pos'] = (x, y)
        graph.nodes[i]['name'] = country_short_names[i].alpha_3.replace(" ", "")
        list_locations = list_locations + " " + country_short_names[i].alpha_3
    list_locations = list_locations.lstrip()
    print("list_locations:\n" + list_locations)
    # for i in range(nx.number_of_nodes(graph)):
    #     x = np.random.randint(0, 100)
    #     y = np.random.randint(0, 100)
    #     graph.nodes[i]['pos'] = (x, y)
    #     graph.nodes[i]['name'] = country_short_names[i].alpha_3.replace(" ", "")
    #     list_locations = country_short_names[i].alpha_3 + " " + list_locations
    return list_locations


# Give weight to each edge in G
def assign_edges_weights(graph, num_round=2):
    for (u, v) in graph.edges():
        x1, y1 = graph.nodes[u]['pos']
        x2, y2 = graph.nodes[v]['pos']
        # Get the distance between endpoints of the given edge
        weight = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        # Round to NUM_ROUND decimal points
        weight = round(weight, num_round)
        graph[u][v]['weight'] = weight


# Pick a starting point and homes and assign is_home data to all of vertices
def pick_sp_and_home_(graph, sp_num, num_locations, num_homes):
    if num_homes > num_locations:
        return "too many homes: homes > locations\n"
    # Node's 'is_home' data is boolean
    # the starting location can be a home.
    list_homes = ""
    for i in list(graph.nodes):
        graph.nodes[i]['is_home'] = False
        graph.nodes[i]['is_sp'] = False
    graph.nodes[list(graph.nodes)[sp_num]]['is_sp'] = True
    for i in random.sample(range(num_locations), num_homes):
        graph.nodes[list(graph.nodes)[i]]['is_home'] = True
        list_homes = graph.nodes[list(graph.nodes)[i]]['name'] + " " + list_homes
    return list_homes, graph.nodes[list(graph.nodes)[sp_num]]['name']


# Initial values for g
num_locations = 200
num_homes = 100  # if you want random number of homes then np.random.randint(0, num_locations)
sp_num = np.random.randint(0, num_locations)
NUM_ROUND = 5

if num_locations == 50 or num_locations == 100 or num_locations == 200:
    g = rgg.crafted_rgg(num_locations)
else:
    g = nx.fast_gnp_random_graph(n=num_locations, p=0.4, seed=None, directed=False)
g = nx.convert_node_labels_to_integers(g, first_label=0, ordering='default', label_attribute=None)
list_locations = assign_nodes_pos_names(g, 100)
assign_edges_weights(g, NUM_ROUND)
list_homes, sp = pick_sp_and_home_(g, sp_num, num_locations, num_homes)

# Check G is metric
g_is_metric = su.is_metric(g)
g_is_connected = nx.is_connected(g)
if g_is_metric and g_is_connected:
    print("\nIs G metric (numNodes=" + str(nx.number_of_nodes(g)) + "): True")
    print('Is G connected : True\n')
    # Convert G to numpy_array for adjacency matrix
    g_2d_array = nx.to_numpy_array(g)

    # Write g to file.in following the specific format illustrated.
    fileName = str(num_locations) + '.in'
    first_five_lines = str(num_locations) + '\n' + str(
        num_homes) + '\n' + list_locations + '\n' + list_homes + '\n' + sp + '\n'

    df = pd.DataFrame(data=g_2d_array)
    df = df.astype(str)
    df = df.mask(df == '0.0', 'x')
    df.to_csv(fileName, sep=' ', index=False, header=False)
    line_prepender(fileName, first_five_lines)

    # Visualize G in a separate window
    nx.draw(g)
    plt.show()

    """
    ======================================================================
       Output Generator for Phase 1
    ======================================================================
    # """
    # # Output Generator for Phase 1
    # input_data = utils.read_file(fileName)
    # num_of_locations, num_houses, list_locations, list_houses, starting_car_location, adjacency_matrix = su.data_parser(
    #     input_data)
    # message = ''
    # G, message = su.adjacency_matrix_to_graph(adjacency_matrix)
    #
    # drop_off_mapping_text = starting_car_location
    #
    # from_sp_to_homes = []
    # for house in list_houses:
    #     drop_off_mapping_text = drop_off_mapping_text + ' ' + house
    #     from_sp_to_homes.append(house)
    # # drop off_mapping is a dictionary of drop off location to list of TAs that got off at said drop off location
    # drop_off_mapping = {starting_car_location: from_sp_to_homes}
    #
    # car_cycle = [starting_car_location]
    # car_cycle_text = starting_car_location
    #
    # num_distinct_loc_ta_dropped = 1
    # text_to_be_written = car_cycle_text + '\n' + str(num_distinct_loc_ta_dropped) + '\n' + drop_off_mapping_text
    # # print("text to be written:\n " + text_to_be_written)
    # fileName = str(num_of_locations) + '.txt'
    # file1 = open(fileName, "w")
    # file1.write(text_to_be_written)
    # file1.close()  # This close() is important
else:
    print("\n")
    if not g_is_metric:
        print(" Is g metric (numNodes=" + str(nx.number_of_nodes(g)) + "): False")
    else:
        print(" Is g metric (numNodes=" + str(nx.number_of_nodes(g)) + "): True")
    if not g_is_connected:
        print(" Is g connected: " + str(g_is_connected))
    print(" Fail!!!! Input.in, output.out not generated\n")
    nx.draw(g)
    plt.show()
