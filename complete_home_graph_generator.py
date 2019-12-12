import argparse

import student_utils as su
import numpy as np
import networkx as nx
import utils
import os
from input_validator import VALID_FILENAMES, RANGE_OF_INPUT_SIZES, MAX_NAME_LENGTH
import math
import matplotlib.pyplot as plt

"""
This function is based on tests function in input_validator.py

Output:
        
"""


# different from version_no_walking
def give_nodes_names(is_sp_home, graph, num_houses, list_of_homes, starting_car_location):
    # always 0 index of the new Complete Graph is starting point.
    if is_sp_home:
        sp_index_in_homes = list_of_homes.index(starting_car_location)
        graph.nodes[0]['name'] = starting_car_location
        for i in range(num_houses):
            graph.nodes[i]['name'] = list_of_homes[i]
        graph.nodes[sp_index_in_homes]['name'] = graph.nodes[0]['name']
        graph.nodes[0]['name'] = starting_car_location

    else:
        graph.nodes[0]['name'] = starting_car_location
        for i in range(1, num_houses + 1):
            # print(i)
            graph.nodes[i]['name'] = list_of_homes[i - 1]
        # print(graph.nodes[i]['name'])

# give the complete graph new weights
def give_edges_weights(new_graph, old_graph, old_list_locations):
    # output: shortest_paths_between_homes
    predecessor, shortest = nx.floyd_warshall_predecessor_and_distance(old_graph)
    shortest_paths_between_homes = {}
    for (u, v) in new_graph.edges():
        # print("u,v : " + str(u) + " , " + str(v))
        left = old_list_locations.index(new_graph.nodes[u]['name'])
        right = old_list_locations.index(new_graph.nodes[v]['name'])
        #  print("(left,right): " + str(left) + " ," + str(right))
        new_graph[u][v]['weight'] = shortest[left][right]
        #  print(new_graph[u][v]['weight'])
        # u,v here is the index of newly created complete graph
        # left,right here is the index of old graph.
        # u <-> left, v <-> right
        shortest_paths_between_homes[(u, v)] = nx.reconstruct_path(left, right, predecessor)
        shortest_paths_between_homes[(v, u)] = nx.reconstruct_path(right, left, predecessor)
    return shortest_paths_between_homes


