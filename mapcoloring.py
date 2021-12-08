# CS-UY 4613 Artificial Intelligence Project 2: Map Coloring
# Isabel Huey, Bianca Macias
# ijh234, bm2815

# Takes in the number of variables,
# the variable_names, the domain_values, the constraint_array, and the current assignments.
# Will return a list of the variable_names with the smallest amount of remaining values
# gonna have remaining_values be a list of lists so it is easy to index and remove values
def minimum_remaining_values(remaining_values, num_variables, variable_names, domain_values, constraint_array, assignments):
    # if the assignment is empty then return all of the variable names
    if assignments == {}:
        # min_remaing_values are all of the variables if there are no assignments
        print(remaining_values, variable_names)
        return (remaining_values, variable_names)

    # Reset Remaining Values
    # Make a list of lists of the domain_values
    # Have to remake this each time we calculate minimum_remaining_values in case an assignment has been removed
    remaining_values = []
    for num in range(num_variables):
        remaining_values.append(domain_values)

    # Edit the lsit of remaining values according to the assignments and the constraints
    for key in assignments:
        d_value = assignments[key]
        row = variable_name.index(key)
        constraint_row = constraint_array[row]
        for value in constraint_row:
            if value == 1:
                theVar = constraint_row.index(value)
                if d_value in remaining_values[theVar]:
                    remaining_values[theVar].remove(d_value)

    # Find the minimu_remaining values and store them in min_rem_values
    smallest_size = 0
    min_rem_values =[]
    for var in remaining_values:
        if var.size() != 0:
            if (smallest_size == 0) & (min_rem_values == []):
                smallest_size = var.size()
                index = remaining_values.index(var)
                min_rem_values.append(variable_names[index])
            elif var.size() < smallest_size:
                smallest_size = var.size()
                index = remaining_values.index(var)
                min_rem_values = []
                min_rem_values.append(variable_names[index])
            elif var.size() == smallest_size:
                index = remaining_values.index(var)
                min_rem_values.append(variable_names[index])

    print(remaining_values, min_rem_values)
    return (remaining_values, min_rem_values)

def degree_heuristic(remaining_values, min_rem_values, variable_names, constraint_array, assignments):
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
            print(constraint_row[index])
            if constraint_row[index] == '1':
                curr_degree_heursitic += 1
        degree_heuristics.append(curr_degree_heursitic)

    curr_highest_value = 0
    highest_degree_heuristic = None
    for value in degree_heuristics:
        if value > curr_highest_value:
            curr_highest_value = value
            index = degree_heuristics.index(value)
            highest_degree_heuristic = min_rem_values[index]
    return highest_degree_heuristic







# def order_domain_values(num_variables, num_domain_values, variable_names, domain_values, constraint_array, var, assignment):
# def inference(num_variables, num_domain_values, variable_names, domain_values, constraint_array, var, assignment):


def select_unassigned_variable(num_variables, num_domain_values, variable_names, domain_values, constraint_array, assignments):
    (remaining_values, min_rem_values) = minimum_remaining_values([], num_variables, variable_names, domain_values, constraint_array, assignments)
    selected_variable = degree_heuristic(remaining_values, min_rem_values, variable_names, constraint_array, assignments)
    return selected_variable

#returns a solution or failure
def backtrack(num_variables, num_domain_values, variable_names, domain_values, constraint_array, assignments):
    assigned_variables = []
    unassigned_variables = []
    for name in variable_names:
        if name in assignments:
            assigned_variables.append(name)
        else:
            unassigned_variables.append(name)
    if unassigned_variables == []:
        return assignments

    var = select_unassigned_variable(num_variables, num_domain_values, variable_names, domain_values, constraint_array, assignments)
    """
    order_domain = order_domain_values(csp,var,assignment)
    for each value in order_domain:
        if value is consistent with assignment:
            add {var = value} to assignment
            inferences = inference(csp, var, assignment)
            if inferences != failure:
                add inferences to csp
                result = backtrack(csp, assignment)
                if result != failure:
                    return result
                remove inferences from csp
            remove {var = value} from assignment
        return failure


    """


#returns a solution or failure
def backtracking_search(num_variables, num_domain_values, variable_names, domain_values, constraint_array):
    return backtrack(num_variables, num_domain_values, variable_names, domain_values, constraint_array, {})

def main():
    # Ask for input to obtain filename and try to open the file
    file = None
    while file == None:
        filename = input("Enter the name of the input file: ")
        try:
            file = open(filename, "r")
        except FileNotFoundError:
            print("File not found, try again")

    initial_state = []
    # Make a list of the initial input from the input file
    for line in file:
        line = line.strip()
        line = line.split(' ')
        initial_state.append(line)


    # Seperate and label the number of variables (regions) and the number of domain values (colors)
    num_variables = initial_state[0][0]
    num_domain_values = initial_state[0][1]
    # Seperate the list of variable names and list of domain values from the rest of the the_input
    variable_names = initial_state[1]
    domain_values = initial_state[2]
    # Seperate the array of constraints from the rest of the the_input
    constraint_array = initial_state[3:]


    goal_state = backtracking_search(num_variables, num_domain_values, variable_names, domain_values, constraint_array)





if __name__ == '__main__':
    main()
