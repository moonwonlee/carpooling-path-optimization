def makeIn(input_file, output_directory, params=[]):
    print('Processing', input_file)
    #input file is the path
    #get data from file and make an 2d array
    input_data = utils.read_file(input_file)
    #take data from 2d array and assign value to each of the parameters we gonna use
    num_of_locations, num_houses, list_locations, list_houses, starting_car_location, adjacency_matrix = data_parser(input_data)
    #the first parameters are not interested for solve.
    #drop_offs :  A dictionary mapping drop-off location to a list of homes of TAs that got off at that particular location
    car_path, drop_offs = solve(list_locations, list_houses, starting_car_location, adjacency_matrix, params=params)

    basename, filename = os.path.split(input_file)
    # we get output file directory from args probably.
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    output_file = utils.input_to_output(input_file, output_directory)
    #this one does all the job for us
    convertToFile(car_path, drop_offs, output_file, list_locations)