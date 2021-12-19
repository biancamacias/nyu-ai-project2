# CS-UY 4613 Artificial Intelligence Project 2: Map Coloring
# Isabel Huey, Bianca Macias
# ijh234, bm2815

import copy
# Takes in the number of variables,
# the variable_names, the domain_values, the constraint_array, and the current assignments.
# Will return a list of the variable_names with the smallest amount of remaining values
# gonna have remaining_values be a list of lists so it is easy to index and remove values
def minimum_remaining_values(prev_d_value, remaining_domains, num_variables, \
    variable_names, domain_values, constraint_array, assignments):
    # if the assignment is empty then return all of the variable names
    if assignments == {}:
        # min_remaing_values are all of the variables if there are no assignments
        return variable_names

    # Find the minimum_remaining values and store them in min_rem_values
    smallest_size = 0
    min_rem_values = []
    index = 0
    for var in remaining_domains:
        if var != []:
            if (smallest_size == 0) & (min_rem_values == []):
                smallest_size = len(var)
                min_rem_values.append(variable_names[index])
            elif len(var) < smallest_size:
                smallest_size = len(var)
                min_rem_values = []
                min_rem_values.append(variable_names[index])
            elif len(var) == smallest_size:
                min_rem_values.append(variable_names[index])
        index += 1
    return min_rem_values

def degree_heuristic(prev_d_value, min_rem_values, \
    variable_names, constraint_array, assignments):
    # Does the degree heursitic still count the adjacent regions that
    # are not being affected because another region alreay took a color choice from them?
    list_of_indexes = []
    for variable in variable_names:
        if variable not in assignments:
            list_of_indexes.append(variable_names.index(variable))

    degree_heuristics = []
    for variable in min_rem_values:
        curr_degree_heursitic = 0
        current_var_index = variable_names.index(variable)
        constraint_row = constraint_array[current_var_index]
        for index in list_of_indexes:
            if constraint_row[index] == '1':
                curr_degree_heursitic += 1
        degree_heuristics.append(curr_degree_heursitic)

    # should fix if works to get rid of repetitiveness of checking the same value twice
    curr_highest_value = degree_heuristics[0]
    if min_rem_values == []:
        return None
    highest_degree_heuristic = min_rem_values[0]
    for value in degree_heuristics[1:]:
        if value >= curr_highest_value:
            curr_highest_value = value
            index = degree_heuristics.index(value)
            highest_degree_heuristic = min_rem_values[index]
    return highest_degree_heuristic

# uses forward checking to remove values from unassigned variable domains
def inference(num_variables, num_domain_values, variable_names, domain_values, \
    constraint_array, assignments):
    # Reset Remaining Values
    # Make a list of lists of the domain_values
    # Have to remake this each time we calculate minimum_remaining_values in case an assignment has been removed
    remaining_domains = []
    for num in range(num_variables):
        curr_copy = copy.deepcopy(domain_values)
        remaining_domains.append(curr_copy)

    # Edit the list of remaining values according to the assignments and the constraints
    for key in assignments:
        d_value = assignments[key]
        row = variable_names.index(key)
        constraint_row = constraint_array[row]
        if key in assignments:
            remaining_domains[row] = []
        counter = 0
        for value in constraint_row:
            if value == '1':
                if d_value in remaining_domains[counter]:
                    index = remaining_domains[counter].index(d_value)
                    del remaining_domains[counter][index]
            counter += 1
    return remaining_domains

# Call the minimin_remaining_values function in order to get the remaining domain
# values of each variable and to get a list of the variables with the
# minimum_remaining_values. Use these found values in the degree_heuristic call
# and select the variable to assign next. Get the index of this variable from
# the variable_names list and use the index to index the list of
# remaining values in order to retreive the remaining values for this variable.
def select_unassigned_variable(prev_d_value, num_variables, num_domain_values, \
    remaining_domains, variable_names, domain_values, constraint_array, assignments):
    min_rem_values = minimum_remaining_values(prev_d_value, \
     remaining_domains, num_variables, variable_names, domain_values, constraint_array, assignments)
    #print(remaining_values, min_rem_values)
    selected_variable = degree_heuristic(prev_d_value, \
        min_rem_values, variable_names, constraint_array, assignments)
    return selected_variable

# returns a solution or failure
def backtrack(prev_d_value, num_variables, num_domain_values, \
    remaining_domains, variable_names, domain_values, constraint_array, assignments):
    assigned_variables = []
    unassigned_variables = []
    succeed = True
    # Base Case
    for name in variable_names:
        if name in assignments:
            assigned_variables.append(name)
        else:
            unassigned_variables.append(name)
    if unassigned_variables == []:
        return assignments

    variable = select_unassigned_variable(prev_d_value, \
        num_variables, num_domain_values, remaining_domains, variable_names, \
        domain_values, constraint_array, assignments)
    if (variable == None):
        return None
    index = variable_names.index(variable)
    for value in reversed(remaining_domains[index]):
    # for value in possible_values:
        assignments[variable] = value
        remaining_domains = inference(num_variables, num_domain_values, \
            variable_names, domain_values, constraint_array, assignments)
        result = backtrack(value, num_variables, num_domain_values, remaining_domains, \
            variable_names, domain_values, constraint_array, assignments)
        if result != None:
            return assignments
        del assignments[variable]
    return None

# Print the assignements in the proper format
def output(variable_names, assignments, output_filename):
    output_file = open(output_filename, "w")
    for key in variable_names:
        print(key + " = " + assignments[key], file = output_file)
    output_file.close()

def main():
    # Ask for input to obtain filename and try to open the file
    file = None
    while file == None:
        filename = input("Enter the name of the input file: ")
        try:
            file = open(filename, "r")
        except FileNotFoundError:
            print("File not found, try again")
    output_filename = input("Enter output filename: ")


    initial_state = []
    # Make a list of the initial input from the input file
    for line in file:
        line = line.strip()
        line = line.split(' ')
        initial_state.append(line)

    # Seperate and label the number of variables (regions) and the number of domain values (colors)
    num_variables = int(initial_state[0][0])
    num_domain_values = int(initial_state[0][1])
    # Seperate the list of variable names and list of domain values from the rest of the the_input
    variable_names = initial_state[1]
    domain_values = initial_state[2]
    # Seperate the array of constraints from the rest of the the_input
    constraint_array = initial_state[3:]

    remaining_domains = []
    for num in range(num_variables):
        curr_copy = copy.deepcopy(domain_values)
        remaining_domains.append(curr_copy)

    goal_state = backtrack(None, num_variables, num_domain_values, remaining_domains, \
        variable_names, domain_values, constraint_array, {})
    output(variable_names, goal_state, output_filename)
    file.close()

if __name__ == '__main__':
    main()
