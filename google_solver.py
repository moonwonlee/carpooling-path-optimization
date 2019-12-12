from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import argparse
import utils

SCALING_FACTOR = 100000


def create_data_model(distance_matrix, start):
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = distance_matrix
    width = len(distance_matrix)

    for i in range(width):
        for j in range(width):
            distance_matrix[i][j] = distance_matrix[i][j] * SCALING_FACTOR
    # print(distance_matrix)
    data['num_vehicles'] = 1
    data['depot'] = start
    return data


def print_solution(manager, routing, assignment):
    """Prints assignment on console."""
    cost = assignment.ObjectiveValue() / SCALING_FACTOR
    print('\n Objective: {} miles'.format(cost))
    index = routing.Start(0)
    plan_output = ' Route for vehicle 0:\n'
    route_distance = 0
    route = []
    while not routing.IsEnd(index):
        route.append(manager.IndexToNode(index))
        plan_output += ' {} ->'.format(manager.IndexToNode(index))
        previous_index = index
        index = assignment.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    route.append(manager.IndexToNode(index))
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    plan_output += ' Route distance: {} miles\n'.format(route_distance / SCALING_FACTOR)
    print(plan_output)
    return route, cost


# Solve the problem with a given search set-up
def solve(routing, search_parameters, manager):
    assignment = routing.SolveWithParameters(search_parameters)
    route = []
    cost = -1
    # Print solution on console.
    if assignment:
        route, cost = print_solution(manager, routing, assignment)
    return route, cost

def first_search(search_parameters, strategy_name):
    """
    AUTOMATIC	Lets the solver detect which strategy to use according to the model being solved.
    PATH_CHEAPEST_ARC	Starting from a route "start" node, connect it to the node which produces the cheapest route segment, then extend the route by iterating on the last node added to the route.
    PATH_MOST_CONSTRAINED_ARC	Similar to PATH_CHEAPEST_ARC, but arcs are evaluated with a comparison-based selector which will favor the most constrained arc first. To assign a selector to the routing model, use the method ArcIsMoreConstrainedThanArc().
    EVALUATOR_STRATEGY	Similar to PATH_CHEAPEST_ARC, except that arc costs are evaluated using the function passed to SetFirstSolutionEvaluator().
    SAVINGS	Savings algorithm (Clarke & Wright). Reference: Clarke, G. & Wright, J.W.: "Scheduling of Vehicles from a Central Depot to a Number of Delivery Points", Operations Research, Vol. 12, 1964, pp. 568-581.
    SWEEP	Sweep algorithm (Wren & Holliday). Reference: Anthony Wren & Alan Holliday: Computer Scheduling of Vehicles from One or More Depots to a Number of Delivery Points Operational Research Quarterly (1970-1977), Vol. 23, No. 3 (Sep., 1972), pp. 333-344.
    CHRISTOFIDES	Christofides algorithm (actually a variant of the Christofides algorithm using a maximal matching instead of a maximum matching, which does not guarantee the 3/2 factor of the approximation on a metric travelling salesman). Works on generic vehicle routing models by extending a route until no nodes can be inserted on it. Reference: Nicos Christofides, Worst-case analysis of a new heuristic for the travelling salesman problem, Report 388, Graduate School of Industrial Administration, CMU, 1976.
    ALL_UNPERFORMED	Make all nodes inactive. Only finds a solution if nodes are optional (are element of a disjunction constraint with a finite penalty cost).
    BEST_INSERTION	Iteratively build a solution by inserting the cheapest node at its cheapest position; the cost of insertion is based on the global cost function of the routing model. As of 2/2012, only works on models with optional nodes (with finite penalty costs).
    PARALLEL_CHEAPEST_INSERTION	Iteratively build a solution by inserting the cheapest node at its cheapest position; the cost of insertion is based on the arc cost function. Is faster than BEST_INSERTION.
    LOCAL_CHEAPEST_INSERTION	Iteratively build a solution by inserting each node at its cheapest position; the cost of insertion is based on the arc cost function. Differs from PARALLEL_CHEAPEST_INSERTION by the node selected for insertion; here nodes are considered in their order of creation. Is faster than PARALLEL_CHEAPEST_INSERTION.
    GLOBAL_CHEAPEST_ARC	Iteratively connect two nodes which produce the cheapest route segment.
    LOCAL_CHEAPEST_ARC	Select the first node with an unbound successor and connect it to the node which produces the cheapest route segment.
    FIRST_UNBOUND_MIN_VALUE	Select the first node with an unbound successor and connect it to the first available node. This is equivalent to the CHOOSE_FIRST_UNBOUND strategy combined with ASSIGN_MIN_VALUE (cf. constraint_solver.h).rategy_name:
    """

    if strategy_name == "AUTOMATIC":
        search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.AUTOMATIC)
    if strategy_name == "PATH_CHEAPEST_ARC":
        search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    if strategy_name == "PATH_MOST_CONSTRAINED_ARC":
        search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_MOST_CONSTRAINED_ARC)
    if strategy_name == "EVALUATOR_STRATEGY":
        search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.EVALUATOR_STRATEGY)
    if strategy_name == "SAVINGS":
        search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.SAVINGS)
    if strategy_name == "SWEEP":
        search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.SWEEP)
    if strategy_name == "CHRISTOFIDES":
        search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.CHRISTOFIDES)
    if strategy_name == "ALL_UNPERFORMED":
        search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.ALL_UNPERFORMED)
    if strategy_name == "BEST_INSERTION":
        search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.BEST_INSERTION)
    if strategy_name == "PARALLEL_CHEAPEST_INSERTION":
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PARALLEL_CHEAPEST_INSERTION)
    if strategy_name == "LOCAL_CHEAPEST_INSERTION":
        search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.LOCAL_CHEAPEST_INSERTION)
    if strategy_name == "GLOBAL_CHEAPEST_ARC":
        search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.GLOBAL_CHEAPEST_ARC)
    if strategy_name == "LOCAL_CHEAPEST_ARC":
        search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.LOCAL_CHEAPEST_ARC)
    if strategy_name == "FIRST_UNBOUND_MIN_VALUE":
        search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.FIRST_UNBOUND_MIN_VALUE)
    return search_parameters
