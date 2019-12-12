import pdb


def walking(list_of_homes, path, occur_dict, sIndex, eIndex, walk_dict):
    # pdb.set_trace()
    index = sIndex
    while index < eIndex:
        if len(occur_dict[path[index]]) > 1:
            if occur_dict[path[index]][1] < eIndex:
                next_occurrence_index = occur_dict[path[index]][1]
                num_homes, homes = count_number_homes(path[(index + 1):next_occurrence_index], list_of_homes)
                # Get rid of current index in dict
                if num_homes > 1:
                    occur_dict[path[index]] = occur_dict[path[index]][1:]
                    path[(index + 1):next_occurrence_index] = walking(list_of_homes, path, occur_dict, index + 1,
                                                                      next_occurrence_index, walk_dict)
                    index += len(path[(index + 1):next_occurrence_index])
                elif num_homes == 1:
                    pathLength = len(path[index: next_occurrence_index])
                    for i in range(pathLength):
                        z = index + i
                        occur_dict[path[z]] = occur_dict[path[z]][1:]

                    walk_dict[path[index]].append(homes[0])
                    path[index: next_occurrence_index] = [-1] * pathLength
                    index += len(path[index: next_occurrence_index])
            else:
                # Get rid of current index in dict
                occur_dict[path[index]] = occur_dict[path[index]][1:]
                index += 1
        else:
            # Get rid of current index in dict
            occur_dict[path[index]] = occur_dict[path[index]][1:]
            index += 1
    return path[sIndex:eIndex]


def count_number_homes(subPath, list_of_homes):
    homes = []
    count = 0
    for i in subPath:
        if i in list_of_homes:
            homes.append(i)
            count += 1
    return count, homes


def create_occurrences(path):
    walk_dict = {}
    occur_dict = {}
    for i in set(path):
        occur_dict[i] = []
        walk_dict[i] = []
    for index, val in enumerate(path):
        occur_dict[val].append(index)
    return occur_dict, walk_dict


def main(path, list_of_homes):
    occur_dict, walk_dict = create_occurrences(path)
    path = walking(list_of_homes, path, occur_dict, 0, len(path), walk_dict)
    finalPath = []
    for index, val in enumerate(path):
        if path[index] != -1:
            finalPath.append(val)

    # print(walk_dict)
    return finalPath, walk_dict