def complete_home_graph_generator_from_file(input_file, params=[]):
    input_data = utils.read_file(input_file)
    old_num_of_locations, old_num_houses, old_list_locations, old_list_houses, old_starting_car_location, old_adjacency_matrix = su.data_parser(
        input_data)

    # make a old graph from file
    old_graph, old_adj_message = su.adjacency_matrix_to_graph(old_adjacency_matrix)

    new_num_of_locations = -1
    new_list_locations = []

    new_num_houses = old_num_houses
    new_list_houses = old_list_houses
    new_starting_car_location = old_starting_car_location
    new_adjacency_matrix = None  # Flag
    shortest_paths_between_homes = None

    message = ''
    error = False
    old_starting_point_index = old_list_locations.index(old_starting_car_location)

    # Make complete_home_graph
    is_sp_home = None
    if old_starting_car_location in new_list_houses:
        is_sp_home = True
    if is_sp_home:
        print(" Sp is home, Complete Graph size = num_houses")
        complete_home_graph = nx.complete_graph(new_num_houses)
        new_num_of_locations = old_num_houses
        new_list_locations = old_list_houses
    else:
        # + 1 for the starting point
        print(" Sp is not home, Complete Graph size = num_houses + 1")
        complete_home_graph = nx.complete_graph(new_num_houses + 1)
        new_num_of_locations = old_num_houses + 1
        new_list_locations = old_list_houses.copy()
        new_list_locations.insert(0, old_starting_car_location)

    # For debugging
    # nx.draw(complete_home_graph)
    # plt.show()

    give_nodes_names(is_sp_home, complete_home_graph, new_num_houses, new_list_houses, new_starting_car_location)
    shortest_paths_between_homes = give_edges_weights(complete_home_graph, old_graph, old_list_locations)

    new_adjacency_matrix = nx.to_numpy_array(complete_home_graph)

    # tests
    if not all(name.isalnum() and len(name) <= MAX_NAME_LENGTH for name in new_list_locations):
        message += f'One or more of the names of your locations are either not alphanumeric or are above the max length of {MAX_NAME_LENGTH}.\n'
        error = True

    # check counts
    if len(new_list_locations) != new_num_of_locations:
        message += f'The number of locations you listed ({len(new_list_locations)}) differs from the number you gave on the first line ({new_num_of_locations}).\n'
        error = True

    if len(new_list_houses) != new_num_houses:
        message += f'The number of homes you listed ({len(new_list_houses)}) differs from the number you gave on the first line ({new_num_houses}).\n'
        error = True

    # # no more needed because in the new complete_home_graph, the number of houses = the number of locatinos
    # if num_of_locations < num_houses:
    #     message += f'The number of houses must be less than or equal to the number of locations.\n'
    #     error = True

    # check containment
    if any(house not in new_list_locations for house in new_list_houses):
        message += f'You listed at least one house that is not an actual location. Ahh!\n'
        error = True

    if new_starting_car_location not in new_list_locations:
        message += f'You listed a starting car location that is not an actual location.\n'
        error = True

    # check distinct
    if not len(set(new_list_locations)) == len(new_list_locations):
        message += 'The names of your locations are not distinct.\n'
        error = True

    if not len(set(new_list_houses)) == len(new_list_houses):
        message += 'The names of your houses are not distinct.\n'
        error = True
    # check adjacency matrix
    if not len(new_adjacency_matrix) == len(new_adjacency_matrix[0]) == new_num_of_locations:
        message += f'The dimensions of your adjacency matrix do not match the number of locations you provided.\n'
        error = True

    if not all(
            entry == 'x' or (type(entry) is float and entry > 0 and entry <= 2e9 and su.decimal_digits_check(entry)) for
            row in new_adjacency_matrix for entry in row):
        message += f'Your adjacency matrix may only contain the character "x", or strictly positive integers less than 2e+9, or strictly positive floats with less than 5 decimal digits.\n'
        error = True

    # if not square, terminate
    if len(set(map(len, new_adjacency_matrix))) != 1 or len(new_adjacency_matrix[0]) != len(new_adjacency_matrix):
        message += f'Your adjacency matrix must be square.\n'
        error = True
        return message, error

    new_adjacency_matrix_numpy = np.matrix(new_adjacency_matrix)

    # check requirements on square matrix
    if not np.all(new_adjacency_matrix_numpy.T == new_adjacency_matrix_numpy):
        message += f'Your adjacency matrix is not symmetric.\n'
        error = True

    if not nx.is_connected(complete_home_graph):
        message += 'Your new complete_home_graph is not connected.\n'
        error = True

    if not su.is_metric(complete_home_graph):
        message += 'Your new complete_home_graph is not metric.\n'
        error = True

    if not message:
        message = "If you've received no other error messages, then your complete_home_graph is valid!\n\n\n"

    # print for debugging
    print("\n old_num_of_locations : " + str(old_num_of_locations))
    print(" old_num_houses : " + str(old_num_houses))
    print(" old_list_locations names: " + str(old_list_locations))
    print(" old_list_houses names : " + str(old_list_houses))
    print(" Old Starting Point name(Str) : " + old_starting_car_location)
    print(" Old Starting Point index     : " + str(old_starting_point_index))

    print("\n New Complete Graph Generated")
    print(" new_num_of_locations names: " + str(new_num_of_locations))
    print(" new_num_houses names: " + str(new_num_houses))
    print(" new_list_locations names: " + str(new_list_locations))
    print(" new_list_houses: " + str(new_list_locations))
    new_starting_point_index = 0
    print(" New Starting Point name(Str) : " + old_starting_car_location)
    print(" ** New Starting Point index: " + str(new_starting_point_index))

    # print(" new_adjacency_matrix:")
    # print(new_adjacency_matrix)
    # print(" shortest_paths_between_homes: \n" + str(shortest_paths_between_homes))
    print("\n")
    # for edge in shortest_paths_between_homes:
    #     print(edge, ':', shortest_paths_between_homes[edge])
    # print("\n")
    return message, error, new_num_of_locations, new_num_houses, old_list_locations, new_list_locations, new_list_houses, \
           new_starting_car_location, new_adjacency_matrix, shortest_paths_between_homes, complete_home_graph, old_graph, new_starting_point_index


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parsing arguments')
    parser.add_argument('input', type=str, help='The path to the input file or directory')
    args = parser.parse_args()

    input_file = args.input
    complete_home_graph_generator_from_file(input_file)