def local_search(search_parameters, strategy_name):
    """
       AUTOMATIC	Lets the solver select the metaheuristic.
       GREEDY_DESCENT	Accepts improving (cost-reducing) local search neighbors until a local minimum is reached.
       GUIDED_LOCAL_SEARCH	Uses guided local search to escape local minima (cf. http://en.wikipedia.org/wiki/Guided_Local_Search); this is generally the most efficient metaheuristic for vehicle routing.
       SIMULATED_ANNEALING	Uses simulated annealing to escape local minima (cf. http://en.wikipedia.org/wiki/Simulated_annealing).
       TABU_SEARCH	Uses tabu search to escape local minima (cf. http://en.wikipedia.org/wiki/Tabu_search).
       """
    # Local Search
    if strategy_name == "AUTOMATIC":
        search_parameters.local_search_metaheuristic = (routing_enums_pb2.LocalSearchMetaheuristic.AUTOMATIC)
    if strategy_name == "GREEDY_DESCENT":
        search_parameters.local_search_metaheuristic = (routing_enums_pb2.LocalSearchMetaheuristic.GREEDY_DESCENT)
    if strategy_name == "GUIDED_LOCAL_SEARCH":
        search_parameters.local_search_metaheuristic = (routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)
    if strategy_name == "SIMUALTED_ANNEALING":
        search_parameters.local_search_metaheuristic = (routing_enums_pb2.LocalSearchMetaheuristic.SIMULATED_ANNEALING)
    if strategy_name == "TABU_SEARCH":
        search_parameters.local_search_metaheuristic = (routing_enums_pb2.LocalSearchMetaheuristic.TABU_SEARCH)

    search_parameters.time_limit.seconds = 30 # Max is 30
    search_parameters.log_search = True
    return search_parameters


# main used in solver.py as a tsp google solver
def main(distance_matrix, start):
    """Entry point of the program."""
    # Instantiate the data problem that starts at give start
    data = create_data_model(distance_matrix, start)

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    names_first_strategies = ["AUTOMATIC", "PATH_CHEAPEST_ARC", "PATH_MOST_CONSTRAINED_ARC", "EVALUATOR_STRATEGY",
                              "SAVINGS", "SWEEP", "CHRISTOFIDES", "ALL_UNPERFORMED", "BEST_INSERTION",
                              "PARALLEL_CHEAPEST_INSERTION", "LOCAL_CHEAPEST_INSERTION", "GLOBAL_CHEAPEST_ARC",
                              "LOCAL_CHEAPEST_ARC", "FIRST_UNBOUND_MIN_VALUE"]
    names_local_strategies = ["AUTOMATIC", "GREEDY_DESCENT", "GUIDED_LOCAL_SEARCH", "SIMULATED_ANNEALING", "TABU_SEARCH"]

    print(
        "---<< Google Search Initiated >>-----------------------------------------------------------------------------------")
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    list_search_parameters = {}
    # first search
    for i in range(14):
        list_search_parameters[i] = first_search(search_parameters, names_first_strategies[i])

    # local search
    routes = {}
    costs = {}

    best_cost = -1
    best_strategy_index = "" # example : (automatic, automatic)
    for i in range(14):
        for j in range(5):
            if (i, j) == (0, 0):
                routes[(0, 0)], costs[(0, 0)] = solve(routing,
                                                    local_search(list_search_parameters[0], names_local_strategies[j]),
                                                    manager)
                best_cost = costs[(0, 0)]
                best_strategy_index = (i,j)
            routes[(i, j)], costs[(i, j)] = solve(routing,
                                                local_search(list_search_parameters[i], names_local_strategies[j]),
                                                manager)
            if best_cost > costs[(i, j)]:
                best_cost = costs[(i, j)]
                best_strategy_index = (i,j)

    print("----<< Google Search Over >>-----------------------------------------------------------------------------------")
    print(" ** Driving Costs of Routes of Different Strategies of Google for the Complete Graph")
    for i in range(14):
        for j in range(5):
            print(" * " + str((i, j)) + "          cost = " + str(costs[i,j]))

    print(" ****** " + str(best_strategy_index) + " is the best before Walking-Optimization\n")

    print(" *** Not Full, Not-Walking-Optimized Routes in index (Google Routes)")
    for i in range(14):
        for j in range(5):
            print(" * " + str((i, j)) + " (nodes in index): " + str(routes[(i, j)]))
    """
    * returns the results of all strategies and costs for complete graphs
    * does not return best_route and best_result because they does not consider the walking optimization.
    * so we just return all the strategies' routes and costs
    """
    return routes, costs, best_strategy_index
